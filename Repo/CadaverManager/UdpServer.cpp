#include "UdpServer.h"


UdpServer::UdpServer()
{
	bReceivedSTA = false;

	hIOMutex = CreateMutex(NULL, FALSE, NULL);
	kill = 0;
	_beginthread(UdpServer::staticUdpServerCallback, 0, this);
}


UdpServer::~UdpServer(void)
{
	kill = 1;

	bReceivedSTA = false;

    closesocket(s);
    WSACleanup();
}

void UdpServer::staticUdpServerCallback(void *a)
{
	((UdpServer *) a)->udpServerCallback();
}

void UdpServer::udpServerCallback(void)
{
	slen = sizeof(si_other);

	//Initialize winsock
	printf("\nInitialising Winsock...");
    if (WSAStartup(MAKEWORD(2,2),&wsa) != 0)
    {
        printf("Failed. Error Code : %d",WSAGetLastError());
        exit(EXIT_FAILURE);
    }
    printf("Initialised.\n");
     
    //Create a socket
    if((s = socket(AF_INET , SOCK_DGRAM , 0 )) == INVALID_SOCKET)
    {
        printf("Could not create socket : %d" , WSAGetLastError());
    }
    printf("Socket created.\n");
     
    //Prepare the sockaddr_in structure
    server.sin_family = AF_INET;
    server.sin_addr.s_addr = INADDR_ANY;
    server.sin_port = htons( PORT );
     
    //Bind
    if( bind(s ,(struct sockaddr *)&server , sizeof(server)) == SOCKET_ERROR)
    {
        printf("Bind failed with error code : %d" , WSAGetLastError());
        exit(EXIT_FAILURE);
    }
    puts("Bind done");
 
    //keep listening for data
    while(!kill)
    {
        //printf("Waiting for data...");
        fflush(stdout);
         
        //clear the buffer by filling null, it might have previously received data
        memset(buf,'\0', BUFLEN);
         
        if ((recv_len = recvfrom(s, buf, BUFLEN, 0, (struct sockaddr *) &si_other, &slen)) == SOCKET_ERROR)
        {
			if (kill) {
				break;
			}
			else {
				//printf("recvfrom() failed with error code : %d" , WSAGetLastError());
				exit(EXIT_FAILURE);
			}
        }
         
        //print details of the client/peer and the data received
        //printf("Received packet from %s:%d\n", inet_ntoa(si_other.sin_addr), ntohs(si_other.sin_port));
        //printf("Data: %s\n" , buf);

		if (buf[0] == 'S' && buf[1] == 'T' && buf[2] == 'A' && buf[3] == '\0') {
			bReceivedSTA = true;
		}
         
        //now reply the client with the same data
        if (sendto(s, buf, recv_len, 0, (struct sockaddr*) &si_other, slen) == SOCKET_ERROR)
        {
            printf("sendto() failed with error code : %d" , WSAGetLastError());
            exit(EXIT_FAILURE);
        }
    }
} 

