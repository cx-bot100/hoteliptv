import requests

# 文件 URL
url = "https://raw.githubusercontent.com/cx-bot100/redrainliptv/refs/heads/main/speedtest/zubo_fofa.txt"

# 请求文件内容
response = requests.get(url)
if response.status_code == 200:
    content = response.text
else:
    print(f"Failed to retrieve content from {url}")
    content = ""

# 筛选包含 '广东电信,#genre#' 和 '四川电信,#genre#' 的行
filtered_lines = [line for line in content.splitlines() if "广东电信,#genre#" in line or "四川电信,#genre#" in line]

# 将结果写入 zubo.txt 文件
with open('zubo.txt', 'w') as file:
    for line in filtered_lines:
        file.write(f"{line}\n")

print(f"已筛选 {len(filtered_lines)} 条内容，并保存到zubo.txt文件中。")
