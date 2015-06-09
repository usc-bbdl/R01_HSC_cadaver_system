#include "EncoderData.h"

EncoderData::EncoderData(char *sDirectoryContainer, char *sDataHeader)
{
	bInSingleTrial = false;
	bClosingFile = false;
    	strcpy_s(this->sDirectoryContainer, sDirectoryContainer);
	strcpy_s(this->sDataHeader, sDataHeader);
	fileOpenCounter = 0;
    	bIsRecording = false;

	numEncoderBoard = 1;
	ULStat = 0;
	counterNum = 0;
	mode = ENCODER | ENCODER_MODE_X4 | CLEAR_ON_Z_OFF;
	debounceTime = CTR_DEBOUNCE_NONE;
	debounceMode = 0;
	edgeDetection = CTR_RISING_EDGE;
	tickSize = 0;
	mapChannel = 0;
	cbErrHandling(PRINTALL, DONTSTOP);
	ticksPerRev = 2000.0;	// For X4 configuration

	hIOMutex = CreateMutex(NULL, FALSE, NULL);
	kill = 0;
	_beginthread(EncoderData::staticEncoderCallback, 0, this);

}


EncoderData::~EncoderData(void)
{
	bIsRecording = false;
	kill = 1;
}

void EncoderData::encoderCallback(void)
{
	// Initialize encoders
	//+++ Iterate
	for (int i = 0; i < numChannels; i++) {
		ULStat = cbCConfigScan(	numEncoderBoard, i, mode, debounceTime,
					debounceMode, edgeDetection, tickSize, mapChannel);
	}

	// Query data looop
	while (!kill) {

		WaitForSingleObject(hIOMutex, INFINITE);

		// Query data for this frame
		double currSampleTime = timeData.getCurrentTime();
		for (int i = 0; i < numChannels; i++) {
			cbCIn32(numEncoderBoard, i, &counterData[i]);
			outDisplayValuesULONG[i] = counterData[i];
			outLoggingValuesULONG[i] = counterData[i];
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
						",%u", 
						outLoggingValuesULONG[i]
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

void EncoderData::staticEncoderCallback(void* a) {
	((EncoderData*)a)->encoderCallback();
}

// Corresponds to the R message
int EncoderData::startRecording()
{
	bIsRecording = true;
	return 0;
}

// Corresponds to the T message
int EncoderData::stopRecording()
{
	bIsRecording = false;
	return 0;
}

int EncoderData::closeRecordingFile()
{
	bClosingFile = true;
	stopRecording();
	return 0;
}


// Corresponds to the N message
int EncoderData::setFileName(char *inFileName)
{
	sprintf_s(
		sFileName, 
		sDirectoryContainer, 
		inFileName
		);
	bInSingleTrial = true;
	return 0;
}