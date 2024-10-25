import requests
from bs4 import BeautifulSoup
import re

# 爬取网页内容
url = "http://tonkiang.us/?iqtv=%E5%A4%A7%E6%B9%BE%E5%8C%BA%E5%8D%AB%E8%A7%86"
response = requests.get(url)
response.encoding = 'utf-8'  # 设置编码
soup = BeautifulSoup(response.text, 'html.parser')

# 查找所有包含 class="resultplus" 的 div 标签
results = []
for div in soup.find_all('div', class_='resultplus'):
    # 查找 <tba> 标签内的网址
    tba_content = div.find('tba')
    
    # 提取 IP 地址或网址内容
    if tab_content:
        url_in_tab = tab_content.get_text(strip=True)
        # 使用正则表达式匹配 IP 地址或网址
        ip_address = re.findall(r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b', url_in_tab)
        if ip_address:
            results.append(f"大湾区卫视,{ip_address[0]}")
        else:
            results.append(f"大湾区卫视,{url_in_tab}")
    
    if tba_content:
        url_in_tba = tba_content.get_text(strip=True)
        ip_address = re.findall(r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b', url_in_tba)
        if ip_address:
            results.append(f"大湾区卫视,{ip_address[0]}")
        else:
            results.append(f"大湾区卫视,{url_in_tba}")

# 保存结果到 key.txt 文件
with open('key.txt', 'w', encoding='utf-8') as file:
    file.write('\n'.join(results))
