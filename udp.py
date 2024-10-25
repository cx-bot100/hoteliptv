import requests
from bs4 import BeautifulSoup
import re

# 目标URL
urls = ["http://tonkiang.us/?iqtv=%E5%A4%A7%E6%B9%BE%E5%8C%BA%E5%8D%AB%E8%A7%86""http://tonkiang.us/?iqtv=%E5%A4%A7%E6%B9%BE%E5%8C%BA%E5%8D%AB%E8%A7%86%E9%AB%98%E6%B8%85"

# 发起请求
response = requests.get(urls)
response.encoding = 'utf-8'

# 解析网页内容
soup = BeautifulSoup(response.text, 'html.parser')

# 查找所有class为'resultplus'的div元素
divs = soup.find_all('div', class_='resultplus')

# 提取包含http和https的IP地址
ip_addresses = []
for div in divs:
    # 使用正则表达式匹配http或https开头的IP地址
    matches = re.findall(r'http[s]?://[^\s]+', div.get_text())
    ip_addresses.extend(matches)

# 将结果写入key.txt文件，格式为“大湾区卫视,ip地址”
with open('key.txt', 'w') as file:
    for ip in ip_addresses:
        file.write(f"大湾区卫视,{ip}\n")

print(f"已提取 {len(ip_addresses)} 个IP地址，并保存到key.txt文件中。")
