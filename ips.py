import requests
import time

# API的基础URL
base_url = "http://wifi.tuomengkj.com/Api/flowsearch"

# 定义cardno的起始和结束值
start_cardno = 13500000
end_cardno = 13600000

# 遍历范围内的cardno
for cardno in range(start_cardno, end_cardno + 1):
    # 构造完整的URL
    url = f"{base_url}?cardno={cardno}&sync=1"
    
    try:
        # 发送HTTP GET请求
        response = requests.get(url)
        
        # 检查HTTP状态码是否为200
        if response.status_code == 200:
            # 提取响应体并保存为文本文件
            with open(f"response_{cardno}.txt", "w", encoding="utf-8") as file:
                file.write(response.text)
            print(f"成功保存: response_{cardno}.txt")
        else:
            print(f"请求失败: cardno={cardno}, 状态码={response.status_code}")
    
    except requests.exceptions.RequestException as e:
        print(f"请求异常: cardno={cardno}, 错误={e}")
    
    # 添加延时以避免触发速率限制
    time.sleep(1)  # 每秒请求一次
