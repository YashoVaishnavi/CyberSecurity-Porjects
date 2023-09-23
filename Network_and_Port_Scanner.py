import re
import socket


open_ports = []

while True:
    try:
        ip_address = input("\n Enter the IP address: ")
        socket.inet_aton(ip_address)  # Check if the IP address is valid
        print("You entered a correct IP address.")
        break
    except socket.error:
        print("Invalid IP address. Please try again.")

while True:
    port_range_pattern = re.compile(r'^(\d+)-(\d+)$')
    print("Enter the range of ports you want to scan in network (e.g., 80-200):")
    port_range = input("Enter port range: ")

    if port_range_pattern.match(port_range):
        port_min = int(port_range_pattern.match(port_range).group(1))
        port_max = int(port_range_pattern.match(port_range).group(2))
        break
    else:
        print("Invalid port range. Please try again.")

for port in range(port_min, port_max + 1):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(0.2)
            result = s.connect_ex((ip_address, port))
            if result == 0:
                open_ports.append(port)
    except socket.error:
        pass

if len(open_ports) > 0:
    print("\nOpen ports:")
    for port in open_ports:
        print(f"Port {port} is open.")
else:
    print("\nNo open ports found.")