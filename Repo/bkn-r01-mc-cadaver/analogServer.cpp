#include "analogServer.h"


analogServer::analogServer(LoadCellData *loadCellData)
{
	pLoadCellData = loadCellData;
	bReceivedPPP = false;
	bReceivedKKK = false;
	bReceivedTTT = false;
	bReceivedRRR = false;
	bReceivedName = false;
	messageIdle = false;
	sprintf_s(
		sNameOfDataFile, 
		"testFile.txt"
		);
	voltageValue = 0;
	
	delayThread = 10;
	hIOMutex = CreateMutex(NULL, FALSE, NULL);
	kill = 0;
	_beginthread(analogServer::staticanalogServerCallback, 0, this);
	//voltageValue = pLoadCellData->outForceControllerValues[7];
}


analogServer::~analogServer(void)
{
	bReceivedPPP = false;
	bReceivedKKK = false;
	bReceivedTTT = false;
	bReceivedRRR = false;
	bReceivedName = false;

	kill = 1;
}

void analogServer::staticanalogServerCallback(void *a)
{
	((analogServer *) a)->analogServerCallback();
}

void analogServer::analogServerCallback(void)
{
	while (!kill) {

		Sleep(delayThread); 
		WaitForSingleObject(hIOMutex, INFINITE);
		bool wasNotConnected = false,wasKKK = false, wasPPP = false, wasRRR= false, wasTTT = false;

		// Query data for this frame
		voltageValue = pLoadCellData->outForceControllerValues[7];
		if ((voltageValue<10)&&(!wasNotConnected)){
				messageIdle = false;
				bReceivedPPP = false;
				bReceivedKKK = false;
				bReceivedTTT = false;
				bReceivedRRR = false;
				bReceivedName = false;
				bNotConnected = true;
				wasNotConnected = true;
				wasKKK = false;
				wasPPP = false;
				wasTTT = false;
				wasRRR = false;
		}else if ((voltageValue>15)&&(voltageValue<30)&&(!wasKKK)){
				messageIdle = false;
				bReceivedPPP = false;
				bReceivedKKK = true;
				bReceivedTTT = false;
				bReceivedRRR = false;
				bReceivedName = true;
				wasNotConnected = false;
				wasKKK = true;
				wasPPP = false;
				wasTTT = false;
				wasRRR = false;

		}else if ((voltageValue>30)&&(voltageValue<40)&&(!wasPPP)){
				messageIdle = false;	
				bReceivedPPP = true;
				bReceivedKKK = false;
				bReceivedTTT = false;
				bReceivedRRR = false;
				bReceivedName = false;
				wasNotConnected = false;
				wasKKK = false;
				wasPPP = true;
				wasTTT = false;
				wasRRR = false;
		}else if ((voltageValue>42)&&(voltageValue<50)&&(!messageIdle)){
				messageIdle = true;
				bReceivedPPP = false;
				bReceivedKKK = false;
				bReceivedTTT = false;
				bReceivedRRR = false;
				bReceivedName = false;
				wasNotConnected = false;
				wasKKK = false;
				wasPPP = false;
				wasTTT = false;
				wasRRR = false;
		}else if((voltageValue>52)&&(voltageValue<60)&&(!wasRRR)){
				messageIdle = false;
				bReceivedPPP = false;
				bReceivedKKK = false;
				bReceivedTTT = false;
				bReceivedRRR = true;
				bReceivedName = false;
				wasNotConnected = false;
				wasKKK = false;
				wasPPP = false;
				wasTTT = false;
				wasRRR = true;
		}else if((voltageValue>65)&&(voltageValue<75)&&(!wasTTT)){
				messageIdle = false;
				bReceivedPPP = false;
				bReceivedKKK = false;
				bReceivedTTT = true;
				bReceivedRRR = false;
				bReceivedName = false;
				wasNotConnected = false;
				wasKKK = false;
				wasPPP = false;
				wasTTT = true;
				wasRRR = false;
		}
		ReleaseMutex( hIOMutex);
	}
		
} 
