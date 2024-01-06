import requests
import time
import sys
import os
import re

if __name__ == '__main__':
    m3u8_url = input('请输入直播地址：') # 获取m3u8直播地址
    file_name = input('请输入直播名称：') # 获取m3u8文件名
    
# 创建目录
    os.makedirs('Cache/', exist_ok=True)
    
def download_m3u8_file(url):
    response = requests.get(url)
    if response.status_code == 200:
        m3u8_content = response.text
        file_name = re.search(r'#EXT-X-MAP:URI="([^"]+)"', m3u8_content).group(1)
        print("下载头文件：", file_name)
        
        file_url = url.rsplit('/', 1)[0] + '/' + file_name  # 拼接完整的文件URL
        file_content = requests.get(file_url).content
        
        with open('Cache/' + "." + file_name , 'wb') as f:
            f.write(file_content)
        print("头文件下载保存成功！")
              
download_m3u8_file(m3u8_url)

print("正在下载m4s切片")

def download_m3u8(url):
    
    response = requests.get(url)
    with open(f'Cache/' + file_name + ".m3u8", 'wb') as f:
        f.write(response.content)
    
    # 下载视频片段
    lines = response.text.split('\n')
    for line in lines:
        if line.endswith('.m4s'):
            m4s_url = url.rsplit("/", 1)[0] + "/" + line
            response = requests.get(m4s_url)
            with open(f'Cache/' + line , 'wb') as f:
                f.write(response.content)
        
# 每1秒访问一次m3u8直播源
while True:
    m3u8_url
    download_m3u8(m3u8_url)
    time.sleep(1)