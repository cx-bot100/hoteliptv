import requests
from bs4 import BeautifulSoup

# 爬取网页内容
url = "http://tonkiang.us/?iqtv=%E5%A4%A7%E6%B9%BE%E5%8C%BA%E5%8D%AB%E8%A7%86"
response = requests.get(url)
response.encoding = 'utf-8'  # 设置编码
soup = BeautifulSoup(response.text, 'html.parser')

# 查找所有包含 onclick=nliu 的元素
results = []
for tag in soup.find_all(onclick=True):
    if 'nliu' in tag['onclick']:
        # 提取 IP 地址（假设 IP 地址在 onclick 字符串中）
        ip_address = tag['onclick'].split('peotua')[-1].strip("()'")
        results.append(f"大湾区卫视，{ip_address}")

# 保存结果到 key.txt 文件
with open('key.txt', 'w', encoding='utf-8') as file:
    file.write('\n'.join(results))
