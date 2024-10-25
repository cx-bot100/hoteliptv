import requests
from bs4 import BeautifulSoup
import re

# 目标URL列表
urls = [
    "http://tonkiang.us/?iqtv=%E5%A4%A7%E6%B9%BE%E5%8C%BA%E5%8D%AB%E8%A7%86",
    "http://www.foodieguide.com/iptvsearch/?s=%E7%BF%A1%E7%BF%A0%E5%8F%B0&l=eowuxJvaa8bre/oee/oOWPsA=="
]

# 保存结果的列表
ip_addresses = []

# 遍历每个URL
for url in urls:
    try:
        # 发起请求
        response = requests.get(url)
        response.encoding = 'utf-8'

        # 解析网页内容
        soup = BeautifulSoup(response.text, 'html.parser')

        # 查找所有class为'resultplus'的div元素
        divs = soup.find_all('div', class_='gapeot')

        # 提取包含http和https的IP地址
        for div in divs:
            matches = re.findall(r'http[s]?://[^\s]+', div.get_text())
            ip_addresses.extend(matches)
    
    except Exception as e:
        print(f"Failed to scrape {url} due to {e}")

# 将结果写入key.txt文件，格式为“大湾区卫视,ip地址”
with open('key.txt', 'w') as file:
    for ip in ip_addresses:
        file.write(f"翡翠台,{ip}\n")

print(f"已提取 {len(ip_addresses)} 个IP地址，并保存到key.txt文件中。")
