import socket 

host = 'localhost'  
port = 4000  

def calc(a, b, h):
    return (a + b) // 2 * h  # Функция для вычисления площади трапеции

def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Создание TCP-сокета
    s.bind((host, port))  # Привязка сокета к хосту и порту
    s.listen(1)  # Прослушивание входящих подключений
    print("Сервер слушает порт", port)

    try:
        while True:
            client, _ = s.accept()  # Принятие подключения от клиента
            mess = client.recv(1024).decode("utf-8")  # Получение сообщения от клиента
            clientMsg = "Message from client: {}".format(mess)
            
            a, b, h = map(int, mess.split(','))  # Разделение сообщения на отдельные значения
            print(clientMsg)
            area = calc(a, b, h)  # Вычисление площади трапеции
            client.send(str(area).encode("utf-8"))  # Отправка ответа клиенту

    except KeyboardInterrupt:
        # Прерывание программы при получении сигнала Ctrl+C
        pass

    except Exception as e:
        # Обработка других исключений
        print("Произошла ошибка:", str(e))

    finally:
        s.close()


if __name__ == "__main__":
    main()