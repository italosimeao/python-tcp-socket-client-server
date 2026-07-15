# 🚀 Python TCP Socket Client-Server Loop

Este projeto demonstra a implementação prática de uma arquitetura Cliente/Servidor utilizando sockets TCP em Python no ambiente Kali Linux. O sistema foi desenvolvido para permitir conexões persistentes e interativas através de loops infinitos (`while True`), tratando encerramentos de forma segura.

## 🛠️ Tecnologias e Ferramentas
* **Linguagem:** Python 3.x
* **Biblioteca Nativa:** `socket`
* **Sistema Operacional:** Kali Linux
* **Editor de Texto:** GNU nano

## ⚙️ Funcionalidades
* **Servidor TCP Persistente:** Escuta conexões na porta `4466`, exibe as mensagens recebidas em tempo real e armazena o histórico em um arquivo local (`output.txt`).
* **Cliente Interativo:** Permite ao usuário digitar mensagens consecutivas através do terminal, reconectando e transmitindo os dados de forma dinâmica.
* **Encerramento Seguro:** Implementação de `KeyboardInterrupt` (`Ctrl + C`) no servidor para fechar os sockets de forma limpa, evitando o travamento de portas no sistema operacional.
* **Comunicação Bidirecional:** O servidor valida o recebimento respondendo ao cliente, destravando a execução no terminal.

## 🚀 Como Executar o Projeto

1. Clone o repositório em sua máquina:
   ```bash
   git clone https://github.com
   ```

2. Abra dois terminais no Kali Linux. No primeiro terminal, inicie o Servidor:
   ```bash
   python3 servidor_TCP.py
   ```

3. No segundo terminal, execute o Cliente e digite suas mensagens:
   ```bash
   python3 cliente_TCP.py
   ```

4. Para encerrar o cliente, digite `sair`. Para parar o servidor, pressione `Ctrl + C`.
