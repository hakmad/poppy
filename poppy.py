import socket


def scan(host, port):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.settimeout(0.5)

    connection_result = client_socket.connect_ex((host, port))

    if connection_result == 0:
        print("Port open: {}".format(port))
    else:
        print("Port closed/filtered: {}".format(port))
        print("Connection error: {}".format(connection_result))

    client_socket.close()

target_ip = socket.gethostbyname("scanme.nmap.org")

print("Starting scan on: {}".format(target_ip))

for port in range(1, 65536):
    scan(target_ip, port)

print("Scan completed")
