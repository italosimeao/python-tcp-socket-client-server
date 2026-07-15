import socket

print("Cliente TCP iniciado. Digite 'sair' para encerrar.")

try:
    while True:
        mensagem = input("Digite a mensagem a enviar: ")
        
        if mensagem.lower() == 'sair':
            print("Saindo...")
            break
            
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        try:
            client.connect(("10.0.2.15", 4466))
            client.send((mensagem + "\n").encode())
            
            pacotes_recebidos = client.recv(1024).decode()
            print("Resposta do servidor: " + pacotes_recebidos)
            client.close()
            
        except Exception as e:
            print("Erro ao conectar com o servidor. Garanta que ele está ativo.")
            client.close()

except KeyboardInterrupt:
    print("\nCliente encerrado.")
