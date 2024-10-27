import requests
import re

# 文件 URL
url = "https://raw.githubusercontent.com/cx-bot100/redrainliptv/refs/heads/main/speedtest/zubo_fofa.txt"

# 请求文件内容
response = requests.get(url)
if response.status_code == 200:
    content = response.text
else:
    print(f"Failed to retrieve content from {url}")
    content = ""

# 使用正则表达式提取 "广东电信,#genre#" 到 "四川电信,#genre#" 之间的内容
pattern = re.compile(r'广东电信,#genre#(.*?)四川电信,#genre#', re.DOTALL)
match = pattern.search(content)
extracted_content = match.group(1).strip() if match else ""

# 将结果写入 zubo.txt 文件
with open('zubo.txt', 'w') as file:
    file.write('地方频道,#genre#\n')
    file.write(extracted_content)

print(f"已提取内容，并保存到zubo.txt文件中。")
