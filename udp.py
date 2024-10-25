import requests
from bs4 import BeautifulSoup

# 爬取网页内容
url = "http://tonkiang.us/?iqtv=%E5%A4%A7%E6%B9%BE%E5%8C%BA%E5%8D%AB%E8%A7%86"
response = requests.get(url)
response.encoding = 'utf-8'  # 设置编码
soup = BeautifulSoup(response.text, 'html.parser')

# 查找所有包含 class="resultplus" 的 div 标签
results = []
for div in soup.find_all('div', class_='resultplus'):
    # 假设 <tab> 标签包含我们需要的 IP 地址
    tab_content = div.find('tba')
    if tab_content:
        ip_address = tab_content.get_text(strip=True)
        results.append(f"大湾区卫视,{ip_address}")

# 保存结果到 key.txt 文件
with open('key.txt', 'w', encoding='utf-8') as file:
    file.write('\n'.join(results))
