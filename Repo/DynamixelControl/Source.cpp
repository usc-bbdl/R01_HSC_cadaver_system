#include <stdio.h>'
#include <conio.h>
#include "include/dynamixel.h"
#include "TimeData.h"

#ifdef _WIN64
#pragma comment(lib, "lib/x64/dynamixel.lib")
#else
#pragma comment(lib, "lib/x86/dynamixel.lib")
#endif

// Control table address
#define P_GOAL_POSITION_L		30
#define P_GOAL_POSITION_H		31
#define P_PRESENT_POSITION_L	36
#define P_PRESENT_POSITION_H	37
#define P_MOVING				46

// Defulat setting
#define DEFAULT_PORTNUM		4 // COM3
#define DEFAULT_BAUDNUM		34 // 1Mbps
#define DEFAULT_ID			1

int Perturb();

int Perturb()
{

}

int main(int argc, char *argv)
{
	int GoalPos[2] = {0, 1023};
	//int GoalPos[2] = {0, 4095}; // for EX serise
	int index = 0;
	int Moving, PresentPos;
	int CommStatus;
	TimeData gPerformanceTimer;
	double startTime;
	double currentTime;

	// Open device
	if( dxl_initialize(DEFAULT_PORTNUM, DEFAULT_BAUDNUM) == 0 )
	{
		printf( "Failed to open USB2Dynamixel!\n" );
		printf( "Press any key to terminate...\n" );
		getch();
		return 0;
	}
	else
		printf( "Succeed to open USB2Dynamixel!\n" );
	
	while(1)
	{
		printf( "Press any key to continue!(press ESC to quit)\n" );
		if(getch() == 0x1b)
			break;

		// Write goal position
		dxl_write_word( DEFAULT_ID, P_GOAL_POSITION_L, GoalPos[index] );
		startTime = gPerformanceTimer.getCurrentTime();
		do {
			// Read present position
			PresentPos = dxl_read_word( DEFAULT_ID, P_PRESENT_POSITION_L );
			currentTime = gPerformanceTimer.getCurrentTime();
			printf( "%f   %d   %d\n", currentTime, GoalPos[index], PresentPos );
				
		}while(currentTime - startTime < 1.2);
		if( index == 0 ) {
			index = 1;
		}
		else {
			index = 0;	
		}
	}

	// Close device
	dxl_terminate();
	printf( "Press any key to terminate...\n" );
	getch();
	return 0;
}