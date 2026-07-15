import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("0.0.0.0", 4466))
server.listen(5)
print("Servidor TCP iniciado. Aguardando conexões...")

try:
    while True:
        file = open("output.txt", "a")
        client_socket, address = server.accept()
        print(f"Conexão recebida de: {address}")
        
        data = client_socket.recv(1024).decode()
        
        if not data:
            file.close()
            client_socket.close()
            continue
            
        print("Mensagem recebida: " + data.strip())
        
        file.write(data + "\n")
        file.close()
        
        client_socket.send(b"Mensagem recebida pelo servidor!")
        client_socket.close()

except KeyboardInterrupt:
    print("\nEncerrando o servidor de forma segura...")
except Exception as error:
    print("Erro no servidor: ", error)
finally:
    server.close()
