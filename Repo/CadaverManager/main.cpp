#include <stdio.h>
#include "UdpServer.h"
#include <Windows.h>

UdpServer gUdpServer;

int main()
{
	bool endProgram = false;
	int eventCounterA = 0;

	while (!endProgram) {
		if (GetAsyncKeyState(VK_ESCAPE) ) {
			endProgram = true;
		}
		if (GetAsyncKeyState(VK_SPACE) ) {
			eventCounterA = 0;
		}
		//if (GetAsyncKeyState(VK_UP) && eventCounterA ==0) {
		if(gUdpServer.bReceivedSTA && eventCounterA == 0) {
			eventCounterA++;
			printf("Pertubot Started\n");
			system("start C:\\Code\\Repo\\Pertubot\\x64\\ReleaseAcademicEdition\\HelloHapticDevice");
			printf("Pertubot Done\n");

			printf("MC_Cadaver Started\n");
			system("start C:\\Code\\Repo\\MC_Cadaver\\x64\\Release\\MC_Cadaver");
			printf("MC_Cadaver Done\n");
			gUdpServer.bReceivedSTA = false;
		}
//		if (GetAsyncKeyState(VK_DOWN) && eventCounterB == 0) {
//		//if(gUdpServer.bReceivedKIN && eventCounterA == 0) {
//			eventCounterB++;
//		}

	}


	return 0;
}