#pragma once
#include <stdio.h>
#include <winsock2.h>
#include <windows.h>
#include <process.h>

#pragma comment(lib, "ws2_32.lib")

#define BUFLEN 512
#define PORT 8888

class UdpServer
{
	SOCKET s;
	struct sockaddr_in server, si_other;
	int slen, recv_len;
	char buf[BUFLEN];
	WSADATA wsa;

	int kill;
	HANDLE hIOMutex;
	static void staticUdpServerCallback(void*);
	void udpServerCallback(void);

public:
	UdpServer(void);
	~UdpServer(void);
};

