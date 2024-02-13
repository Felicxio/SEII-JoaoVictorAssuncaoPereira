import socket  # Importa o módulo de socket para comunicação de rede

HEADER = 64  # Define o tamanho do cabeçalho para 64 bytes
PORT = 5050  # Define a porta do servidor como 5050
FORMAT = "utf-8"  # Define o formato de codificação das mensagens como UTF-8
DISCONNECT_MESSAGE = "!DISCONNECT"  # Define a mensagem de desconexão
SERVER = '192.168.1.3'  # Define o endereço IP do servidor
ADDR = (SERVER, PORT)  # Cria uma tupla com o endereço do servidor e a porta

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Cria um objeto de socket TCP/IP
client.connect(ADDR)  # Conecta ao servidor usando o endereço e a porta especificados

# Função para enviar uma mensagem ao servidor
def send(msg):
    message = msg.encode(FORMAT)  # Codifica a mensagem para o formato UTF-8
    msg_length = len(message)  # Obtém o comprimento da mensagem
    send_length = str(msg_length).encode(FORMAT)  # Codifica o comprimento da mensagem para o formato UTF-8
    send_length += b' ' * (HEADER - len(send_length))  # Adiciona espaços em branco para preencher o cabeçalho
    client.send(send_length)  # Envia o comprimento da mensagem
    client.send(message)  # Envia a mensagem
    print(client.recv(2048).decode(FORMAT))  # Aguarda e exibe a resposta do servidor

send("Hello World!")  # Envia a mensagem "Hello World!"
input()  # Aguarda a entrada do usuário
send("Hello Everyone!")  # Envia a mensagem "Hello Everyone!"
input()  # Aguarda a entrada do usuário
send("Hello João!")  # Envia a mensagem "Hello João!"

send(DISCONNECT_MESSAGE)  # Envia a mensagem de desconexão



