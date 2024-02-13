import socket  # Importa o módulo socket para permitir a comunicação via rede.
import select  # Importa o módulo select para monitorar os sockets para leitura.

UDP_IP = "127.0.0.1"  # Define o endereço IP para conexão.
IN_PORT = 5005  # Define a porta para recebimento dos dados.
timeout = 3  # Define um timeout de 3 segundos para esperar por dados.

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # Cria um objeto de socket UDP.
sock.bind((UDP_IP, IN_PORT))  # Associa o socket à porta IN_PORT no endereço UDP_IP.

while True:  # Loop infinito para receber dados continuamente.
    data, addr = sock.recvfrom(1024)  # Recebe dados do cliente.
    if data:  # Verifica se há dados recebidos.
        print "File name:", data  # Imprime o nome do arquivo recebido.
        file_name = data.strip()  # Remove espaços em branco do nome do arquivo.

    f = open(file_name, 'wb')  # Abre o arquivo para escrita em modo binário.

    while True:  # Loop para receber dados continuamente.
        ready = select.select([sock], [], [], timeout)  # Verifica se há dados prontos para leitura no socket.
        if ready[0]:  # Se houver dados prontos para leitura.
            data, addr = sock.recvfrom(1024)  # Recebe os dados do cliente.
            f.write(data)  # Escreve os dados recebidos no arquivo.
        else:  # Se o timeout ocorrer.
            print "%s Finish!" % file_name  # Imprime uma mensagem indicando que a transmissão do arquivo foi concluída.
            f.close()  # Fecha o arquivo.
            break  # Sai do loop.