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

# 分类内容
local_channels = []
central_channels = []
other_channels = []

# 按行分类
for line in extracted_content.splitlines():
    if "广东|广东卫视" in line or "卫视" in line:
        local_channels.append(line)
    elif "CCTV" in line:
        central_channels.append(line)
    else:
        other_channels.append(line)

# 将分类后的内容写入 zubo.txt 文件
with open('zubo.txt', 'w') as file:
    file.write("地方频道,#genre#\n")
    for line in local_channels:
        file.write(f"{line}\n")

    file.write("\n央视频道,#genre#\n")
    for line in central_channels:
        file.write(f"{line}\n")

    file.write("\n其他频道,#genre#\n")
    for line in other_channels:
        file.write(f"{line}\n")

print(f"已分类并保存到zubo.txt文件中。")
