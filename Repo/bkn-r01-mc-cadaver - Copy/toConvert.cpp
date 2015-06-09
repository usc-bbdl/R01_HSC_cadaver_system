// MCDAQ
// Board 0:	Encoder Reader - QUAD08

// FLAGS For now use one or the other
//#define USING_ENCODERS	//First
#define USING_VOLTAGEOUT

#include <windows.h>
#include <stdio.h>
#include <conio.h>
#include "phidget/phidget21.h"
#include "include/cbw.h"
#pragma comment(lib, "lib/cbw32.lib")
#pragma comment(lib, "phidget/phidget21.lib")

#define minVoltage 0.0f
#define maxVoltage 2.0f	// Volts

#define maxForce 15.0f	//Newtons

double load_cell_reading[5];

FILE *fp;

LARGE_INTEGER	gInitTick, gCurrentTick, gClkFrequency;

int CCONV AttachHandlerBridge1(CPhidgetHandle phid, void *userptr)
{
	CPhidgetBridgeHandle bridge = (CPhidgetBridgeHandle)phid;

	CPhidgetBridge_setEnabled(bridge, 0, PTRUE);
	CPhidgetBridge_setEnabled(bridge, 1, PTRUE);
	CPhidgetBridge_setEnabled(bridge, 2, PTRUE);
	CPhidgetBridge_setEnabled(bridge, 3, PTRUE);

	CPhidgetBridge_setGain(bridge, 0, PHIDGET_BRIDGE_GAIN_128);
	CPhidgetBridge_setGain(bridge, 1, PHIDGET_BRIDGE_GAIN_128);
	CPhidgetBridge_setGain(bridge, 2, PHIDGET_BRIDGE_GAIN_128);
	CPhidgetBridge_setGain(bridge, 3, PHIDGET_BRIDGE_GAIN_128);
	CPhidgetBridge_setDataRate(bridge, 10);

	return 0;
}

int CCONV AttachHandlerBridge2(CPhidgetHandle phid, void *userptr)
{
	CPhidgetBridgeHandle bridge = (CPhidgetBridgeHandle)phid;

	CPhidgetBridge_setEnabled(bridge, 0, PTRUE);
	CPhidgetBridge_setEnabled(bridge, 1, PFALSE);
	CPhidgetBridge_setEnabled(bridge, 2, PFALSE);
	CPhidgetBridge_setEnabled(bridge, 3, PFALSE);

	CPhidgetBridge_setGain(bridge, 0, PHIDGET_BRIDGE_GAIN_128);

	CPhidgetBridge_setDataRate(bridge, 10);

	return 0;
}

int CCONV data_bridge1(CPhidgetBridgeHandle phid, void *userPtr, int index, double val)
{
	CPhidgetBridgeHandle bridge = (CPhidgetBridgeHandle)phid;
	double f, ms;
	int i;

	load_cell_reading[index] = val;
	return 0;
}

int CCONV data_bridge2(CPhidgetBridgeHandle phid, void *userPtr, int index, double val)
{
	CPhidgetBridgeHandle bridge = (CPhidgetBridgeHandle)phid;
	double f, ms;
	int i;

	load_cell_reading[index + 4] = val;
	return 0;
}

void main ()
{
	QueryPerformanceCounter(&gInitTick);
	QueryPerformanceFrequency(&gClkFrequency);
	
#ifdef USING_ENCODERS
	int BoardNumEncoders = 1;
	int ULStatEncoders = NOERRORS;
	int Mode,DebounceTime, DebounceMode, EdgeDetection;
	
	Mode = ENCODER | ENCODER_MODE_X4 | CLEAR_ON_Z_OFF;
	DebounceTime = CTR_DEBOUNCE_NONE;
	DebounceMode = 0;
	EdgeDetection = CTR_RISING_EDGE;
#endif

#ifdef USING_VOLTAGEOUT
	int BoardNumVoltage = 0;
	int ULStatVoltage = NOERRORS;
#endif
	//cbErrHandling (PRINTALL, DONTSTOP);

#ifdef USING_ENCODERS
	// INITIALIZE ENCODERS
fprintf(fileConsole,  ("\n\nInitializing Encoders...");
	+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
	for(int i = 0; i < 8; i++)
	{
		ULStatEncoders = cbCConfigScan(BoardNumEncoders, i, Mode, DebounceTime, DebounceMode, EdgeDetection, 0, 0);
		if(ULStatEncoders == NOERRORS)
		{
fprintf(fileConsole,  ("\nInitialized Encoder %01d successfully", i);
		}
	}
fprintf(fileConsole,  ("\n\nInitialized Encoders successfully");
	getch();
#endif

#ifdef USING_VOLTAGEOUT

	//Phidget Bridge
	
	CPhidgetBridgeHandle bridge1;
	CPhidgetBridgeHandle bridge2;

	CPhidgetBridge_create(&bridge1);
	CPhidgetBridge_create(&bridge2);

	CPhidget_set_OnAttach_Handler((CPhidgetHandle)bridge1, AttachHandlerBridge1,NULL);
	CPhidget_set_OnAttach_Handler((CPhidgetHandle)bridge2, AttachHandlerBridge2,NULL);
	
	CPhidgetBridge_set_OnBridgeData_Handler(bridge1, data_bridge1, NULL);
	CPhidgetBridge_set_OnBridgeData_Handler(bridge2, data_bridge2, NULL);

	CPhidget_open((CPhidgetHandle)bridge1, 293182);
	CPhidget_open((CPhidgetHandle)bridge2, 341581);

fprintf(fileConsole, ("\n\nInitialized Load Cells succesfully");

	//End Phidget Bridge

	// INITIALIZE VOUT
	int voltageGain = UNI10VOLTS;

	double slope2 = 49.002;
	double slope4 = 49.002;
	double slope6 = 49.002;
	double slope8 = 49.002;   
	double slope10 = 49.002;
	double slope12 = 49.002;

	double yCrossing2;
	double yCrossing4;
	double yCrossing6;
	double yCrossing8;
	double yCrossing10;
	double yCrossing12;

	double initial_load_cell_reading2;
	double initial_load_cell_reading4;
	double initial_load_cell_reading6;
	double initial_load_cell_reading8;
	double initial_load_cell_reading10;
	double initial_load_cell_reading12;
	
	double actual_Force2;
	double actual_Force4;
	double actual_Force6;
	double actual_Force8;
	double actual_Force10;
	double actual_Force12;

	double desired_Reading2 = 0.20f;
	double desired_Reading4 = 0.20f;
	double desired_Reading6 = 0.20f;
	double desired_Reading8 = 0.20f;
	double desired_Reading10 = 0.20f;
	double desired_Reading12 = 0.20f;

	double error_Reading2 = 0.0f;
	double error_Reading4 = 0.0f;
	double error_Reading6 = 0.0f;
	double error_Reading8 = 0.0f;
	double error_Reading10 = 0.0f;
	double error_Reading12 = 0.0f;

	double kp2 = 1.00f;
	double kp4 = 1.00f;
	double kp6 = 1.00f;
	double kp8 = 1.00f;
	double kp10 = 1.00f;
	double kp12 = 1.00f;

	double voltageValue4 = 0.0f;
	double voltageValue6 = 0.0f;
	double voltageValue2 = 0.0f;
	double voltageValue8 = 0.0f;
	double voltageValue10 = 0.0f;
	double voltageValue12 = 0.0f;

	//double voltageValue8 = 0.0f;
	int Options = DEFAULTOPTION;
	int UDStat = NOERRORS;
fprintf(fileConsole,  ("\n\nInitializing VoltageOut modules...");
	{
		//cbVOut(BoardNumVoltage, 2, voltageGain, voltageValue2, Options);
		cbVOut(BoardNumVoltage, 4, voltageGain, voltageValue4, Options);
		cbVOut(BoardNumVoltage, 6, voltageGain, voltageValue6, Options);
		cbVOut(BoardNumVoltage, 2, voltageGain, voltageValue2, Options);
		cbVOut(BoardNumVoltage, 8, voltageGain, voltageValue8, Options);
		cbVOut(BoardNumVoltage, 10, voltageGain, voltageValue10, Options);
		cbVOut(BoardNumVoltage, 12, voltageGain, voltageValue12, Options);
		//cbVOut(BoardNumVoltage, 8, voltageGain, voltageValue8, Options);
		//printf ("\nInitialized VoltageOut module %01d successfully", i);
	}
fprintf(fileConsole,  ("\n\nInitialized VoltageOut modules successfully");

	//cbDConfigPort(BoardNumVoltage, 2, DIGITALOUT);
	cbDConfigPort(BoardNumVoltage, 1, DIGITALOUT);
	cbDOut(BoardNumVoltage, 1, 0);
	
	getch();


#endif

	// REAL-TIME
	unsigned short countedVal[8];
	bool bExitFlag = false;
	bool forceControlOn = false;
	bool windUp = false;
	bool writingFile = false;

	initial_load_cell_reading2 =  load_cell_reading[0];
	initial_load_cell_reading4 =  load_cell_reading[1];
	initial_load_cell_reading6 =  load_cell_reading[2];
	initial_load_cell_reading8 =  load_cell_reading[3];
	initial_load_cell_reading10 =  load_cell_reading[4];
	initial_load_cell_reading12 =  0;

	desired_Reading2 = initial_load_cell_reading2;
	desired_Reading4 = initial_load_cell_reading4;
	desired_Reading6 = initial_load_cell_reading6;
	desired_Reading8 = initial_load_cell_reading8;
	desired_Reading10 = initial_load_cell_reading10;
	desired_Reading12 = initial_load_cell_reading12;

	yCrossing2 = -slope2*initial_load_cell_reading2;
	yCrossing4 = -slope4*initial_load_cell_reading4;
	yCrossing6 = -slope6*initial_load_cell_reading6;
	yCrossing8 = -slope8*initial_load_cell_reading8;
	yCrossing10 = -slope10*initial_load_cell_reading10;
	yCrossing12 = -slope12*initial_load_cell_reading12;

	while (!bExitFlag)
	{
		if(GetAsyncKeyState(VK_ESCAPE))
		{
			bExitFlag = true;
		}

#ifdef USING_VOLTAGEOUT

		if(GetAsyncKeyState(VK_UP))
		{
			//voltageValue2 = 5.0f;
			//+++ Change the name of vars
			cbDOut(BoardNumVoltage, 1, 255);//cbDOut(BoardNumVoltage, 1, 255);
			windUp = true;
			//cbVOut (BoardNumVoltage, 2, voltageGain, voltageValue2, Options);
		}
		else if(GetAsyncKeyState(VK_DOWN))
		{
			//voltageValue2 = 0.0f;
			cbDOut(BoardNumVoltage, 1, 0);
			windUp = false;
			forceControlOn = false;
			//cbVOut (BoardNumVoltage, 2, voltageGain, voltageValue2, Options);
		}
		else if(GetAsyncKeyState('Z'))
		{
			if(windUp && !forceControlOn)
			{
				windUp = false;
				forceControlOn = true;
			}
		}
		else if(GetAsyncKeyState('X'))
		{
			writingFile = true;
			fp = fopen("test.txt","w");

			if(fp==NULL)
			{
				fprintf(stderr, "Can't open output file test.txt\n");
			}
		}
		else if(GetAsyncKeyState('Q') && desired_Reading2 <= maxForce - 0.001)
		{
			//voltageValue12 += 0.001; 
			desired_Reading2 += 0.001;
		}
		else if(GetAsyncKeyState('A') && desired_Reading2 >= initial_load_cell_reading2 + 0.001)
		{
			//voltageValue12 -= 0.001; 
			desired_Reading2 -= 0.001;
		}
		if(GetAsyncKeyState('W') && desired_Reading4 <= maxForce - 0.001 )
		{
			//voltageValue10 += 0.001; 
			desired_Reading4 += 0.001;
		}
		else if(GetAsyncKeyState('S') && desired_Reading4 >= initial_load_cell_reading4 + 0.001)
		{
			//voltageValue10 -= 0.001; 
			desired_Reading4 -= 0.001;
		}
		
		if(GetAsyncKeyState('E') && desired_Reading6 <= maxForce - 0.001 )
		{
			//voltageValue8 += 0.001; 
			desired_Reading6 += 0.001;
		}
		else if(GetAsyncKeyState('D') && desired_Reading6 >= initial_load_cell_reading6 + 0.001)
		{
			//voltageValue8 -= 0.001; 
			desired_Reading6 -= 0.001;
		}

		if(GetAsyncKeyState('R') && desired_Reading8 <= maxForce - 0.001 )
		{
			//voltageValue6 += 0.001; 
			desired_Reading8 += 0.001;
		}
		else if(GetAsyncKeyState('F') && desired_Reading8 >= initial_load_cell_reading8 + 0.001)
		{
			//voltageValue6 -= 0.001; 
			desired_Reading8 -= 0.001;
		}
		
		if(GetAsyncKeyState('T') && desired_Reading10 <= maxForce - 0.001 )
		{
			//voltageValue10 += 0.001; 
			desired_Reading10 += 0.001;
		}
		else if(GetAsyncKeyState('G') && desired_Reading10 >= initial_load_cell_reading10 + 0.001)
		{
			//voltageValue4 -= 0.001; 
			desired_Reading10 -= 0.001;
		}

		if(GetAsyncKeyState('Y') && desired_Reading12 <= maxForce - 0.001 )
		{
			//voltageValue2 += 0.001; 
			desired_Reading12 += 0.001;
		}
		else if(GetAsyncKeyState('H') && desired_Reading12 >= initial_load_cell_reading12 + 0.001)
		{
			//voltageValue2 -= 0.001; 
			desired_Reading12 -= 0.001;
		}
#endif

#ifdef USING_ENCODERS
		
		if(ULStatEncoders == NOERRORS)
		{
			for(int i = 0; i < 8; i++)
			{
				ULStatEncoders = cbCIn(BoardNumEncoders, i,  &countedVal[i]);
			}
		}
		else
		{
fprintf(fileConsole,  ("\n\n ERROR IN ULStatEncoders!");
			break;
		}

#endif

#ifdef USING_VOLTAGEOUT

		if(GetAsyncKeyState(VK_SPACE))
		{
			voltageValue4 = 0.0f;
			voltageValue6 = 0.0f;
			voltageValue2 = 0.0f;
			voltageValue8 = 0.0f;
			voltageValue10 = 0.0f;
			voltageValue12 = 0.0f;
		}
		
		error_Reading2 = desired_Reading2 - load_cell_reading[0];	
		error_Reading4 = desired_Reading4 - load_cell_reading[1];
		error_Reading6 = desired_Reading6 - load_cell_reading[2];
		error_Reading8 = desired_Reading8 - load_cell_reading[3];
		error_Reading10 = desired_Reading10 - load_cell_reading[4];
		//error_Force12 = desired_Force12 - load_cell_reading[0];

		if(forceControlOn)
		{
			voltageValue2 =  kp2*error_Reading2 + voltageValue2;
			//voltageValue4 =  kp2*error_Force4 + voltageValue4;
			voltageValue6 =  kp6*error_Reading6 + voltageValue6;
			//voltageValue8 =  kp2*error_Force8 + voltageValue8;
			//voltageValue10 =  kp10*error_Reading10 + voltageValue10;
		}

		// LIMIT CORRECTION AND OUTPUT

		if (voltageValue8 + 0.4 <= maxVoltage && voltageValue8 >= minVoltage)
		{
			cbVOut (BoardNumVoltage, 8, voltageGain, 0, Options);
		}

		if (voltageValue10 <= maxVoltage && voltageValue10 >= minVoltage)
		{
			cbVOut (BoardNumVoltage, 10, voltageGain, 0, Options);
		}

		if (voltageValue12 <= maxVoltage && voltageValue12 >= minVoltage)
		{
			cbVOut (BoardNumVoltage, 12, voltageGain, 0, Options);
		}

		if (voltageValue6 <= maxVoltage && voltageValue6 >= minVoltage)
		{
			cbVOut (BoardNumVoltage, 6 , voltageGain, voltageValue6 + 0.4, Options);
		}

		if (voltageValue4 <= maxVoltage && voltageValue4 >= minVoltage)
		{
			cbVOut (BoardNumVoltage, 4, voltageGain, 0 , Options);
		}

		if (voltageValue2 + 0.4 <= maxVoltage && voltageValue2 >= minVoltage)
		{
			cbVOut (BoardNumVoltage, 2, voltageGain, voltageValue2 + 0.4, Options);
		}

#endif

#ifdef USING_ENCODERS 
		// Print Output
fprintf(fileConsole,  ("\n Count:");
		for(int i = 0; i < 8; i++)
		{
			ULStatEncoders = cbCConfigScan(BoardNumEncoders, i, Mode, DebounceTime, DebounceMode, EdgeDetection, 0, 0);
			if(ULStatEncoders == NOERRORS)
			{
fprintf(fileConsole,  ("\t%05u", countedVal[i]);
			}
		}

#endif
		actual_Force2 = slope2*load_cell_reading[0] + yCrossing2;
		actual_Force4 = slope4*load_cell_reading[1] + yCrossing4;
		actual_Force6 = slope6*load_cell_reading[2] + yCrossing6;
		actual_Force8 = slope8*load_cell_reading[3] + yCrossing8;
		actual_Force10 = slope10*load_cell_reading[4] + yCrossing10;


#ifdef USING_VOLTAGEOUT
		// Approximately 100 Hz Recording
		double actualTime;
		QueryPerformanceCounter(&gCurrentTick);
		actualTime = gCurrentTick.QuadPart - gInitTick.QuadPart;
		actualTime /= gClkFrequency.QuadPart;
		

fprintf(fileConsole, ("\nTime %.3lf",actualTime );
	
fprintf(fileConsole,  ("\nDesired\t%01.2f\t%01.2f\t%01.2f\t%01.2f\t%01.2f\t%01.2f", desired_Reading2/*desired_Reading2*slope2+yCrossing2*/, desired_Reading4, desired_Reading6, desired_Reading8, desired_Reading10);
fprintf(fileConsole,  ("\nV\t%01.2f\t%01.2f\t%01.2f\t%01.2f\t%01.2f\t%01.2f", voltageValue2, voltageValue4, voltageValue6, voltageValue8, voltageValue10);
fprintf(fileConsole,  ("\nBridge\t%01.2f\t%01.2f\t%01.2f\t%01.2f\t%01.2f\t%01.2f", load_cell_reading[0], actual_Force4,load_cell_reading[2],actual_Force8,actual_Force10);
		//printf ("\nError\t%01.2f\t%01.2f\t%01.2f\t%01.2f\t%01.2f\t%01.2f", error_Reading2*slope2, error_Reading4*slope4, error_Reading6*slope6, error_Reading8*slope8, error_Reading10*slope10);
		if(writingFile)
		{
			fprintf(fp,"%.3lf\t%01.2f\t%01.2f\t%01.2f\t%01.2f\t%01.2f\t%01.2f\n", actualTime, load_cell_reading[0], actual_Force4,load_cell_reading[2],actual_Force8,actual_Force10);
		}
#endif
	}

	// Wrap it up

	voltageValue4 = 0.0f;
	voltageValue6 = 0.0f;
	voltageValue2 = 0.0f;
	voltageValue8 = 0.0f;
	voltageValue10 = 0.0f;
	voltageValue12 = 0.0f;

	if (voltageValue6 <= maxVoltage && voltageValue6 >= minVoltage)
	{
		cbVOut (BoardNumVoltage, 6, voltageGain, voltageValue6, Options);
	}

	if (voltageValue4 <= maxVoltage && voltageValue4 >= minVoltage)
	{
		cbVOut (BoardNumVoltage, 4, voltageGain, voltageValue4, Options);
	}

	if (voltageValue2 <= maxVoltage && voltageValue2 >= minVoltage)
	{
		cbVOut (BoardNumVoltage, 2, voltageGain, voltageValue2, Options);
	}

	if (voltageValue8 <= maxVoltage && voltageValue8 >= minVoltage)
	{
		cbVOut (BoardNumVoltage, 8, voltageGain, voltageValue8, Options);
	}

	if (voltageValue10 <= maxVoltage && voltageValue10 >= minVoltage)
	{
		cbVOut (BoardNumVoltage, 10, voltageGain, voltageValue10, Options);
	}

	if (voltageValue12 <= maxVoltage && voltageValue12 >= minVoltage)
	{
		cbVOut (BoardNumVoltage, 12, voltageGain, voltageValue12, Options);
	}


	cbDOut(BoardNumVoltage, 1, 0);

fprintf(fileConsole,  ("\n\n Stopping Wheatstone bridge");

	CPhidget_close((CPhidgetHandle)bridge1);
	CPhidget_close((CPhidgetHandle)bridge2);
	CPhidget_delete((CPhidgetHandle)bridge1);
	CPhidget_delete((CPhidgetHandle)bridge2);
	
	if(writingFile)
	{
		fclose(fp);
	}

fprintf(fileConsole,  ("\n\n Closing program");


	getch();
}
