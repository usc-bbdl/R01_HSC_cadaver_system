#include "UdpClient.h"
#include <Windows.h>

UdpClient gUdpClient;

int main(void)
{
    while(1) {
        if (GetAsyncKeyState(VK_ESCAPE)) {
            break;
        }
    }
    return 0;
}