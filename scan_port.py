import socket

ip = "192.168.18.12"
port_list = [80, 443, 139, 445, 8080, 546, 547, 21, 22, 23]

for port in port_list:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = s.connect_ex((ip, port))

    if result == 0:
        print('-' * 60)
        print('Port: ', port, 'Open')
        print('-' * 60)
    else:
        print('Port: ', port, 'Closed')