import socket

server = socket.socket(
    socket.AF_INET,
    socket.SOCK_DGRAM
)

server.bind(("127.0.0.1", 33001))

print("UDP server listening...")

clients = {}

while True:
    data, address = server.recvfrom(1024)
    message = data.decode()

    # Register new clients
    if address not in clients:
        clients[address] = address
        print(f"New client connected: {address}")

    print(f"Received from {address}: {message}")

    # Forward message to all other clients
    for client_address in clients:
        if client_address != address:
            server.sendto(
                f"{address}: {message}".encode(),
                client_address
            )