#include "LoadCellData.h"

LoadCellData::LoadCellData(char *sDirectoryContainer, char *sDataHeader)
{
	loadCellConfigFile = fopen("C:\\config\\loadcell_calibration.txt","r");
	
	bInSingleTrial = false;
	bClosingFile = false;
    	strcpy_s(this->sDirectoryContainer, sDirectoryContainer);
	strcpy_s(this->sDataHeader, sDataHeader);
	fileOpenCounter = 0;
    	bIsRecording = false;

	if (loadCellConfigFile != NULL) {
		for (int i = 0; i < numChannels; i++) {
			fscanf(
				loadCellConfigFile, 
				"%lf %lf\n", 
				&loadCellIntercept[i],
				&loadCellSlope[i]
			);
		}
	}
	else {
		MessageBoxA(
			NULL, 
			"Could not find load cell config file in C:\\config",
			"", 
			MB_OK
		);
	}

	CPhidgetBridge_create(&bridge1);
	CPhidgetBridge_create(&bridge2);

	CPhidget_set_OnAttach_Handler((CPhidgetHandle)bridge1, AttachHandlerBridge, NULL);
	CPhidget_set_OnAttach_Handler((CPhidgetHandle)bridge2, AttachHandlerBridge, NULL);

	CPhidget_open((CPhidgetHandle)bridge1, 293182);
	CPhidget_open((CPhidgetHandle)bridge2, 341581);

	hIOMutex = CreateMutex(NULL, FALSE, NULL);
	kill = 0;
	delayThread = 10;

	_beginthread(LoadCellData::staticLoadCellCallback, 0, this);
}


LoadCellData::~LoadCellData(void)
{
	bIsRecording = false;
	kill = 1;

	CPhidget_close((CPhidgetHandle)bridge1);
	CPhidget_close((CPhidgetHandle)bridge2);

	CPhidget_delete((CPhidgetHandle)bridge1);
	CPhidget_delete((CPhidgetHandle)bridge2);
}

void LoadCellData::loadCellCallback(void)
{
	// Query data looop
	while (!kill) {

		Sleep(delayThread); 
		WaitForSingleObject(hIOMutex, INFINITE);

		// Query data for this frame
		double currSampleTime = timeData.getCurrentTime();
		getLoadCellData();
		for(int i = 0; i < numChannels; i++) {
			outDisplayValues[i] = loadCellValue[i];
			outForceControllerValues[i] = loadCellValue[i];
			outLoggingValues[i] = loadCellValue[i];
		}

		if (bInSingleTrial) {
			// Recording for this frame
			if (fileOpenCounter == 0) {
				dataFile = fopen(sFileName, "w");
				if (dataFile == NULL) {
					MessageBoxA(
						NULL, 
						"Could not open data file", 
						"File Error",
						MB_OK
					);
				}

				fprintf(
					dataFile,
					sDataHeader
				);
				fileOpenCounter++;
			}

			if(fileOpenCounter == 1 && bIsRecording) {
				fprintf(dataFile, "%f", currSampleTime);
				for(int i = 0; i < numChannels; i++) {
					fprintf(
						dataFile, 
						",%.3f", 
						outLoggingValues[i]
					);
				}
				fprintf(
					dataFile, 
					"\n" 
					);
			}

			if(fileOpenCounter == 1 && bClosingFile) {
				if(dataFile != NULL) {
					fclose(dataFile);
				}
				// If this was successfull then exit the single trial and reset flags
				dataFile = NULL;
				fileOpenCounter = 0;
				bClosingFile = false;
				bInSingleTrial = false;

			}   

		}
		ReleaseMutex( hIOMutex);
	}

}

void LoadCellData::staticLoadCellCallback(void* a) {
	((LoadCellData*)a)->loadCellCallback();
}

// Non blocking, needs a separate thread for logging
int LoadCellData::getLoadCellData()
{
	double tempLoadcell[8];
	for(int i = 0; i < 4; i++) {
		CPhidgetBridge_getBridgeValue(bridge1, i, tempLoadcell + i);
		CPhidgetBridge_getBridgeValue(bridge2, i, tempLoadcell + i + 4);
	}

	for(int i = 0; i < numChannels; i++) {
		//loadCellValue[i] = tempLoadcell[i];
		loadCellValue[i] = loadCellIntercept[i] + tempLoadcell[i] * loadCellSlope[i];
	}
	return 0;
}	

int LoadCellData::stopRecording(void)
{
	bIsRecording = false;
	return 0;
}


int LoadCellData::startRecording(void)
{
	bIsRecording = true;
	return 0;
}

int LoadCellData::closeRecordingFile()
{
	bClosingFile = true;
	stopRecording();
	return 0;
}

int CCONV AttachHandlerBridge(CPhidgetHandle phid, void *userptr)
{
	CPhidgetBridgeHandle bridge = (CPhidgetBridgeHandle)phid;

	CPhidgetBridge_setEnabled(bridge, 0, PTRUE);
	CPhidgetBridge_setEnabled(bridge, 1, PTRUE);
	CPhidgetBridge_setEnabled(bridge, 2, PTRUE);
	CPhidgetBridge_setEnabled(bridge, 3, PTRUE);

	CPhidgetBridge_setGain(bridge, 0, PHIDGET_BRIDGE_GAIN_128);
	CPhidgetBridge_setGain(bridge, 1, PHIDGET_BRIDGE_GAIN_128);
	CPhidgetBridge_setGain(bridge, 2, PHIDGET_BRIDGE_GAIN_128);
	CPhidgetBridge_setGain(bridge, 3, PHIDGET_BRIDGE_GAIN_128);

	CPhidgetBridge_setDataRate(bridge, 1);

	return 0;
}

// Corresponds to the N message
int LoadCellData::setFileName(char *inFileName)
{
	sprintf_s(
		sFileName, 
		sDirectoryContainer, 
		inFileName
		);
	bInSingleTrial = true;
	return 0;
}

