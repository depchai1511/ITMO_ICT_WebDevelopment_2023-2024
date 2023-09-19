
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
