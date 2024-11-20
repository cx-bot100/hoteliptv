import requests

# 目标URL
url = "http://foodieguide.com/iptvsearch/hoteliptv.php"

# 设置POST请求的参数
payload = {
    '576f4': '广东省',  # 例如：填写具体需要的参数值
    'Submit': '+',
    'town': '52576f44',  # 填写对应的参数
    'ave': 'KuudNuB02s',  # 填写对应的参数
    'address': 'grade-v-ca'  # 填写对应的参数
}

# 发送POST请求
response = requests.post(url, data=payload)

# 检查请求是否成功
if response.status_code == 200:
    print("请求成功，正在处理数据...")
    content = response.text

    # 处理返回的HTML或数据，这里以保存为文本文件为例
    with open('output.txt', 'w', encoding='utf-8') as file:
        file.write(content)
    print("数据已保存到output.txt文件中。")
else:
    print(f"请求失败，HTTP状态码: {response.status_code}")
