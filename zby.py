import requests
from bs4 import BeautifulSoup
import re

# 目标URL
url = "https://fofa.info/result?qbase64=InVkcHh5IiAmJiByZWdpb249Ikd1YW5nZG9uZyIgJiYgb3JnPSJDaGluYW5ldCI%3D" #广东

# 用于存储不重复的IP地址
unique_ips = set()

# 发起请求
try:
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36"
    }
    response = requests.get(url, headers=headers)
    response.encoding = 'utf-8'

    # 解析网页内容
    soup = BeautifulSoup(response.text, 'html.parser')

    # 查找所有<a>标签并提取包含IP地址的href链接
    links = soup.find_all('a', href=True)
    for link in links:
        href = link['href']
        # 使用正则表达式提取IP地址（IPv4格式）
        matches = re.findall(r'(\d+\.\d+\.\d+\.\d+)', href)
        unique_ips.update(matches)

except Exception as e:
    print(f"Failed to scrape {url} due to {e}")

# 用于存储验证通过的IP地址
valid_ips = []

# 验证每个IP地址的连接性
for ip in unique_ips:
    test_url = f"http://{ip}/status"
    try:
        # 检查URL是否可访问
        response = requests.get(test_url, headers=headers, timeout=10)
        # 如果响应状态码为200，则表示验证通过
        if response.status_code == 200:
            valid_ips.append(ip)
            print(f"{ip} is valid.")
        else:
            print(f"{ip} returned status code {response.status_code}.")
    except Exception as e:
        print(f"Failed to validate {ip} due to {e}")

# 将结果写入zblink.txt文件
with open('zblink.txt', 'w') as file:
    for ip in valid_ips:
        file.write(f"{ip}\n")

print(f"已验证 {len(valid_ips)} 个IP地址，并保存到zblink.txt文件中。")
