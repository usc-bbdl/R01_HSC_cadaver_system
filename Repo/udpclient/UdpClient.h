#pragma once
#include <stdio.h>
#include <winsock2.h>
#include <windows.h>
#include <process.h>

#pragma comment(lib,"ws2_32.lib") 
 
#define SERVER "192.168.0.2" 
#define BUFLEN 512  
#define PORT 8888  
 
class UdpClient
{
    struct sockaddr_in si_other;
    int s, slen;
    char buf[BUFLEN];
    char message[BUFLEN];
    WSADATA wsa;
    int kill;
	HANDLE hIOMutex;	
    
	static void staticUdpClientCallback(void*);
    void udpClientCallback(void);

public:
    UdpClient(void);
    ~UdpClient(void);

};

