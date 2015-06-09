#pragma once
#define WIN32_LEAN_AND_MEAN
#include <windows.h>
#include <stdio.h>
#include <string.h>
#include <process.h>
#include <time.h>
#include <iostream>

// Data Logging Class
// Allows us to record data by giving the function the values from 
// global variables or from variables calculated in data adquisition
// classes or others
class DataLogger
{
public:
	
	bool bIsRecording;   // Used to let user know the recording state

	DataLogger(DWORD delayMS, char* sDirectoryContainer, char* sDataHeader);
	~DataLogger(void);

	int startRecording(void);
	int closeRecordingFile(void);
	void sendLogString(char *);
	int setFileName(char *);

private:
	static void staticRecordingCallback(void* param);
	void recordingCallback(void);
	int stopRecording(void);

	bool bClosingFile;
	char sDirectoryContainer[512];
	char sData[600];
	char sDataHeader[600];
	int fileOpenCounter;
	char sFileName[400];
	FILE *dataFile;
	int kill;
	HANDLE hIOMutex;	
	DWORD delayMS;
	bool bInSingleTrial;
};