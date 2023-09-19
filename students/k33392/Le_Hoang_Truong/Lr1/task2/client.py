import socket

host = 'localhost' 
port = 4000  

def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Создание TCP-сокета
    s.connect((host, port))  # Подключение к серверу

    try:
        while True:
            user_input = input('Do you want to send a message to the server? (y/n)')    # Запрос ввода от пользователя
            user_input = user_input.lower()
            if user_input == 'n':
                break

            a = input("Enter the larger base of the trapezoid: ")
            b = input("Enter the smaller base of the trapezoid: ")
            h = input("Enter the height of the trapezoid: ")
            message = a + "," + b + "," + h  # Формирование сообщения

            s.send(message.encode("utf-8"))  # Отправка сообщения серверу
            reply_message = s.recv(1024).decode("utf-8")  # Получение ответа от сервера
            print(f"Area is: {reply_message}")   # Вывод ответа сервера (вычисленная площадь)
                
    except KeyboardInterrupt:
        pass

    except Exception as e:
        # Обработка других исключений
        print("An error occurred:", str(e))

    finally:
        s.close()  # Закрытие сокета

if __name__ == "__main__":
    main()