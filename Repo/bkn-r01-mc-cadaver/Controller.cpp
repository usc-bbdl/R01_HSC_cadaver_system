#include "Controller.h"

Controller::Controller(LoadCellData *loadCellData, DCMotorCommand *dcMotorCommand)
{

	pLoadCellData = loadCellData;
	pDCMotorCommand = dcMotorCommand;

	hIOMutex = CreateMutex(NULL, FALSE, NULL);
	kill = 0;
	delayThread = 10;


	// CHANGE TO THE DESIRED NUMBER OF GROUPS TO CONTROL
	initControllerIndex = 0;
	numControllers = 5;


	motorSelection[0] = 1;
	motorSelection[1] = 2;
	motorSelection[2] = 3;
	motorSelection[3] = 4;
	motorSelection[4] = 5;
	motorSelection[5] = 0;
	motorSelection[6] = 0;
	motorSelection[7] = 0;

	loadCellSelection[0] = 0;
	loadCellSelection[1] = 2;
	loadCellSelection[2] = 4;
	loadCellSelection[3] = 5;
	loadCellSelection[4] = 6;
	loadCellSelection[5] = 0;
	loadCellSelection[6] = 0;
	loadCellSelection[7] = 0;

	bWindUp = false;
	bForceControlOn = false;
	maxForce = 15.0;	//Newtons
	for (int i = 0; i < 8; i++) {
		desiredReading[i] = 0.0;
		voltageValue[i] = 0.0;
		errorReading[i] = 0.0;
		kp[i] = 0.25;
	}
	kp[0] = 0.3;
	kp[1] = 0.3;
	kp[2] = 0.2;
	
	_beginthread(Controller::staticControllerCallback, 0, this);
}

Controller::~Controller(void)
{
	bForceControlOn = false;
}

int Controller::enableForceControl()
{
	bWindUp = false;
	bForceControlOn = true;
	return 0;
}

int Controller::enableWindUp()
{
	bWindUp = true;
	return 0;
}

// Updates control loop
// Inputs
//		loadCellReadings	Gets load cell values from the user (sensor)
// Outputs
//		voltageValues to the motors
// Internal
//		errorReading		Gets change from desired and load cell readings
//		desiredReading		Gets INITIALIZED desired reading from the Windup
int Controller::updateControlLoop(double *loadCellReadings, double *outputValues)
{
	// How can we add an easy selector to control output to different motors?
	// Each motor is independent of each other and has its own sensors
	if (bWindUp) {
		for (int i = initControllerIndex; i < numControllers; i++) { 
			desiredReading[i] = loadCellReadings[loadCellSelection[i]] + 0.05;
			voltageValue[i] = 0.4;
			*(outputValues + motorSelection[i]) = *(voltageValue + i);
		}

	}
	else if (bForceControlOn) {
		for (int i = initControllerIndex; i < numControllers; i++) { 

			//errorReading[i] = desiredReading[i] - *(loadCellReadings + loadCellSelection[i]);	

			errorReading[i] = desiredReading[i] - loadCellReadings[loadCellSelection[i]];	

			voltageValue[i] =  kp[i] * errorReading[i] + voltageValue[i];

			*(outputValues + motorSelection[i]) = *(voltageValue + i);
		}
	}
	return 0;
}

int Controller::updateDesiredReading(int index, double value)
{
	desiredReading[index] = value;
	return 0;
}

void Controller::controllerCallback(void)
{
	//if(has wound up ???
	// Force controller update loop
	while (!kill) {

		Sleep(delayThread); 
		WaitForSingleObject(hIOMutex, INFINITE);

		updateControlLoop((double*) pLoadCellData->outForceControllerValues, outputDCValues);
		pDCMotorCommand->SendVoltageArrayOut(outputDCValues);

		ReleaseMutex( hIOMutex);
	}

}

void Controller::staticControllerCallback(void* a) {
	((Controller*)a)->controllerCallback();
}