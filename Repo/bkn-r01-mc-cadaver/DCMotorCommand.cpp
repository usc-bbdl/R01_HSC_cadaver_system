#include "DCMotorCommand.h"

DCMotorCommand::DCMotorCommand(void)
{
	numMotors = 7;
	BoardNumVoltage = 0;
	Options = DEFAULTOPTION;
	voltageGain = UNI10VOLTS;
	minVoltage = 0.0;
	maxVoltage = 2.0;
	
	// Initializing VoltageOut modules
	for(int i = 0; i < numMotors; i++) {
		cbVOut(BoardNumVoltage, 2 * i, voltageGain, 0, Options);
	}

	// Configuring Digital Outputs
	cbDConfigPort(BoardNumVoltage, 1, DIGITALOUT);
	cbDOut(BoardNumVoltage, 1, 0);

}

DCMotorCommand::~DCMotorCommand(void)
{
	for(int i = 0; i < numMotors; i++) {
		cbVOut(BoardNumVoltage, 2 * i, voltageGain, 0, Options);
	}

	cbDOut(BoardNumVoltage, 1, 0);

}

int DCMotorCommand::SendVoltageArrayOut(double *voltages)
{
	for(int i = 0; i < numMotors; i++) {
		if(*(voltages + i) >= minVoltage && *(voltages + i) <= maxVoltage) {
			cbVOut(BoardNumVoltage, 2 * i, voltageGain, *(voltages + i), Options);
		}
	}
	return 0;
}

int DCMotorCommand::SendVoltageOut(int index, double voltage)
{
	if(voltage >= minVoltage && voltage <= maxVoltage) {
		//cbVOut(BoardNumVoltage, 2 * index, voltageGain, voltage, Options);
		motorVoltages[index] = voltage;
	}
	SendVoltageArrayOut(motorVoltages);

	return 0;
}


int DCMotorCommand::TurnAmplifiersOn()
{
	cbDOut(BoardNumVoltage, 1, 255);
	return 0;
}

int DCMotorCommand::TurnAmplifiersOff()
{
	for (int i = 0; i < numMotors; i++) {
		*(motorVoltages + i) = 0;
	}
	SendVoltageArrayOut(motorVoltages);
	cbDOut(BoardNumVoltage, 1, 0);
	return 0;
}

/*int DCMotorCommand::WindUpMotors()
{
	for (int i = 0; i < numMotors; i++) {
		*(motorVoltages + i) = 0.4;
	}
	SendVoltageArrayOut(motorVoltages);

	return 0;
}

int DCMotorCommand::SetVoltages()
{
	SendVoltageArrayOut(motorVoltages);
	return 0;
}*/

