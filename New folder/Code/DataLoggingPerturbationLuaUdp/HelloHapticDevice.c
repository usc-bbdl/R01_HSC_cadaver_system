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

#include <stdio.h>
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

int count;

int recording;
int kill;

void mainLoop(void);
void recordingLoop(void);

HANDLE    hIOMutex; //= CreateMutex (NULL, FALSE, NULL);	

hduVector3Dd global_position;
hduVector3Dd global_force;
hduVector3Dd global_joint_angles;
hduVector3Dd global_joint_torque;

HDCallbackCode HDCALLBACK gravityWellCallback(void *data);

/*******************************************************************************
 Main function.
 Initializes the device, starts the schedule, creates a schedule callback
 to handle gravity well forces, waits for the user to press a button, exits
 the application.
*******************************************************************************/
int main(int argc, char* argv[])
{    
	int KeyInfo;

	HDErrorInfo error;
    HDSchedulerHandle hGravityWell;

    /* Initialize the device, must be done before attempting to call any hd 
       functions. Passing in HD_DEFAULT_DEVICE causes the default device to be 
       initialized. */
    HHD hHD = hdInitDevice(HD_DEFAULT_DEVICE);

	hIOMutex = CreateMutex(NULL, FALSE, NULL);
	kill = 0;
	recording = 0;

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
	_beginthread( recordingLoop );
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
    
	//while (!_kbhit())
    do
	{
		KeyInfo = _getch();
		if ( tolower( KeyInfo ) == 'q') 
		{
			kill = 1;
		}
		else
		{
			if ( tolower( KeyInfo ) == 'r' )
			{
				if ( recording == 0) {
					printf("Data recording ON\n");
					recording = 1;
				}
				else
				{
					printf("Data recording OFF\n");
					recording = 0;
				}
			}
		}

		
		/* Periodically check if the gravity well callback has exited. */
        if (!hdWaitForCompletion(hGravityWell, HD_WAIT_CHECK_STATUS))
        {
            kill = 1;
			fprintf(stderr, "Press any key to quit.\n");     
            getch();
            break;
        }
//		printf("\n%d", count);
    } while (!kill);

    /* For cleanup, unschedule callback and stop the scheduler. */
    hdStopScheduler();
    hdUnschedule(hGravityWell);

    /* Disable the device. */
    hdDisableDevice(hHD);

    return 0;
}

/*******************************************************************************
 Servo callback.  
 Called every servo loop tick.  Simulates a gravity well, which sucks the device 
 towards its center whenever the device is within a certain range.
*******************************************************************************/
HDCallbackCode HDCALLBACK gravityWellCallback(void *data)
{
    //const HDdouble kStiffness = 0.075; /* N/mm */
	const HDdouble kStiffness = 0.045; /* N/mm */
    const HDdouble kGravityWellInfluence = 400; /* mm */

    /* This is the position of the gravity well in cartesian
       (i.e. x,y,z) space. */
    static const hduVector3Dd wellPos = {0,0,0};
	hduVector3Dd wellPos2 = {0.0, 0.0, 0.0};



    HDErrorInfo error;
    hduVector3Dd position;
    hduVector3Dd force;
    hduVector3Dd positionTwell;

    HHD hHD = hdGetCurrentDevice();

    /* Begin haptics frame.  ( In general, all state-related haptics calls
       should be made within a frame. ) */
   	WaitForSingleObject( hIOMutex, INFINITE );
	hdBeginFrame(hHD);

    /* Get the current position of the device. */
    hdGetDoublev(HD_CURRENT_POSITION, position);

    memset(force, 0, sizeof(hduVector3Dd));
    
    /* >  positionTwell = wellPos-position  < 
       Create a vector from the device position towards the gravity 
       well's center. */
    count++;
	
	//wellPos2[0] = (count%5000)/100;
	wellPos2[1] = 20*sin((count)*6.28/360);
	hduVecSubtract(positionTwell, wellPos2, position);

		
	
    
    /* If the device position is within some distance of the gravity well's 
       center, apply a spring force towards gravity well's center.  The force
       calculation differs from a traditional gravitational body in that the
       closer the device is to the center, the less force the well exerts;
       the device behaves as if a spring were connected between itself and
       the well's center. */
    if (hduVecMagnitude(positionTwell) < kGravityWellInfluence)
    {
        /* >  F = k * x  < 
           F: Force in Newtons (N)
           k: Stiffness of the well (N/mm)
           x: Vector from the device endpoint position to the center 
           of the well. */
		
        hduVecScale(force, positionTwell, kStiffness);
		
    }


    /* Send the force to the device. */
    hdSetDoublev(HD_CURRENT_FORCE, force);
    

	/* Get data for logging */
	hdGetDoublev(HD_CURRENT_POSITION, global_position);
	hdGetDoublev(HD_CURRENT_FORCE, global_force);
	hdGetDoublev(HD_CURRENT_JOINT_ANGLES, global_joint_angles);
	hdGetDoublev(HD_CURRENT_JOINT_TORQUE, global_joint_torque);
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

void recordingLoop( void )
{
	FILE *data;
	double time = 0.0;

	data = fopen("data.txt","w");
	while ( !kill )
	{
		if ( recording == 1)
		{
			Sleep(10);
			time += 0.01;
			WaitForSingleObject( hIOMutex, INFINITE );

			//printf("%f\t", time);
			//printf("%f\t%f\t%f\t", global_position[0], global_position[1], global_position[2]);
			//printf("%f\t%f\t%f\n", global_force[0], global_force[1], global_force[2]);

			fprintf(data, "%f\t", time);
			fprintf(data, "%f\t%f\t%f\t", global_position[0], global_position[1], global_position[2]);
			fprintf(data, "%f\t%f\t%f\t", global_force[0], global_force[1], global_force[2]);
			fprintf(data, "%f\t%f\t%f\t", global_joint_angles[0], global_joint_angles[1], global_joint_angles[2]);
			fprintf(data, "%f\t%f\t%f\t", global_joint_torque[0], global_joint_torque[1], global_joint_torque[2]);
			fprintf(data, "\n");

			ReleaseMutex( hIOMutex );
		}
	}
	fclose(data);
}

