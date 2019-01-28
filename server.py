from xmlrpc.server import SimpleXMLRPCServer
import netifaces as ni

ni.ifaddresses('wlp2s0')
ip = ni.ifaddresses('wlp2s0')[ni.AF_INET][0]['addr']

print("IP do servidor: ", ip)


def game(pergunta, ip_cliente):
    print("Pergunta enviada por ", ip_cliente, ":", pergunta)
    resposta = input("Digite a sua resposta: ")
    return resposta

server = SimpleXMLRPCServer((ip, 8000))
print("Esperando conexões na porta 8000...")
server.register_function(game, "game")
server.serve_forever()
