/*****************************************************************************

Copyright (c) 2004 SensAble Technologies, Inc. All rights reserved.

OpenHaptics(TM) toolkit. The material embodied in this software and use of
this software is subject to the terms and conditions of the clickthrough
Development License Agreement.

For questions, comments or bug reports, go to forums at: 
    http://dsc.sensable.com

Module Name:

  HelloHapticDevice.c

Description: 

  This application creates a gravity well, which will attract
  the device towards its center when the device enters its proximity.  

*******************************************************************************/
#ifdef  _WIN64
#pragma warning (disable:4996)
#endif

extern "C"{
#include "lua.h"
#include "lualib.h"
#include "lauxlib.h"
}
#include <iostream>

#include <stdio.h>
#include <GL\glut.h>
#include <assert.h>

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
//#include <process.h>
#include <windows.h>
#include <time.h>
#include <pthread.h>

#define NUM_THREADS 1

#pragma comment(lib, "lua51.lib")
#pragma comment(lib, "pthreadVC2.lib")

const double MAX_FORCE = 8.0;

int count;
	const HDdouble kStylusTorqueConstant = 400.0;//3.14*40.0; /* radians */

int recording;
int kill;

void mainLoop(void);
//void recordingLoop(void);
void receiveUdp( void *dummy );
void recordingLoop( void *dummy);
void report_errors(lua_State *L, int status);

HANDLE    hIOMutex; //= CreateMutex (NULL, FALSE, NULL);	

hduVector3Dd global_position;
hduVector3Dd globalOutputTorque;
hduVector3Dd global_joint_angles;
hduVector3Dd global_joint_torque;

hduVector3Dd global_desired_position;
hduVector3Dd global_desired_angle;
hduVector3Dd globalInputForce;
bool perturbationOn = false;

lua_State *L;
int statusLua;

char gTimeStamp[120];
    hduVector3Dd jointTorqueCommand;

HDCallbackCode HDCALLBACK gravityWellCallback(void *data);

pthread_t               gThreads[NUM_THREADS];
pthread_mutex_t         gMutex;
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

		//fprintf(gDataFile,"%f", globalOutputForce[0]);
		fprintf(gDataFile,"%f\t%f\t%f\t", globalOutputTorque[0], globalOutputTorque[1], globalOutputTorque[2]);
		//fprintf(gDataFile,"%f\t%f\t%f\t", globalOutputForce[0], globalOutputForce[1], globalOutputForce[2]);
		//fprintf(gDataFile,"%f\t%f\t%f\t", global_position[0], global_position[1], global_position[2]);
		//fprintf(gDataFile,"%f\t%f\t%f\t", global_joint_angles[0], global_joint_angles[1], global_joint_angles[2]);
		
		fprintf(gDataFile,"\n");
    }
}


void TimerCB (int iTimer)
{
    LogData();

	// Set The Timer For This Function Again
	glutTimerFunc (3, TimerCB, 1);
}

void* NoTimerCB (void *)
{
    while (1)
    {
        LogData();
        Sleep(1);
    }
}

void InitProgram()
{
    time_t rawtime;
    struct tm *timeinfo;
    time(&rawtime);
    timeinfo = localtime(&rawtime);
    //sprintf_s(gTimeStamp,"%4d%02d%02d%02d%02d.txt",timeinfo->tm_year+1900, timeinfo->tm_mon+1, timeinfo->tm_mday, timeinfo->tm_hour, timeinfo->tm_min);
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
	int KeyInfo;

	HDErrorInfo error;
    HDSchedulerHandle hGravityWell;

    /* Initialize the device, must be done before attempting to call any hd 
       functions. Passing in HD_DEFAULT_DEVICE causes the default device to be 
       initialized. */
	//HDstring deviceP1= "PREMIUM"; //Case sensitive careful!
	HHD hHD = hdInitDevice("Premium");

    InitProgram();

	hIOMutex = CreateMutex(NULL, FALSE, NULL);
	kill = 0;
	recording = 0;

	lua_State *L = lua_open();
	luaL_openlibs(L);
	luaopen_base(L);
	luaopen_table(L);
    luaopen_string(L);
    luaopen_math(L);

	sumZReal = 1.82;

	double tim = 0.0;
	time_t rawtime;
	struct tm *timeinfo;
	time(&rawtime);
	timeinfo = localtime(&rawtime);
	sprintf(gTimeStamp, "C:\\Users\\Sangerlab\\Dropbox\\DataPertubot\\Pbot%4d%02d%02d%02d%02d.txt",timeinfo->tm_year+1900,timeinfo->tm_mon+1,timeinfo->tm_mday, timeinfo->tm_hour,timeinfo->tm_min);
	gDataFile = fopen(gTimeStamp,"a");

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
    pthread_mutex_init (&gMutex, NULL);
	int logdata_handle = pthread_create(&gThreads[0], NULL, NoTimerCB,	NULL);
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


	L = lua_open();
	luaL_openlibs(L);
	luaopen_base(L);
	luaopen_table(L);
    luaopen_string(L);
    luaopen_math(L);
    char filename[20] = "receiveUdp.lua";
	std::cerr << "-- Loading file: " << filename << std::endl;
    statusLua = luaL_loadfile(L, filename);

	count = 0;
	
	globalInputForce[2] = 0.0;
	globalInputForce[1] = 0.0;

	//statusLua = lua_pcall(L, 0, LUA_MULTRET, 0);
	//recording = 1;
	//perturbationOn = true;
	//Sleep(2000);
	//_beginthread( receiveUdp, 0, NULL);
	
	//CTimer timm;
	//timm.reset();
	bool perturbCycle = true; //true: high level of perturbation, low is low level

	//Remove comments to enable perturbation and recording
	//lua_pcall(L, 0, LUA_MULTRET, 0);
	getch();
	gIsRecording = true;
	Sleep(5000);
	perturbationOn = true;
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
    do
	{
		//printf("\n%f\t%f\t%f\t%f", global_joint_angles[0], global_joint_angles[1], global_joint_angles[2], jointTorqueCommand[0]);
		

		// Give a square waveq
		if(perturbationOn)			 
		{
			tMJ = gCurrentTick.QuadPart - gInitTick.QuadPart;
			QueryPerformanceCounter(&gCurrentTick);
			tMJ = gCurrentTick.QuadPart - gInitTick.QuadPart;
			tMJ /= gClkFrequency.QuadPart;
			
			

			if(0 == startPert)
			{
				startPert++;
				tMJInit = tMJ;
			}

			tMJ -= tMJInit;
			
			torI = 0.0;
			torF = 150.0*1.4*0.7;
			tDuration = 0.10;
			double tNorm = tMJ/tDuration;
			double highTIme = 2.2*0.45*0.30; 
			double lowTIme = 3.0; 
			tMult3 = tNorm * tNorm * tNorm;

			if(tMJ <= tDuration) 
			{
				jointTorqueCommand[0] = (torI + (torI - torF) * ( (15.0 * tNorm * tMult3) - (6.0 * tNorm * tNorm * tMult3) - (10.0 * tMult3))); // tDuration;
			}
			else if(tMJ <= tDuration + highTIme) 
			{
			}
			else if(tMJ <= tDuration + highTIme + lowTIme) 
			{
				jointTorqueCommand[0] = kStylusTorqueConstant/0.2 * torI;
			}
			else
			{
				startPert = 0;
			}
			////PREVIOUS PERTURBATION
			//globalInputForce[0] = -1.8;
			//Sleep(100);
			//globalInputForce[0] = 0.8;
			//Sleep(23);
			//globalInputForce[0] = 0.0;
			//Sleep(8000);
		}
		else

		{
			
		}
		
		if(GetAsyncKeyState('W') & 0x8000)
			sumZReal += 0.01;
		if(GetAsyncKeyState('S') & 0x8000)
			sumZReal -= 0.01;




		if(kbhit())
		{
			KeyInfo = _getch();
			if ( tolower( KeyInfo ) == 'q') 
			{
				kill = 1;
			}
			if ( tolower( KeyInfo ) == 'p') 
			{
				perturbationOn = true;
			}

			//QueryPerformanceFrequency(&frequency);
			//QueryPerformanceCounter(&tick0);
			//QueryPerformanceCounter(&tick1);
			//QueryPerformanceCounter(&tick2);
		}

		

		//wellPos2[1]+=0.01;
		
		/* Periodically check if the gravity well callback has exited. */
        if (!hdWaitForCompletion(hGravityWell, HD_WAIT_CHECK_STATUS))
        {
            kill = 1;
			fprintf(stderr, "Press any key to quit.\n");     
            getch();
            break;
        }
    } while (!kill);

    /* For cleanup, unschedule callback and stop the scheduler. */
    hdStopScheduler();
    hdUnschedule(hGravityWell);

    /* Disable the device. */
    hdDisableDevice(hHD);

    report_errors(L, statusLua);
	lua_close(L);


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
		jointTorqueCommand[2] = angleDiff[2] * kStylusTorqueConstant;
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

    /* Signify that the callback should continue running, i.e. that
       it will be called again the next scheduler tick. */
    return HD_CALLBACK_CONTINUE;
}

/*****************************************************************************/
//void receiveUdp( void *dummy )
//{
//	lua_pcall(L, 0, LUA_MINSTACK, 0);
//	//recording = 1;	
//	//perturbationOn = true;
//}

	//lua_pcall(L, 0, LUA_MULTRET, 0);
	//recording = 1;
	//perturbationOn = true;



void report_errors(lua_State *L, int status)
{
  if ( status!=0 ) {
    std::cerr << "-- " << lua_tostring(L, -1) << std::endl;
    lua_pop(L, 1); // remove error message
  }
}


