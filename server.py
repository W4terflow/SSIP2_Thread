import socket
import threading


def handle_client(conn, addr):
    print(f"Подключен клиент: {addr}")
    msg = ''

    while True:
        data = conn.recv(1024)
        if not data:
            break
        msg += data.decode()
        conn.send(data)

    print(f"Сообщение от клиента {addr}: {msg}")
    conn.close()
    print(f"Клиент {addr} отключен")


def start_server():
    sock = socket.socket()
    sock.bind(('', 9090))
    sock.listen(5)
    print("Сервер запущен и ожидает подключения клиентов...")

    while True:
        conn, addr = sock.accept()
        client_thread = threading.Thread(target=handle_client, args=(conn, addr))
        client_thread.start()


if __name__ == "__main__":
    start_server()