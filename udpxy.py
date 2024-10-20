import socket
from concurrent.futures import ThreadPoolExecutor

# UDPXY扫描函数
def scan_udpxy(ip, port=4022, output_file="udpxy_servers.txt"):
    """
    扫描指定IP和端口是否有UDPXY服务，并将结果保存到文件中。
    """
    try:
        # 创建一个UDP socket
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.settimeout(3)  # 设置超时时间为3秒

        # UDPXY的默认请求（例如GET /status）
        message = b'GET /status'

        # 发送请求到指定IP和端口
        sock.sendto(message, (ip, port))

        # 尝试接收服务器响应
        response, _ = sock.recvfrom(1024)  # 接收1024字节的响应
        if response:
            print(f"{ip}:{port} - UDPXY server found")
            # 将发现的UDPXY服务器IP写入文件
            with open(output_file, "a") as file:
                file.write(f"{ip}:{port}\n")
    except socket.timeout:
        print(f"{ip}:{port} - No response (timeout)")
    except Exception as e:
        print(f"{ip}:{port} - Error: {e}")
    finally:
        sock.close()

# 扫描IP段函数
def scan_ip_range(start_ip, end_ip, port=4022, output_file="udpxy_servers.txt"):
    """
    扫描指定IP段内的UDPXY服务器，并将结果保存到文件中。
    """
    # 清空或创建输出文件
    open(output_file, "w").close()

    # 将IP地址转换为数字
    start_ip_split = list(map(int, start_ip.split('.')))
    end_ip_split = list(map(int, end_ip.split('.')))

    # 生成IP段内的IP地址
    ips = []
    for i in range(start_ip_split[3], end_ip_split[3] + 1):
        ips.append(f"{start_ip_split[0]}.{start_ip_split[1]}.{start_ip_split[2]}.{i}")
    
    # 使用线程池并行扫描
    with ThreadPoolExecutor(max_workers=200) as executor:
        for ip in ips:
            executor.submit(scan_udpxy, ip, port, output_file)

# 示例调用
if __name__ == "__main__":
    start_ip = "113.77.0.0"
    end_ip = "113.80.255.255"
    port = 4022  # UDPXY的默认端口
    output_file = "udpxy_servers.txt"  # 输出文件
    scan_ip_range(start_ip, end_ip, port, output_file)
    print(f"扫描完成，结果已保存到 {output_file}")
