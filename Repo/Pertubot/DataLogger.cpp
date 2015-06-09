#include "DataLogger.h"

DataLogger::DataLogger(DWORD delayMS, char *sDirectoryContainer, char *sDataHeader)
{
	bInSingleTrial = false;
	bClosingFile = false;
	this->delayMS = delayMS;
	strcpy_s(this->sDirectoryContainer, sDirectoryContainer);
	strcpy_s(this->sDataHeader, sDataHeader);
	fileOpenCounter = 0;
	
	hIOMutex = CreateMutex(NULL, FALSE, NULL);
	kill = 0;
	bIsRecording = false;
	_beginthread(DataLogger::staticRecordingCallback, 0, this);
}

DataLogger::~DataLogger(void)
{
	bIsRecording = false;
	kill = 1;
}

void DataLogger::sendLogString(char *logString)
{
	strcpy_s(sData, logString);
}

void DataLogger::recordingCallback() 
{ 
	int count = 0;

	while (!kill) {
		if(delayMS > 0) {
			Sleep(delayMS); 
		}
		WaitForSingleObject(hIOMutex, INFINITE);

		if (bInSingleTrial) {
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
				fprintf(dataFile, "%s", sData);
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


void DataLogger::staticRecordingCallback(void* a) {
	//std::cout << "In threadFunc\n";
	((DataLogger*)a)->recordingCallback();
}


// Corresponds to the R message
int DataLogger::startRecording()
{
	bIsRecording = true;
	return 0;
}

// Corresponds to the T message
int DataLogger::stopRecording()
{
	bIsRecording = false;
	return 0;
}

int DataLogger::closeRecordingFile()
{
	bClosingFile = true;
	stopRecording();
	return 0;
}


// Corresponds to the N message
int DataLogger::setFileName(char *inFileName)
{
	sprintf_s(
		sFileName, 
		sDirectoryContainer, 
		inFileName
		);
	bInSingleTrial = true;
	return 0;
}
//??? IoC way of building DataLogger:
