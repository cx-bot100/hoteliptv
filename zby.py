from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import requests
import re
import time

# 配置Chrome WebDriver
options = webdriver.ChromeOptions()
options.add_argument('--headless')  # 无头模式，不显示浏览器界面
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)

# 目标URL
url = "https://fofa.info/result?qbase64=InVkcHh5IiAmJiByZWdpb249Ikd1YW5nZG9uZyIgJiYgb3JnPSJDaGluYW5ldCI%3D"

# 用于存储不重复的IP地址
unique_links = set()

# 访问页面
try:
    driver.get(url)
    time.sleep(5)  # 等待页面加载，可以根据网络情况调整等待时间

    # 查找包含IP地址的div元素
    elements = driver.find_elements(By.CLASS_NAME, "hsxa-meta-data-list")
    for element in elements:
        # 提取div文本内容中的http和https链接
        matches = re.findall(r'http[s]?://[^\s]+', element.text)
        unique_links.update(matches)

except Exception as e:
    print(f"Failed to scrape {url} due to {e}")

finally:
    driver.quit()

# 用于存储验证通过的链接
valid_links = []

# 请求头
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36"
}

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

# 将结果写入zblink.txt文件
with open('zblink.txt', 'w') as file:
    for link in valid_links:
        file.write(f"{link}\n")

print(f"已验证 {len(valid_links)} 个链接，并保存到zblink.txt文件中。")
