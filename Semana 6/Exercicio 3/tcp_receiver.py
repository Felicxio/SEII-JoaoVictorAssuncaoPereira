import socket  # Importa o módulo socket para permitir a comunicação via rede.

TCP_IP = "127.0.0.1"  # Define o endereço IP para conexão.
FILE_PORT = 5005  # Define a porta para recebimento do nome do arquivo.
DATA_PORT = 5006  # Define a porta para recebimento dos dados do arquivo.
timeout = 3  # Define um timeout de 3 segundos para as conexões.
buf = 1024  # Define o tamanho do buffer para leitura dos dados.

sock_f = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Cria um objeto de socket TCP para receber o nome do arquivo.
sock_f.bind((TCP_IP, FILE_PORT))  # Associa o socket à porta FILE_PORT no endereço TCP_IP.
sock_f.listen(1)  # Coloca o socket em modo de escuta, permitindo uma conexão.

sock_d = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Cria um objeto de socket TCP para receber os dados do arquivo.
sock_d.bind((TCP_IP, DATA_PORT))  # Associa o socket à porta DATA_PORT no endereço TCP_IP.
sock_d.listen(1)  # Coloca o socket em modo de escuta, permitindo uma conexão.

while True:  # Loop infinito para aceitar conexões continuamente.
    conn, addr = sock_f.accept()  # Aceita uma conexão com o socket sock_f e obtém o objeto de conexão e o endereço do cliente.
    data = conn.recv(buf)  # Recebe os dados do cliente.
    if data:  # Verifica se há dados recebidos.
        print "File name:", data  # Imprime o nome do arquivo recebido.
        file_name = data.strip()  # Remove espaços em branco do nome do arquivo.

    f = open(file_name, 'wb')  # Abre o arquivo para escrita em modo binário.

    conn, addr = sock_d.accept()  # Aceita uma conexão com o socket sock_d e obtém o objeto de conexão e o endereço do cliente.
    while True:  # Loop para receber os dados do arquivo continuamente.
        data = conn.recv(buf)  # Recebe os dados do cliente.
        if not data:  # Verifica se não há mais dados recebidos.
            break  # Se não houver mais dados, sai do loop.
        f.write(data)  # Escreve os dados recebidos no arquivo.

    print "%s Finish!" % file_name  # Imprime uma mensagem indicando que a transmissão do arquivo foi concluída.
    f.close()  # Fecha o arquivo.
