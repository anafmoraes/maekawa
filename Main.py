from threading import Thread
import socket
import time
import sys
from random import randint

class Maekawa:
    timeout = 3   # [seconds]
    voted = False
    accessing = False
    answers = 0
    onhold = []
    port = [8081, 8082]

    def main():
        # Inicialização do servidor
        myPort = 8080
        thread1 = Server(myPort)
        thread1.start()

        timeout_start = time.time()

        while time.time() < timeout_start + timeout:

            #Entrar no loop de 1 em 1 segundo
            time.sleep(1)

            wantCS = randint(0,4) # [0 1 2 3 4]
            
            # Quero entrar na seção crítica
            if (wantCS == 0):
                self.__class__.voted = True
                thread2 = []
                print("Quero entrar na seção crítica")

                # Mover ess bloco para uma função sendMessage("ASK")
                sendMessage("ASK")

                while True:
                    # Confere se pode ou não entrar na seção crítica
                    if(answers == len(self.__class__.port)):
                        # 4- Entrei na seção crítica e atualizo status de que está na seção crítica
                        self.__class__.accessing = True
                        print("Estou acessando a seção crítica")
                        time.sleep(randint(1,5))
                        print("Meu trabalho na seção crítica terminou!")
                        sendMessage("FREE")

                        # if (len(onhold) == 0):
                        #     self.__class__.voted: False
                        # else:
                        #     clientsocket = onhold.pop()
                        #     sendTo(clientsocket, "OK")

                        self.__class__.answers = 0
                        self.__class__.accessing = False
                        break
        sendMessage("EXIT")
        print("Peer finalizado!") 
        thread1.join()
        return 0

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
                    # Estou acessando a seção crítica ou já respondi uma REQUEST com OK
                    if(voted | acessing):
                        onhold.add(self.clientsocket)
                        print("Requisição em espera...")
                    else:
                        self.clientsocket.send("OK")
                elif (data[2] == "OK"):
                    self.__class__answers += 1
                    print("Aumenta resposta")
                elif (data[2] == "FREE"):
                    # Caso a fila esteja vazia, a máquina j atualiza seu status para mostrar que não enviou nenhuma mensagem REPLY desde o recebimento da última mensagem RELEASE
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

    @classmethod

    def sendMessage(self, message):
        # Envio mensagem para cada peer do meu subconjunto
        for i in range(len(self.__class__.port)):
            thread2.append(Client(port[i], message))
            thread2[i].start()
        # Espero resposta de cada peer do meu subconjunto
        for i in range(len(self.__class__.port)):
            thread2[i].join()
            print ("Todas as threads de requisição foram finalizadas")


if __name__ == "__main__":
    main()        