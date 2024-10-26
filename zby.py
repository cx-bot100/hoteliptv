from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
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
    time.sleep(10)  # 等待页面加载，可以根据网络情况调整等待时间

    # 查找包含IP地址的div元素
    elements = driver.find_elements(By.CLASS_NAME, "hsxa-host")
    for element in elements:
        # 提取div文本内容中的http和https链接
        matches = re.findall(r'http[s]?://[^\s]+', element.text)
        unique_links.update(matches)

except Exception as e:
    print(f"Failed to scrape {url} due to {e}")

finally:
    driver.quit()

# 将结果写入zblink.txt文件
with open('zblink.txt', 'w') as file:
    for link in unique_links:
        file.write(f"{link}\n")

print(f"已抓取 {len(unique_links)} 个链接，并保存到zblink.txt文件中。")
