#pragma once
#include <stdio.h>
#include <winsock2.h>
#include <windows.h>
#include <process.h>

#pragma comment(lib, "ws2_32.lib")

class UdpServer
{
	SOCKET s;
	struct sockaddr_in server, si_other;
	int slen, recv_len;
	static const int BUFLEN = 512;
	static const int PORT = 9877;
	char buf[BUFLEN];
	WSADATA wsa;

	int kill;
	HANDLE hIOMutex;
	static void staticUdpServerCallback(void*);
	void udpServerCallback(void);

public:
	bool bReceivedSTA;


	UdpServer();
	~UdpServer();
};

