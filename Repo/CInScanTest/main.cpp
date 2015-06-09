/*CInScan02.C****************************************************************

File:                         CInScan01.C

Library Call Demonstrated:    cbCInScan(), FOREGROUND mode

Purpose:                      Scans a range of Counter Input Channels and stores
                                the sample data in an array.

Demonstration:                Displays the counter input on two channels.
                              Continuously updates the display
                              until a key is pressed.

Other Library Calls:          cbErrHandling()

Special Requirements:         Board 0 must support counter scan function.
                              TTL signals on selected counter inputs.

Copyright (c) 1995-2006, Measurement Computing Corp.
All Rights Reserved.
***************************************************************************/


/* Include files */
#include <windows.h>
#include <stdio.h>
#include <conio.h>
#include <stdlib.h>
#include "include/cbw.h"
#include "TimeData.h"

#ifdef _WIN64
#	pragma comment(lib, "lib/x64/cbw64.lib")
#else
#	pragma comment(lib, "lib/x86/cbw32.lib")
#endif

void ClearScreen()
{
	system("cls");
}

const int numActiveChannels = 2;		// LastCtr - FirstCtr + 1;	SET THIS MANUALLY
const int numValuesPerChannel = 1;		// Count / numActiveChannels; SET THIS MANUALLY
long Count = 80;
DWORD CounterData[80];

void main ()
{
	/* Variable Declarations */
	int I;
	int BoardNum = 1;
	int ULStat = 0;
	int FirstCtr = 0;
	int LastCtr = 1;
	int CounterNum, MapChannel;
	int Mode, DebounceTime, DebounceMode, EdgeDetection, TickSize;

	long Rate = 10;


	unsigned Options;
	TimeData timeData;

    cbErrHandling (PRINTALL, DONTSTOP);

	CounterNum = 0;
	Mode = ENCODER | ENCODER_MODE_X4 | CLEAR_ON_Z_OFF;
	DebounceTime = CTR_DEBOUNCE_NONE;
	DebounceMode = CTR_TRIGGER_BEFORE_STABLE;
	EdgeDetection = CTR_RISING_EDGE;
	TickSize = 0;
	MapChannel = 0;

	ULStat = cbCConfigScan(BoardNum, CounterNum, Mode, DebounceTime, DebounceMode, EdgeDetection, TickSize, MapChannel);

    Options = CTR32BIT | BACKGROUND | CONTINUOUS;
    printf ("Done initializing\n\n");

	getch();
	printf("Logging Data\n\n");

	ULStat = cbCInScan (BoardNum, FirstCtr, LastCtr, Count, &Rate, CounterData, Options);

	double currTime;
	FILE *testData;
	testData = fopen("newestData.txt", "w");
	for(;;)
	{
		if(kbhit())
			break;
		Sleep(100);
		currTime = timeData.getCurrentTime();
		printf("\n%lf\t%8d\t", currTime, Rate);
		for (int j = 0; j < numValuesPerChannel; j++) { 
			printf("\n");
		    	for(int i = 0; i < numActiveChannels; i++) {
				printf("\t\t%u\t", CounterData[0]);
				//printf("\t\t%u\t", CounterData[j*numActiveChannels + i]);
			}
		}
	}
    Options = CTR32BIT;

	fclose(testData);
	system("pause");
}
