import socket

host = 'localhost'  
port = 4000 

def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # Создание сокета UDP
    s.connect((host, port))  # Установка соединения с сервером

    try:
        while True:
            user_input = input('Do you want to send a message to the server? (y/n)')  # Запрос ввода от пользователя
            user_input = user_input.lower()
            if user_input == 'n':
                break

            s.send(b"Hello, server")  # Отправка данных серверу
            reply_message = s.recv(1024).decode("utf-8")  # Получение ответного сообщения от сервера
            print(f"Server reply: {reply_message}")  # Вывод ответного сообщения сервера на экран
                
    except KeyboardInterrupt:
        pass

    except Exception as e:
        # Обработка других исключений
        print("An error occurred:", str(e))

    finally:
        s.close()  # Закрытие сокета

if __name__ == "__main__":
    main()