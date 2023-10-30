import socket
import ssl

hostname = "localhost"  # Имя вашего сервера или IP-адрес
port = 4433  # Порт, на котором запущен сервер

context = ssl.create_default_context(ssl.Purpose.SERVER_AUTH)
context.load_verify_locations(cafile="server.crt")
context.verify_mode = ssl.CERT_OPTIONAL

with socket.create_connection((hostname, port)) as sock:
    with context.wrap_socket(sock, server_hostname=hostname) as ssock:
        print("Соединение установлено с сервером.")
        while True:
            message = input("Введите сообщение: ")
            ssock.send(message.encode('utf-8'))
            response = ssock.recv(2048)
            print("Получено от сервера:", response.decode('utf-8'))
