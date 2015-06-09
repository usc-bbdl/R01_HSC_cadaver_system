#include "UdpServer.h"
#include <windows.h>

UdpServer gUdpServer;

int main()
{
	
	while(1) {
		if (GetAsyncKeyState(VK_ESCAPE)) {
			break;
		}
	}


	return 0;
}
