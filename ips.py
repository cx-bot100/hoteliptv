import requests
import re

# 目标 URL
url = "https://www.foodieguide.com/iptvsearch/hoteliptv.php"

# 设置 GET 请求的参数
params = {
    'page': 1,
    'net': '广东省',  # 填写具体的参数值
}

# 发送 GET 请求
response = requests.get(url, params=params)

# 检查请求是否成功
if response.status_code == 200:
    print("GET 请求成功，开始提取 IP 地址...")
    content = response.text

    # 使用正则表达式提取 IP 地址
    ip_pattern = re.compile(r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b')  # 匹配 IPv4 地址
    ip_addresses = ip_pattern.findall(content)

    # 去重并保存
    unique_ips = sorted(set(ip_addresses))
    with open('ips.txt', 'w', encoding='utf-8') as file:
        for ip in unique_ips:
            file.write(ip + '\n')

    print(f"提取完成，共找到 {len(unique_ips)} 个唯一 IP 地址，已保存到 ips.txt 文件中。")
else:
    print(f"GET 请求失败，HTTP 状态码: {response.status_code}")
