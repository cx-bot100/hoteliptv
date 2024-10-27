from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time
import re

# 配置Chrome WebDriver
options = webdriver.ChromeOptions()
options.add_argument('--headless')  # 无头模式，不显示浏览器界面
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)

# 目标URL
url = "https://fofa.info/result?qbase64=InVkcHh5IiAmJiByZWdpb249Ikd1YW5nZG9uZyIgJiYgb3JnPSJDaGluYW5ldCI%3D"

# 用于存储不重复的IP地址和端口
unique_ips = set()

# 访问页面
try:
    driver.get(url)
    time.sleep(5)  # 等待页面加载，可以根据网络情况调整等待时间

    # 查找包含IP地址和端口的元素
    elements = driver.find_elements(By.XPATH, "//span[@data-clipboard-text]")
    for element in elements:
        ip_port = element.get_attribute("data-clipboard-text").strip()
        # 检查是否是有效的IP:PORT格式
        if re.match(r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}:\d+$', ip_port):
            unique_ips.add(ip_port)

except Exception as e:
    print(f"Failed to scrape {url} due to {e}")

finally:
    driver.quit()

# 将结果写入zblink.txt文件
with open('zblink.txt', 'w') as file:
    for ip in unique_ips:
        file.write(f"{ip}\n")

print(f"已抓取 {len(unique_ips)} 个IP地址和端口，并保存到zblink.txt文件中。")
