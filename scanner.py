import socket
import threading
import sys
from queue import Queue
from datetime import datetime

print_lock = threading.Lock()

target = input("Taramak istediğiniz IP veya Domain adresini girin: ")

try:
    target_ip = socket.gethostbyname(target)
except socket.gaierror:
    print("\n[!] Geçersiz host adı veya IP adresi.")
    sys.exit()

print("-" * 50)
print(f"Hedef IP       : {target_ip}")
print(f"Tarama Başlangıcı: {str(datetime.now())}")
print("-" * 50)

queue = Queue()
open_ports = []

def port_scan(port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1.0)
        
        result = s.connect_ex((target_ip, port))
        
        if result == 0:
            with print_lock:
                print(f"[+] Port {port:5} : AÇIK")
                open_ports.append(port)
        s.close()
    except Exception:
        pass

def threader():
    while True:
        port = queue.get()
        
        port_scan(port)
        
        queue.task_done()

for x in range(100):
    t = threading.Thread(target=threader)
    t.daemon = True 
    t.start()


for port in range(1, 1025):
    queue.put(port)

queue.join()

print("-" * 50)
print(f"Tarama tamamlandı!")
print(f"Açık Portlar: {sorted(open_ports)}")
print("-" * 50)
