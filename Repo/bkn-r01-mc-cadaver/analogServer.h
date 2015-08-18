#pragma once
#include <windows.h>
#include <process.h>
#include <stdio.h>
#include "LoadCellData.h"
class analogServer
{

	int kill;
	HANDLE hIOMutex;
	DWORD delayThread;
	LoadCellData *pLoadCellData;
	static void staticanalogServerCallback(void*);
	void analogServerCallback(void);
	bool messageIdle;
public:
	bool bNotConnected;
	bool bReceivedTTT;
	bool bReceivedKKK;
	bool bReceivedPPP;
	bool bReceivedRRR;
	bool bReceivedName;
	double voltageValue;
	char sNameOfDataFile[512];

	analogServer(LoadCellData*);
	~analogServer();
};

