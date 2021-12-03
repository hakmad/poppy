import socket


target_ip = "127.0.0.1"

print("Starting scan on: {}".format(target_ip))

for port in range(1, 1023):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    connection_result = client_socket.connect_ex((target_ip, port))

    if (connection_result == 0):
        print("Port open: {}".format(port))

    client_socket.close()

print("Scan completed")
