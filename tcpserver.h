#ifndef TCPSERVER_H
#define TCPSERVER_H

#include "tcpserver_lib_global.h"
#include <QTcpServer>
#include <QList>
#include "tcpsocket.h"

class TCPSERVER_LIB_EXPORT Tcpserver : public QTcpServer
{
    Q_OBJECT
public:
    QList<tcpSocket*> socketList;

public:
    Tcpserver(QObject *parent = nullptr, int port = 0);
    qint64 writeData(tcpSocket* socket, const char* dat);

protected:
    void incomingConnection(qintptr socketDescriptor);

protected slots:
    void socketData(QString str, qint64 len);
    void clientDisconnect(int socketDescriptor );

signals:
    void updataServer(QString, qint64);

};

#endif // TCPSERVER_H
