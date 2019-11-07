from threading import Thread
import socket
import pickle

class Client(Thread):

    # Constructor
    def __init__(self, port, message):
        Thread.__init__(self)
        self.port = port
        self.message = message

    # Execute Client
    def run(self):
        # 1- Se conecta com cada peer do seu subconjunto pela porta do servidor do peer correspondende
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(('127.0.0.1', self.port))   

        # 2- Envia mensagem para o peer e espera uma resposta => 1 thread para cada envio. Espera todas as respostas com o join
        s.send(self.message)