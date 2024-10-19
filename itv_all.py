import os
import socket

# 定义要扫描的IP段（例如：192.168.1.1 - 192.168.1.255）
ip_prefix = "14.16.34.0"  # 修改为你要扫描的IP段前缀
start_ip = 14.16.34.0  # 开始IP
end_ip = 14.16.133.255  # 结束IP
port = 4022  # 检查的端口（例如HTTP端口）

# 输出文件路径
output_file = "ips.txt"

def is_ip_reachable(ip, port, timeout=2):
    """检查IP是否可用（端口开放）"""
    try:
        sock = socket.create_connection((ip, port), timeout=timeout)
        sock.close()
        return True
    except (socket.timeout, socket.error):
        return False

def scan_ip_range():
    """扫描IP段并将可用IP写入文件"""
    available_ips = []

    for i in range(start_ip, end_ip + 1):
        ip = f"{ip_prefix}{i}"
        print(f"Scanning {ip}...")

        if is_ip_reachable(ip, port):
            print(f"{ip} is reachable.")
            available_ips.append(ip)
        else:
            print(f"{ip} is not reachable.")

    # 写入可用IP到TXT文件
    with open(output_file, "w") as f:
        f.write("\n".join(available_ips))
    
    print(f"Scan complete. Available IPs saved to {output_file}.")

if __name__ == "__main__":
    scan_ip_range()
