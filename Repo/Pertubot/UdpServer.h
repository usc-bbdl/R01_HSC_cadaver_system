#pragma once
#include <stdio.h>
#include <winsock2.h>
#include <windows.h>
#include <process.h>
#include "DataLogger.h"

#pragma comment(lib, "ws2_32.lib")


class UdpServer
{
	static const size_t BUFLEN = 512;
	static const u_short PORT = 8888;
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
	bool bReceivedTTT;
	bool bReceivedPPP;
	bool bReceivedRRR;
	bool bReceivedName;
	char sNameOfDataFile[512];

	UdpServer();
	~UdpServer(void);
};

