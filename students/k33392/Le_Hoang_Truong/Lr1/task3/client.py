import socket

host = 'localhost'  
port = 4000 

def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Создание TCP-сокета

    try:
        s.connect((host, port))  # Подключение к серверу

        request = "GET / HTTP/1.1\r\nHost: localhost\r\n\r\n"  # Формирование GET-запроса
        s.send(request.encode('utf-8'))  # Отправка запроса на сервер

        response = s.recv(1024).decode('utf-8')  # Получение ответа от сервера
        print(response)  # Вывод полученного ответа

    except KeyboardInterrupt:
        # Прерывание программы при получении сигнала Ctrl+C
        pass

    except Exception as e:
        # Обработка других исключений
        print("An error occurred:", str(e))


if __name__ == "__main__":
    main()