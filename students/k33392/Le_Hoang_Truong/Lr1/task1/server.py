import socket

host = 'localhost'  
port = 4000  

def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # Создание сокета UDP
    s.bind((host, port))  # Привязка сокета к адресу и порту

    print("Server listening on port", port)

    try:
        while True:
            mess, addr = s.recvfrom(1024)  # Получение данных от клиента
            mess = mess.decode("utf-8")  # Декодирование данных из байтов в строку
            clientMsg = "Message from Client: {}".format(mess)
            clientIP = "Client IP Address: {}".format(addr)

            print(clientMsg)  
            print(clientIP) 
            
            s.sendto(b'Hello client!', addr)  # Отправка данных обратно клиенту

    except KeyboardInterrupt:
        # Прерывание программы при получении сигнала Ctrl+C
        pass

    except Exception as e:
        # Обработка других исключений
        print("An error occurred:", str(e))

    finally:
        s.close()  # Закрытие сокета

if __name__ == "__main__":
    main()
