#include "DataLogger.h"

void DataLogger::sendLogString(char *logString)
{
	strcpy_s(dataString, logString);
}

void DataLogger::recordingCallback() 
{ 
	double tim = 0.0;
	time_t rawtime;
	struct tm *timeInfo;
	time(&rawtime);
	timeInfo = localtime(&rawtime);
#ifdef _WIN64
	sprintf_s(gTimeStamp, "x64_%4d%02d%02d%02d%02d_Generic.txt", timeInfo->tm_year + 1900, timeInfo->tm_mon + 1, timeInfo->tm_hour, timeInfo->tm_min);
#else
	sprintf_s(gTimeStamp, "x86_%4d%02d%02d%02d%02d_Generic.txt", timeInfo->tm_year + 1900, timeInfo->tm_mon + 1, timeInfo->tm_hour, timeInfo->tm_min);
#endif
	data = fopen(gTimeStamp, "w");
	while (!kill) {
		if (isRecording == 1) {
			Sleep(delayThread); 

			//+++ Check multithreading
			WaitForSingleObject(hIOMutex, INFINITE);

			fprintf(data, "%s", dataString);

			ReleaseMutex( hIOMutex);
		}
	}
}


DataLogger::DataLogger(DWORD delay)
{
	hIOMutex = CreateMutex(NULL, FALSE, NULL);
	kill = 0;
	isRecording = false;
	delayThread = delay;
	_beginthread(DataLogger::staticRecordingCallback, 0, this);
}

void DataLogger::staticRecordingCallback(void* a) {
	//std::cout << "In threadFunc\n";
	((DataLogger*)a)->recordingCallback();
}

DataLogger::~DataLogger(void)
{
	isRecording = false;
	kill = 1;
	fclose(data);
}

int DataLogger::startRecording()
{
	isRecording = true;
	return 0;
}

//??? IoC way of building DataLogger:
