from ping3 import ping

def ping_range(start_ip, end_ip):
    
    reachable_ips = []

    for i in range(start_ip, end_ip + 1):
        ip = f"192.168.98.{i}"
        response_time = ping(ip)
        if response_time is not None:
            print(f"{ip} is reachable (Response Time: {response_time} ms)")
            reachable_ips.append(ip)

    return reachable_ips

start_ip = 1
end_ip = 254

reachable_ip_list = ping_range(start_ip, end_ip)

print("Reachable IP addresses:")
for ip in reachable_ip_list:
    print(ip)


'''
Reachable IP addresses:
192.168.98.1
192.168.98.100
192.168.98.101
192.168.98.102
192.168.98.164
192.168.98.251
'''
