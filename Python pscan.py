import socket

ip = input("Digite o Host ou IP a ser verificado: ")

ports = [] #Recebe as portas
count = 0

while count < 10:
    ports.append(int(input("Digite a porta a ser verificada: ")))
    count = count + 1

for port in ports:
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.settimeout(0.05)
    code = client.connect_ex((ip, port))
    if code == 0:
        print(f"Porta {port} - Aberta")
    else:
        print(f"Porta {port} - Fechada")

print("Scan finalizado")
