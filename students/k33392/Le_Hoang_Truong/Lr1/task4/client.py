import socket
import threading
import sys

host = 'localhost'  # Хост (локальный компьютер)
port = 4000  # Порт для подключения

# Создаем сокет
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((host, port))  # Подключение к серверу

def receive_messages():
    """Прием сообщений от сервера"""
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            print(message)
        except:
            # Произошла ошибка, закрытие соединения
            print('An error occurred while receiving messages.')
            client_socket.close()

def send_messages():
    """Отправка сообщений на сервер"""
    while True:
        try:
            message = input()
            client_socket.send(message.encode('utf-8'))
        except KeyboardInterrupt:
            # Закрытие соединения при нажатии Ctrl+C
            # client_socket.close()
            client_socket.close()


def main():
    # Создаем два потока для приема и отправки сообщений
    receive_thread = threading.Thread(target=receive_messages)
    receive_thread.start()

    send_thread = threading.Thread(target=send_messages)
    send_thread.start()

if __name__ == "__main__":
    main()