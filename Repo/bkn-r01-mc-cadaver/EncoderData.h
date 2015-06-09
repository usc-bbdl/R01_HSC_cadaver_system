#pragma once
#include <windows.h>
#include <process.h>
#include <stdio.h>
#include <time.h>
#include "include/cbw.h"
#include "TimeData.h"

#ifdef _WIN64
#	pragma comment(lib, "lib/x64/cbw64.lib")
#else
#	pragma comment(lib, "lib/x86/cbw32.lib")
#endif

class EncoderData
{
	//Global Encoder Variables
	int numEncoderBoard;
	int ULStat;
	int counterNum, mapChannel;
	static const int numChannels = 7;
	int mode, debounceTime, debounceMode, edgeDetection, tickSize;
	DWORD counterData[numChannels];
	double ticksPerRev;

	// Recording Multiple Trials
	bool bClosingFile;
	char sDirectoryContainer[512];
	char sDataHeader[600];
	int fileOpenCounter;
	char sFileName[400];
	FILE *dataFile;
	int kill;
	HANDLE hIOMutex;	
	bool bInSingleTrial;

	int stopRecording(void);

public:
	TimeData timeData;
	bool bIsRecording; 
	EncoderData(char* sDirectoryContainer, char* sDataHeader);
	~EncoderData(void);
	ULONG volatile outDisplayValuesULONG[8];
	ULONG volatile outLoggingValuesULONG[8];
	static void staticEncoderCallback(void*);
	void encoderCallback(void);
	
	// Recording Multiple Trials
	int startRecording(void);
	int closeRecordingFile(void);
	int setFileName(char *);
};

