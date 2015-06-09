#pragma once
#include <windows.h>
#include <process.h>
#include <stdio.h>
#include <time.h>
#include "include/phidget21.h"
#include "TimeData.h"


#ifdef _WIN64
#	pragma comment(lib, "lib/x64/phidget21.lib")
#else
#	pragma comment(lib, "lib/x86/phidget21.lib")
#endif

//+++ Propertly encapsulate callback
int CCONV AttachHandlerBridge(CPhidgetHandle, void *);

class LoadCellData
{
	//+++ Add status string to send to console
	// or other debugging output
	CPhidgetBridgeHandle bridge1;
	CPhidgetBridgeHandle bridge2;

	static const int numChannels = 7;
	FILE *loadCellConfigFile;

	double loadCellIntercept[numChannels];
	double loadCellSlope[numChannels];
	
	int kill;
	HANDLE hIOMutex;	
	DWORD delayThread;

	// Recording Multiple Trials
	bool bClosingFile;
	char sDirectoryContainer[512];
	char sDataHeader[600];
	int fileOpenCounter;
	char sFileName[400];
	FILE *dataFile;
	bool bInSingleTrial;
	int stopRecording(void);

public:
	bool bIsRecording; 
	TimeData timeData;

	double loadCellValue[8];
	LoadCellData(char* sDirectoryContainer, char* sDataHeader);
	~LoadCellData();
	int getLoadCellData();
	double volatile outDisplayValues[8];
	double volatile outLoggingValues[8];
	double volatile outForceControllerValues[8];

	static void staticLoadCellCallback(void*);
	void loadCellCallback(void);


	// Recording Multiple Trials
	int startRecording(void);
	int closeRecordingFile(void);
	int setFileName(char *);
};
