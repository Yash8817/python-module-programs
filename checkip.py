import socket
hostname = socket.gethostname()
dell_ip = socket.gethostbyname(hostname)
print("your are IP address is :" +dell_ip)