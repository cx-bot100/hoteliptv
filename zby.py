import requests
from bs4 import BeautifulSoup
import re

# 目标URL
url = "https://fofa.info/result?qbase64=InVkcHh5IiAmJiByZWdpb249Ikd1YW5nZG9uZyI%3D" #广东

# 用于存储不重复的IP地址
unique_links = set()

# 发起请求
try:
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36"
    }
    response = requests.get(url, headers=headers)
    response.encoding = 'utf-8'

    # 解析网页内容
    soup = BeautifulSoup(response.text, 'html.parser')

    # 查找所有class为'hsxa-host'的span标签
    spans = soup.find_all('span', class_='hsxa-host')
    for span in spans:
        # 使用正则表达式匹配http或https的链接
        matches = re.findall(r'http[s]?://[^\s]+', span.get_text())
        unique_links.update(matches)

except Exception as e:
    print(f"Failed to scrape {url} due to {e}")

# 用于存储验证通过的链接
valid_links = []

# 验证每个链接的连接性
for link in unique_links:
    test_url = f"{link}/status"
    try:
        # 检查URL是否可访问
        response = requests.get(test_url, headers=headers, timeout=10)
        # 如果响应状态码为200，则表示验证通过
        if response.status_code == 200:
            valid_links.append(link)
            print(f"{link} is valid.")
        else:
            print(f"{link} returned status code {response.status_code}.")
    except Exception as e:
        print(f"Failed to validate {link} due to {e}")

# 将结果写入txt文件
with open('zblink.txt', 'w') as file:
    for link in valid_links:
        file.write(f"{link}\n")

print(f"已验证 {len(valid_links)} 个链接，并保存到txt文件中。")
