import socket  # Importa o módulo socket para permitir a comunicação via rede.
import time  # Importa o módulo time para lidar com operações relacionadas ao tempo.
import sys  # Importa o módulo sys para acessar os argumentos da linha de comando.

UDP_IP = "127.0.0.1"  # Define o endereço IP para conexão.
UDP_PORT = 5005  # Define a porta para envio dos dados.
buf = 1024  # Define o tamanho do buffer para leitura dos dados do arquivo.
file_name = sys.argv[1]  # Obtém o nome do arquivo a partir dos argumentos da linha de comando.

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # Cria um objeto de socket UDP.
sock.sendto(file_name, (UDP_IP, UDP_PORT))  # Envia o nome do arquivo para o endereço UDP_IP e porta UDP_PORT.
print "Sending %s ..." % file_name  # Imprime uma mensagem indicando que o arquivo está sendo enviado.

f = open(file_name, "r")  # Abre o arquivo em modo de leitura.
data = f.read(buf)  # Lê os primeiros dados do arquivo com tamanho igual ao buffer.
while(data):  # Loop enquanto houver dados a serem lidos do arquivo.
    if(sock.sendto(data, (UDP_IP, UDP_PORT))):  # Envia os dados para o endereço UDP_IP e porta UDP_PORT.
        data = f.read(buf)  # Lê mais dados do arquivo com tamanho igual ao buffer.
        time.sleep(0.02)  # Espera um curto período de tempo para dar tempo ao receptor de salvar os dados.

sock.close()  # Fecha o socket.
f.close()  # Fecha o arquivo.
