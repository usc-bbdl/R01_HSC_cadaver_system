#pragma once

#include <windows.h>
#include <process.h>
#include "LoadCellData.h"
#include "DCMotorCommand.h"
//#include <stdio.h>

class Controller
{
	// This should allow us to change the configuration
	// without having to mess with hardware for now
	// Consider making all this const int
	int numControllers;
	int motorSelection[8];
	int loadCellSelection[8];
	double outputDCValues[8];

	int kill;
	HANDLE hIOMutex;	
	DWORD delayThread;

	LoadCellData *pLoadCellData;
	DCMotorCommand *pDCMotorCommand;

	int initControllerIndex;

public:
	bool bForceControlOn;
	bool bWindUp;
	double maxForce;	
	double voltageValue[8];
	double desiredReading[8];
	double errorReading[8];
	double kp[8];
	Controller(LoadCellData*, DCMotorCommand*);
	~Controller(void);
	int enableForceControl();
	int enableWindUp();
	int updateControlLoop(double *, double *);
	int updateDesiredReading(int, double);

	static void staticControllerCallback(void*);
    void controllerCallback(void);
};

