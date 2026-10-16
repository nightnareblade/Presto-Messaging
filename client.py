# Main thread: Sends messages to the server.
# Background thread: Continuously listens for incoming messages.

import socket
import threading

client = socket.socket(
    socket.AF_INET,
    socket.SOCK_DGRAM
)

server_address = ("127.0.0.1", 33001)


# Receives messages from other clients
def receive_messages():
    while True:
        try:
            data, address = client.recvfrom(1024)
            print(f"\n{data.decode()}")
        except OSError:
            break


# Start receiving thread
receive_thread = threading.Thread(
    target=receive_messages,
    daemon=True
)

receive_thread.start()


# Main thread handles sending messages
while True:
    message = input("Enter message: ")

    if message == "quit":
        break

    client.sendto(
        message.encode(),
        server_address
    )

client.close()