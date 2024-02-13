import socket  # Importa o módulo de socket para comunicação de rede
import threading  # Importa o módulo threading para lidar com múltiplas conexões simultaneamente

HEADER = 64  # Define o tamanho do cabeçalho para 64 bytes
PORT = 5050  # Define a porta do servidor como 5050
SERVER = socket.gethostbyname(socket.gethostname())  # Obtém o endereço IP do servidor
ADDR = (SERVER, PORT)  # Cria uma tupla com o endereço do servidor e a porta
FORMAT = 'utf-8'  # Define o formato de codificação das mensagens como UTF-8
DISCONNECT_MESSAGE = '!DISCONNET'  # Define a mensagem de desconexão

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Cria um objeto de socket TCP/IP
server.bind(ADDR)  # Liga o servidor ao endereço e porta especificados

# Função para lidar com um cliente conectado
def handle_client(conn, addr):
    print(f'[NEW CONNECTION] {addr} connected')  # Informa que um novo cliente se conectou
    connected = True  # Define uma flag para manter a conexão ativa
    while connected:  # Loop enquanto a conexão estiver ativa
        msg_length = conn.recv(HEADER).decode(FORMAT)  # Recebe o comprimento da mensagem
        if msg_length:  # Verifica se o comprimento da mensagem é válido
            msg_length = int(msg_length)  # Converte o comprimento da mensagem para inteiro
            msg = conn.recv(msg_length).decode(FORMAT)  # Recebe a mensagem completa
            if msg == DISCONNECT_MESSAGE:  # Verifica se a mensagem é de desconexão
                connected = False  # Define a flag de conexão como falsa para encerrar o loop
            print(f'[{addr}] {msg}')  # Exibe a mensagem recebida e o endereço do cliente
            conn.send("Msg received".encode(FORMAT))  # Envia uma confirmação de recebimento da mensagem
    conn.close()  # Fecha a conexão com o cliente após o loop

# Função para iniciar o servidor
def start():
    server.listen()  # Inicia o servidor e começa a ouvir por conexões
    print(f"[LISTENING] Server is listening on {SERVER}")  # Informa que o servidor está ouvindo
    while True:  # Loop infinito para aceitar conexões continuamente
        conn, addr = server.accept()  # Aceita uma nova conexão
        thread = threading.Thread(target=handle_client, args=(conn, addr))  # Cria uma nova thread para lidar com o cliente
        thread.start()  # Inicia a thread
        print(f"[ACTIVE CONNECTIONS] {threading.active_count() - 1}")  # Exibe o número de conexões ativas

print('[STARTING] server is starting...')  # Informa que o servidor está sendo iniciado
start()  # Inicia o servidor



