import socket

def start_server():
    # Create a socket object
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Define the host and the port
    host = 'localhost'
    port = 11111

    # Bind the socket to the host and port
    server_socket.bind((host, port))

    # Listen for incoming connections
    server_socket.listen(1)
    print(f"Server listening on {host}:{port}")

    # Accept a connection
    client_socket, addr = server_socket.accept()
    print(f"Connection from {addr}")

    # Receive a message from the client
    message = client_socket.recv(1024).decode('utf-8')
    print(f"Received message: {message}")

    # Close the connection
    client_socket.close()
    server_socket.close()

if __name__ == "__main__":
    start_server()
