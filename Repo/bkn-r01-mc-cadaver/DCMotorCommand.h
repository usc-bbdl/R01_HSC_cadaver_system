#pragma once
#include "include/cbw.h"

#ifdef WIN_64
#	pragma comment(lib, "lib/x64/cbw64.lib")
#else
#	pragma comment(lib, "lib/x86/cbw32.lib")
#endif

class DCMotorCommand
{
	int voltageGain;
	int numMotors;
	double minVoltage;	// Volts
	double maxVoltage;	// Volts
	int Options;
	int BoardNumVoltage;


public:

	// Use a binary number to indicate which out of the 8 maximum motors
	// are enabled for the controller
	// In this case we have motors 1 and 3 so the number would be 
	// b'00001010'
	// or for our case a mask of value 10
	// Send this number to the controller

	DCMotorCommand(void);
	~DCMotorCommand(void);
	int SendVoltageArrayOut(double *);
	double motorVoltages[8];
	int SendVoltageOut(int, double);
	int TurnAmplifiersOn();
	int TurnAmplifiersOff();
	int WindUpMotors();
	int SetVoltages();
};

