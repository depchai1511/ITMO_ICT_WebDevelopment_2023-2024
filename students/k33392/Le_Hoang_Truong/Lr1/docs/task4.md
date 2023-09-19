# Задание 4

Реализовать многопользовательский чат. Для применения с TCP
необходимо запускать клиентские подключения И прием и отправку
сообщений всем юзерам на сервере в потоках. Не забудьте сохранять
юзеров, чтобы потом отправлять им сообщения.

## Выполнение

### Реализация сервера

```python

import socket 
import threading 

host = 'localhost'  
port = 4000  
clients = [] 
client_names = [] 

def broadcast(message, sender):
    """Рассылка сообщения всем клиентам (кроме отправителя)"""
    for client in clients:
        if client != sender:
            client.send(message)

def handle_client(client):
    """Обработка подключения от клиента"""
    while True:
        try:
            message = client.recv(1024)
            if not message:
                raise Exception
            else:
                broadcast(message, client)

        except:
            # Произошла ошибка подключения, закрытие соединения и удаление клиента из списка
            index = clients.index(client)
            clients.remove(client)
            client.close()
            name = client_names[index]
            client_names.remove(name)
            
            broadcast(f'{name} покинул чат.\n'.encode('utf-8'), None)
            break

def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Создание серверного сокета
    s.bind((host, port))  # Привязка сокета к хосту и порту
    s.listen(10)  # Ожидание входящих подключений (максимум 10)

    print("Server listening on port", port)

    try:
        """Начало прослушивания подключений от клиентов"""
        while True:
            client, addr = s.accept()
            clientMsg = "New Client address: {}".format(addr)
            print(clientMsg)
            client.send('NAME'.encode('utf-8'))
            name = client.recv(1024).decode('utf-8')
            client_names.append(name)
            clients.append(client)

            print(f'New client name: {name}')
            broadcast(f'{name} has join the chat.\n'.encode('utf-8'), None)
            client.send('Connection successful! You have joined the chat.'.encode('utf-8'))
            thread = threading.Thread(target=handle_client, args=(client,))
            thread.start()

    except KeyboardInterrupt:
        # Обработка прерывания Ctrl+C
        pass

    except Exception as e:
        print("An error occurred:", str(e))

    finally:
        s.close()

if __name__ == "__main__":
    main()

```

### Реализация клиента

```python
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
```

## Пример работы

![Пример задания 4](image/task4.png)