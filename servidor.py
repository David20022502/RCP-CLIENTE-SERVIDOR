from xmlrpc.server import SimpleXMLRPCServer

import logging
import os

logging.basicConfig(level=logging.INFO)
messages=[]
server=SimpleXMLRPCServer(
    ('localhost', 9000),
    logRequests=True
)

def onShowMessage(user):
    if len(messages)>0:
        mes=messages[len(messages)-1]
        mes1=mes.split(":")
        if mes1[1]!=user:
            return mes1[1]+" le dice: "+mes1[0]
        else:
            return "No tienes mensajes"
    else:
        return "No tienes mensajes"

def onSubmitMessage(message,user):
    messages.append(message+":"+user)
    data=onShowMessage(user)
    return data


server.register_function(onSubmitMessage)
server.register_function(onShowMessage)

try:
    print('precione crtl+c para salir')
    server.serve_forever()
except KeyboardInterrupt:
    print('saliendo')