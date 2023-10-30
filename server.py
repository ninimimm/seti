import socket
import ssl

hostname = "localhost"  # Имя вашего сервера или IP-адрес
port = 4433  # Порт, на котором запущен сервер

context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
context.load_cert_chain(certfile="server.crt", keyfile="server.key")
context.verify_mode = ssl.CERT_OPTIONAL
context.load_verify_locations(cafile="client.crt")

with socket.create_server((hostname, port)) as server_sock:
    server_sock = context.wrap_socket(server_sock, server_side=True)
    print("Сервер запущен...")
    while True:
        client_sock, addr = server_sock.accept()
        with client_sock:
            print("Соединение установлено с", addr)
            data = client_sock.recv(2048)
            print("Получено от клиента:", data)
