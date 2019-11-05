from threading import Thread, Condition
from Server import *
from Client import *
import socket
import time
import sys
from random import randint

def main():
    #Lê arquivo com configuração da rede e salva em variavel global
    timeout = 3   # [seconds]
    voted = False
    accessing = False
    answers = 0
    onhold = []
    port = [8081]

    # Inicialização do servidor com a porta que foi passada como argumento
    # ! Mudar depois para porta fixa
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
            voted = True
            thread2 = []
            print("Quero entrar na seção crítica")

            # Mover ess bloco para uma função sendMessage("ASK")
            # Envio mensagem para cada peer do meu subconjunto
            for i in range(len(port)):
                thread2.append(Client(port[i], "ASK"))
                thread2[i].start()
            # Espero resposta de cada peer do meu subconjunto
            for i in range(len(port)):
                thread2[i].join()
            print ("Todas as threads de requisição foram finalizadas")

            while True:
                # Confere se pode ou não entrar na seção crítica
                if(answers == len(port)):
                    # 4- Entrei na seção crítica e atualizo status de que está na seção crítica
                    accessing = True
                    print("Estou acessando a seção crítica")
                    time.sleep(randint(1,5))
                    print("Meu trabalho na seção crítica terminou!")
                    sendMessage("FREE")

                    # Não entendi essa parte
                    if (len(onhold) == 0):
                        voted: False
                    else:
                        clientsocket = onhold.pop()
                        sendTo(p, "OK")

                    answers = 0
                    accessing = False
                    break
                    

    print("Peer finalizado!") 
    thread1.join()
    return 0

if __name__ == "__main__":
    main()        