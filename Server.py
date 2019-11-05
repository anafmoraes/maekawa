from threading import Thread
import socket
import pickle

class Server(Thread):

    # Constructor
    def __init__(self, port):
        super(Server, self).__init__()
        self.port = port

    # Open server
    def run(self):
        
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind(('127.0.0.1', self.port))
        s.listen()
        print("Inicializaçao do servidor...")

        while (data != "EXIT"):
            clientsocket, address = s.accept()
            # Quando receber uma mensagem:
            # 1: abre uma thread para tratar a mensagem
            data = self.clientsocket.recv(128)
            if (data[2] == "ASK"):
                if(voted | acessing):
                    onhold.add(self.clientsocket)
                    print("Requisição em espera...")
                else:
                    self.clientsocket.send("OK")
            elif (data[2] == "OK"):
                answers += 1
                print("Aumenta resposta")
            elif (data[2] == "FREE"):
                if(len(onhold) == 0):
                    voted = False
                else:
                    self.clientsocket.pop(onhold)
                    sendTo (self.clientsocket, "OK")               
            else:
                s.close()
                return 0
        s.close()
        return 0