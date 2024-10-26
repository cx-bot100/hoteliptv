import requests
from bs4 import BeautifulSoup
import re

# 目标URL列表
urls = [
    "http://tonkiang.us/?iqtv=%E5%A4%A7%E6%B9%BE%E5%8C%BA%E5%8D%AB%E8%A7%86%E9%AB%98%E6%B8%85", #dwq
    "http://tonkiang.us/?iqtv=%E5%B9%BF%E4%B8%9C%E7%8F%A0%E6%B1%9F%E9%AB%98%E6%B8%85", #gdzj
    "http://tonkiang.us/?iqtv=%E5%B9%BF%E4%B8%9C%E4%BD%93%E8%82%B2%E9%AB%98%E6%B8%85", #gdty
    "http://tonkiang.us/?iqtv=%E5%B9%BF%E4%B8%9C%E6%96%B0%E9%97%BB%E9%AB%98%E6%B8%85", #gdxw
    "http://tonkiang.us/?iqtv=%E5%B9%BF%E4%B8%9C%E5%BD%B1%E8%A7%86%E9%AB%98%E6%B8%85" #gdys
]

# 保存结果的字典
ip_addresses = {
    "大湾区卫视": [],
    "广东珠江高清": [],
    "广东体育高清": [],
    "广东新闻高清": [],
    "广东影视高清": [],
}

# 遍历每个URL
for url in urls:
    try:
        # 发起请求
        response = requests.get(url)
        response.encoding = 'utf-8'

        # 解析网页内容
        soup = BeautifulSoup(response.text, 'html.parser')

        # 查找所有class为'resultplus'的div元素
        divs = soup.find_all('div', class_='resultplus')

        # 提取包含http和https的IP地址并分类
        for div in divs:
            # 获取频道信息
            resultplus_div = div.find_previous_sibling('div', class_='resultplus')
            if resultplus_div:
                resultplus_name = resultplus_div.get_text().strip()
                
                # 使用正则表达式匹配http或https开头的IP地址
                matches = re.findall(r'http[s]?://[^\s]+', div.get_text())
                
                # 根据频道分类存储IP地址
                if "大湾区卫视" in resultplus_name:
                    ip_addresses["大湾区卫视"].extend(matches)
                elif "广东珠江高清" in resultplus_name:
                    ip_addresses["广东珠江高清"].extend(matches)
                elif "广东体育高清" in resultplus_name:
                    ip_addresses["广东体育高清"].extend(matches)
                elif "广东新闻高清" in resultplus_name:
                    ip_addresses["广东新闻高清"].extend(matches)
                elif "广东影视高清" in resultplus_name:
                    ip_addresses["广东影视高清"].extend(matches)
    
    except Exception as e:
        print(f"Failed to scrape {url} due to {e}")

# 将结果写入key.txt文件
with open('key.txt', 'w') as file:
    file.write('地方频道,#genre#\n')
    for resultplus, ips in ip_addresses.items():
        for ip in ips:
            file.write(f"{resultplus},{ip}\n")

print(f"已提取 {sum(len(ips) for ips in ip_addresses.values())} 个IP地址，并保存到key.txt文件中。")
