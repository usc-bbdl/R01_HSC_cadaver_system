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
	//numControllers = 5;
	numControllers = 8;

	for (int i=0;i<numControllers;i++)
	{
		loadCellSelection[i] = i;
	}
	motorSelection[0] = 1;
	motorSelection[1] = 0;
	motorSelection[2] = 2;
	motorSelection[3] = 0;
	motorSelection[4] = 3;
	motorSelection[5] = 4;
	motorSelection[6] = 5;

	controllerOnFlag[0] = false;
	controllerOnFlag[1] = false;
	controllerOnFlag[2] = true;
	controllerOnFlag[3] = false;
	controllerOnFlag[4] = true;
	controllerOnFlag[5] = false;
	controllerOnFlag[6] = false;
	controllerOnFlag[7] = false;

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
	//kian starts here
	bForceControlOn = false;
	//kian ends here
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
			if (controllerOnFlag[i])
			{
				desiredReading[i] = loadCellReadings[i] + 0.05;
				voltageValue[i] = 0.4;
				*(outputValues + motorSelection[i]) = *(voltageValue + i);
			}
		}
	}
	else if (bForceControlOn) {
		for (int i = initControllerIndex; i < numControllers; i++) 
		{
			if (controllerOnFlag[i])
			{
				//errorReading[i] = desiredReading[i] - *(loadCellReadings + loadCellSelection[i]);	 
				errorReading[i] = desiredReading[i] - loadCellReadings[i];
				voltageValue[i] =  kp[i] * errorReading[i] + voltageValue[i];
				*(outputValues + motorSelection[i]) = *(voltageValue + i);
			}
		}
	}//Kian: if both force control and windup are false, set voltage to 0.
	else{
				for (int i = initControllerIndex; i < numControllers; i++) { 
					voltageValue[i] = 0;

					*(outputValues + motorSelection[i]) = *(voltageValue+i);
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