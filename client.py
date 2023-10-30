import socket
import ssl

hostname = "localhost"  # Имя вашего сервера или IP-адрес
port = 4433  # Порт, на котором запущен сервер

context = ssl.create_default_context(ssl.Purpose.SERVER_AUTH)
context.load_verify_locations(cafile="server.crt")
context.verify_mode = ssl.CERT_OPTIONAL

with socket.create_connection((hostname, port)) as sock:
    with context.wrap_socket(sock, server_hostname=hostname) as ssock:
        ssock.sendall(b"GET / HTTP/1.1\r\nHost: " + bytes(hostname, 'utf-8') + b"\r\n\r\n")
        print(ssock.recv(2048))
