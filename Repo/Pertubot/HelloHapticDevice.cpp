#ifdef  _WIN64
#pragma warning (disable:4996)
#endif

#include <iostream>
#include <stdio.h>
#include "UdpServer.h"
#if defined(WIN32)
# include <windows.h>
# include <conio.h>
#else
# include "conio.h"
# include <string.h>
#endif

#include <HD/hd.h>
#include <HDU/hduError.h>
#include <HDU/hduVector.h>
#include <windows.h>
#include <time.h>
#include "TimeData.h"
#include "DataLogger.h"

using namespace std;

TimeData gTimeData;
DataLogger gDataLogger = DataLogger(
				10, 
				"C:\\data\\%s_phantom",
				"time,angx,angy,angz,torx,tory,torz\n"
			);	

UdpServer gUdpServer = UdpServer();

bool bIsPerturbing = false;

char dataString[200];

const double MAX_FORCE = 8.0;

int count;
const HDdouble kStylusTorqueConstant = 400.0;	//3.14*40.0; /* radians */

int recording;
int kill;

void mainLoop(void);

HANDLE    hIOMutex; //= CreateMutex (NULL, FALSE, NULL);	

hduVector3Dd global_position;
hduVector3Dd globalOutputTorque;
hduVector3Dd global_joint_angles;
hduVector3Dd global_joint_torque;

hduVector3Dd global_desired_position;
hduVector3Dd global_desired_angle;
hduVector3Dd globalInputForce;


char gTimeStamp[120];
hduVector3Dd jointTorqueCommand;

HDCallbackCode HDCALLBACK gravityWellCallback(void *data);

bool                    gResetSim=false,gIsRecording=false, gResetGlobal=false;
LARGE_INTEGER           gInitTick, gCurrentTick, gClkFrequency;
FILE                    *gDataFile, *gConfigFile;


/*******************************************************************************
Main function.
Initializes the device, starts the schedule, creates a schedule callback
to handle gravity well forces, waits for the user to press a button, exits
the application.
*******************************************************************************/

inline void LogData( void)
{   
	// Approximately 100 Hz Recording
	double actualTime;
	QueryPerformanceCounter(&gCurrentTick);
	actualTime = gCurrentTick.QuadPart - gInitTick.QuadPart;
	actualTime /= gClkFrequency.QuadPart;
	if (gIsRecording)
	{   
		fprintf(gDataFile,"%.3lf\t",actualTime );

		fprintf(gDataFile,"%f\t%f\t%f\t", globalOutputTorque[0], globalOutputTorque[1], globalOutputTorque[2]);
		fprintf(gDataFile,"\n");
	}
}



void InitProgram()
{
	time_t rawtime;
	struct tm *timeinfo;
	time(&rawtime);
	timeinfo = localtime(&rawtime);
}

double sumZReal = 1.82;


class CTimer {
public:
	CTimer() {
		reset();
	}
	/// reset() makes the timer start over counting from 0.0 seconds.
	void reset() {
		unsigned __int64 pf;
		QueryPerformanceFrequency( (LARGE_INTEGER *)&pf );
		freq_ = 1.0 / (double)pf;
		QueryPerformanceCounter( (LARGE_INTEGER *)&baseTime_ );
	}
	/// seconds() returns the number of seconds (to very high resolution)
	/// elapsed since the timer was last created or reset().
	double seconds() {
		unsigned __int64 val;
		QueryPerformanceCounter( (LARGE_INTEGER *)&val );
		return (val - baseTime_) * freq_;
	}
	/// seconds() returns the number of milliseconds (to very high resolution)
	/// elapsed since the timer was last created or reset().
	double milliseconds() {
		return seconds() * 1000.0;
	}
private:
	double freq_;
	unsigned __int64 baseTime_;
};


int main(int argc, char* argv[])
{    
	HDErrorInfo error;
	HDSchedulerHandle hGravityWell;

	/* Initialize the device, must be done before attempting to call any hd 
	functions. Passing in HD_DEFAULT_DEVICE causes the default device to be 
	initialized. */
	//HDstring deviceP1= "PREMIUM"; //Case sensitive careful!
	HHD hHD = hdInitDevice(NULL);

	InitProgram();

	sumZReal = 1.82;

	QueryPerformanceCounter(&gInitTick);
	QueryPerformanceFrequency(&gClkFrequency);


	if (HD_DEVICE_ERROR(error = hdGetError())) 
	{
		hduPrintError(stderr, &error, "Failed to initialize haptic device");
		fprintf(stderr, "\nPress any key to quit.\n");
		getch();
		return -1;
	}

	printf("Hello Haptic Device!\n");
	printf("Found device model: %s.\n\n", hdGetString(HD_DEVICE_MODEL_TYPE));

	/* Schedule the main callback that will render forces to the device. */
	hGravityWell = hdScheduleAsynchronous(
		gravityWellCallback, 0, 
		HD_MAX_SCHEDULER_PRIORITY);

	hdEnable(HD_FORCE_OUTPUT);

	hdStartScheduler();
	//_beginthread( recordingLoop ,0, NULL);
	/* Check for errors and abort if so. */
	if (HD_DEVICE_ERROR(error = hdGetError()))
	{
		hduPrintError(stderr, &error, "Failed to start scheduler");
		fprintf(stderr, "\nPress any key to quit.\n");
		return -1;
	}

	/* Wait until the user presses a key.  Meanwhile, the scheduler
	runs and applies forces to the device. */
	printf("Press R to record data\n");
	printf("Press Q to quit.\n\n");

	count = 0;

	globalInputForce[2] = 0.0;
	globalInputForce[1] = 0.0;

	//Sleep(3000);
	//Turn recording on
	//perturbationOn = true;

	double addForce = 2.0;
	double tMJ = 0.0;
	int startPert = 0;
	double tMJInit;
	double tDuration;
	double tMult3;
	double torI;
	double torF;
	global_desired_angle[1] = 0.0;
	global_desired_angle[2] = 0.0;
	// int eventPerturbationCounter = 0;
	do
	{
		// The robot can receive N R P T, normally in that order
		// If the robot receives TER command reset to the initial state of the 
		// perturbot
		if(gUdpServer.bReceivedName) {
			gDataLogger.setFileName(gUdpServer.sNameOfDataFile);
			gUdpServer.bReceivedName = false;
		}
		if(gUdpServer.bReceivedRRR) {
			gTimeData.resetTimer();
			gDataLogger.startRecording();
			gUdpServer.bReceivedRRR = false;
		}
		if(gUdpServer.bReceivedPPP) {
			bIsPerturbing = true;
			gUdpServer.bReceivedPPP = false;
		}
		if(gUdpServer.bReceivedTTT) {
			bIsPerturbing = false;
			startPert = 0;
			gDataLogger.closeRecordingFile();
			gUdpServer.bReceivedTTT = false;
		}


		// Give a square waveq
		if (bIsPerturbing) {
			// No delay for perturbation
			tMJ = gCurrentTick.QuadPart - gInitTick.QuadPart;
			QueryPerformanceCounter(&gCurrentTick);
			tMJ = gCurrentTick.QuadPart - gInitTick.QuadPart;
			tMJ /= gClkFrequency.QuadPart;

			if (0 == startPert) {
				startPert++;
				tMJInit = tMJ;
			}

			tMJ -= tMJInit;

			torI = 0.0;
			torF = -168.0*24.0;
			tDuration = 0.10;
			double tNorm = tMJ/tDuration;
			double highTIme = 2.2*0.45*0.30; 
			double lowTIme = 3.0; // Changing to a ridiculously high time?
			tMult3 = tNorm * tNorm * tNorm;

			if (tMJ <= tDuration) {
				jointTorqueCommand[0] = (torI + (torI - torF) * ( (15.0 * tNorm * tMult3) - (6.0 * tNorm * tNorm * tMult3) - (10.0 * tMult3))); // tDuration;
			}
			else if (tMJ <= tDuration + highTIme) {
			}
			else if (tMJ <= tDuration + highTIme + lowTIme) {
				// Turn it to the low torque in low time, in this case 0
				jointTorqueCommand[0] = kStylusTorqueConstant/0.2 * torI;
			}
			else {
				// Turn off perturbation
			    bIsPerturbing = false;
			}
		}
		//else if(

		if (GetAsyncKeyState('W') & 0x8000) {
			sumZReal += 0.01;
		}
		if (GetAsyncKeyState('S') & 0x8000) {
			sumZReal -= 0.01;
		}

		/* Periodically check if the gravity well callback has exited. */
		if (!hdWaitForCompletion(hGravityWell, HD_WAIT_CHECK_STATUS))
		{
			kill = 1;
			//fprintf(stderr, "Press any key to quit.\n");     
			//getch();
			break;
		}
	} while (!kill);

	/* For cleanup, unschedule callback and stop the scheduler. */
	hdStopScheduler();
	hdUnschedule(hGravityWell);

	/* Disable the device. */
	hdDisableDevice(hHD);
	exit(0);

	return 0;
}

static const hduVector3Dd nominalBaseTorque(200.0,300.0,200.0); //mNm

#define MAX_OUTPUT_DOF  3
static long alMotorDACValuesServo[MAX_OUTPUT_DOF];
//while (nValue < -32768 || nValue > 32767);

/*******************************************************************************
Servo callback.  
Called every servo loop tick.  Simulates a gravity well, which sucks the device 
towards its center whenever the device is within a certain range.
*******************************************************************************/
HDCallbackCode HDCALLBACK gravityWellCallback(void *data)
{
	//const HDdouble kStiffness = 0.075; /* N/mm */
	//const HDdouble kStiffness = 0.095; /* N/mm */
	//const HDdouble kStiffness = 0.395; /* N/mm */
	//const HDdouble kGravityWellInfluence = 800; /* mm */
	const HDdouble kTorqueInfluence = 3.14; /* radians */

	/* This is the position of the gravity well in cartesian
	(i.e. x,y,z) space. */

	//Sensor data of where I am
	hduVector3Dd wellPos;
	//wellPos[2]= 0.0 ;//global_desired_position[0];
	wellPos[1]= sumZReal ;//global_desired_position[1];
	//wellPos[2]=global_desired_position[2];

	//User command data of where I want to go

	HDErrorInfo error;
	hduVector3Dd currentAngles;
	hduVector3Dd force;
	hduVector3Dd angleDiff;

	HHD hHD = hdGetCurrentDevice();

	/* Begin haptics frame.  ( In general, all state-related haptics calls
	should be made within a frame. ) */
	WaitForSingleObject( hIOMutex, INFINITE );
	hdBeginFrame(hHD);

	/* Get the current position of the device. */
	hdGetDoublev(HD_CURRENT_JOINT_ANGLES, currentAngles);
	//if(fabs(position[0]) <  80.0)
	memset(force, 0, sizeof(hduVector3Dd));
	//   
	//   /* >  positionTwell = wellPos-position  < 
	//      Create a vector from the device position towards the gravity 
	//      well's center. */
	count++;
	//
	////wellPos2[0] = (count%5000)/100;


	//hduVecSubtract(angleDiff, global_desired_angle, currentAngles);
	angleDiff[1] = global_desired_angle[1] - currentAngles[1];
	angleDiff[2] = global_desired_angle[2] - currentAngles[2];

	if (hduVecMagnitude(angleDiff) < kTorqueInfluence)
	{
		//		jointTorqueCommand[0] =	angleDiff[1] * kStylusTorqueConstant;
		jointTorqueCommand[1] = angleDiff[1] * kStylusTorqueConstant;
		//jointTorqueCommand[2] = angleDiff[2] * kStylusTorqueConstant;
	}
	for(int i = 0; i < 3; i++)
	{
		if (jointTorqueCommand[i] > nominalBaseTorque[i])
			jointTorqueCommand[i] = nominalBaseTorque[i];
		else if (jointTorqueCommand[i] < -nominalBaseTorque[i])
			jointTorqueCommand[i] = -nominalBaseTorque[i];
	}

	//hdSetDoublev(HD_CURRENT_FORCE, globalInputForce);
	hdSetDoublev(HD_CURRENT_JOINT_TORQUE, jointTorqueCommand);

	/* Get data for logging */
	//hdGetDoublev(HD_CURRENT_POSITION, global_position);
	//if(fabs(global_position[0]) <  60.0)
	//perturbationOn = false;

	hdGetDoublev(HD_CURRENT_JOINT_TORQUE, globalOutputTorque);

	hdGetDoublev(HD_CURRENT_JOINT_ANGLES, global_joint_angles);
	if (gDataLogger.bIsRecording) {
		sprintf_s(	
			dataString, 
			"%f,%f,%f,%f,%f,%f,%f\n", 
			gTimeData.getCurrentTime(), 
			global_joint_angles[0], 
			global_joint_angles[1], 
			global_joint_angles[2], 
			globalOutputTorque[0], 
			globalOutputTorque[1], 
			globalOutputTorque[2] 
		);
		gDataLogger.sendLogString(dataString);
	}
	//hdGetDoublev(HD_CURRENT_JOINT_TORQUE, global_joint_torque);
	/* End haptics frame. */
	hdEndFrame(hHD);

	ReleaseMutex( hIOMutex );
	/* Check for errors and abort the callback if a scheduler error
	is detected. */
	if (HD_DEVICE_ERROR(error = hdGetError()))
	{
		hduPrintError(stderr, &error, 
			"Error detected while rendering gravity well\n");

		if (hduIsSchedulerError(&error))
		{
			return HD_CALLBACK_DONE;
		}
	}

	//if (gUdpServer.bTerminateCycle) {
	//	return HD_CALLBACK_DONE;
	//}

	/* Signify that the callback should continue running, i.e. that
	it will be called again the next scheduler tick. */
	return HD_CALLBACK_CONTINUE;
}

