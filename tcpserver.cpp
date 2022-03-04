#include "tcpserver.h"
#include <QThread>

Tcpserver::Tcpserver(QObject *parent, int port)
    : QTcpServer{parent}
{
    listen(QHostAddress::Any, port);
}

qint64 Tcpserver::writeData(tcpSocket *socket, const char *dat)
{
    if(socket != nullptr)
    {
        return socket->write(dat);
    }
    return -1;
}

void Tcpserver::incomingConnection(qintptr socketDescriptor)
{
    tcpSocket *socket = new tcpSocket();
    socket->setSocketDescriptor(socketDescriptor);
    socketList.append(socket);

    connect(socket, &tcpSocket::dataReceived, this, &Tcpserver::socketData);
    connect(socket, &tcpSocket::updataDisconnect, this, &Tcpserver::clientDisconnect);
}

void Tcpserver::socketData(QString str, qint64 len)
{
    //qDebug() <<  "msg:"<< QThread::currentThread();
    emit updataServer(str, len);
}



void Tcpserver::clientDisconnect(int socketDescriptor)
{
    for(int i = 0; i < socketList.count(); ++i)
    {
        if(socketList.at(i)->socketDescriptor() == socketDescriptor)
        {
            socketList.remove(i);
            return;
        }
    }
}
