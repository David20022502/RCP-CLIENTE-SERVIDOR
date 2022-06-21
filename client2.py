import xmlrpc.client

proxy = xmlrpc.client.ServerProxy('http://localhost:9000')
username=input('usuario:')
while 1<2:
    mensaje = input('mensaje/ (0 ver mensajes):')
    if mensaje!="0":
        proxy.onSubmitMessage(mensaje,username)
    else:
        print(proxy.onShowMessage(username))
    