import threading
import time

sem_impressora1 = threading.Semaphore(1)  
sem_impressora2 = threading.Semaphore(1)  
sem_scanner = threading.Semaphore(1)     

def usuario1():
    print("Usuário 1: Tentando acessar a Impressora 1...")
    sem_impressora1.acquire()
    print("Usuário 1: Impressora 1 adquirida.")
    time.sleep(3) 
    print("Usuário 1: Tentando acessar o Scanner...")
    sem_scanner.acquire()
    print("Usuário 1: Scanner adquirido.")
    time.sleep(3)  
    sem_scanner.release()
    sem_impressora1.release()
    print("Usuário 1: Tarefa concluída e recursos liberados.\n")

def usuario2():
    print("Usuário 2: Tentando acessar a Impressora 2...")
    sem_impressora2.acquire()
    print("Usuário 2: Impressora 2 adquirida.")
    time.sleep(3)  
    print("Usuário 2: Tentando acessar o Scanner...")
    sem_scanner.acquire()
    print("Usuário 2: Scanner adquirido.")
    time.sleep(3) 
    sem_scanner.release()
    sem_impressora2.release()
    print("Usuário 2: Tarefa concluída e recursos liberados.\n")

t1 = threading.Thread(target=usuario1)
t2 = threading.Thread(target=usuario2)
t1.start()
t2.start()
t1.join()
t2.join()
print("Execução finalizada.")
