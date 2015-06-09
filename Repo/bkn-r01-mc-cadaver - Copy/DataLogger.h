#pragma once
#define WIN32_LEAN_AND_MEAN
#include <windows.h>
#include <stdio.h>
#include <string.h>
#include <process.h>
#include <time.h>
#include <iostream>
#include "EncoderData.h"

// Data Logging Class
// Allows us to record data by giving the function the values from 
// global variables or from variables calculated in data adquisition
// classes or others
class DataLogger
{
public:

	char gTimeStamp[100];
	char dataString[400];
	bool isRecording;

	DataLogger(DWORD);	// Always use this constructor!!!
	~DataLogger(void);

	int startRecording(void);
	int stopRecording(void);
	static void staticRecordingCallback(void* param);
    void recordingCallback(void);
    void sendLogString(char *);

private:
	FILE *data;
	int kill;
	HANDLE hIOMutex;	
	DWORD delayThread;
};