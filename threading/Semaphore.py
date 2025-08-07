import threading
import time

sem = threading.Semaphore(1)

def access_elevator(person):
    print(f"{person} waiting...")
    sem.acquire()
    print(f"{person} entered elevator")
    time.sleep(2)
    print(f"{person} exited elevator")
    sem.release()

for i in range(6):
    threading.Thread(target=access_elevator, args=(f"Person {i+1}",)).start()
