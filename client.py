import xmlrpc.client

# import thread
import time

import netifaces as ni
ni.ifaddresses('wlp2s0')
ip = ni.ifaddresses('wlp2s0')[ni.AF_INET][0]['addr']

print("Ip do cliente = ", ip)

erro = False

while (True):
    if not erro:
        entrada = input("Sua mensagem: ")

    try:
        with xmlrpc.client.ServerProxy("http://192.168.1.8:8000/") as proxy:
            print("Mensagem recebida: ", str(proxy.game(entrada, ip)))
        erro = False

    except ConnectionRefusedError:
        print("Ocorreu um erro de conexao, tentando enviar a mensagem novamente")
        erro = True
        time.sleep(1)
