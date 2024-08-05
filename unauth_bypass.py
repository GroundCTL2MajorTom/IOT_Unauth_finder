import os
import requests
import re
from collections import Counter
from concurrent.futures import ThreadPoolExecutor
import pyfiglet

banner = pyfiglet.figlet_format("IOT web bypass")
print("\033[32m"+banner+"\033[0m")
print("Version:1.0")
print("Author: GroundCTL2MajorTom@\033[34mIOTSec-Zone\033[0m")

for i in range(2):
    print(f"\n")

def load_excluded_extensions(filename):
    with open(filename, 'r') as f:
        return tuple(line.strip() for line in f if line.strip())

def load_patterns(filename):
    with open(filename, 'r') as f:
        return [line.strip() for line in f if line.strip()]

directory = input("请输入要列出文件的目录: ").strip(" ").strip("'")

host = input("请输入主机地址 (例如 http://example.com): ")

if not host.startswith("http://") and not host.startswith("https://"):
    host = "http://" + host

if host.endswith("/"):
    host = host[:-1]

pattern_file = "dic/login"
patterns = load_patterns(pattern_file)

extensions_file = "dic/extensions"
excluded_extensions = load_excluded_extensions(extensions_file)

file_list = []

for root, dirs, files in os.walk(directory):
    for filename in files:
        if not filename.lower().endswith(excluded_extensions):
            relative_path = os.path.relpath(os.path.join(root, filename), directory)
            
            file_list.append(relative_path)


valid_urls = []
length_count = Counter()

def fetch_url(filename):
    url = f"{host}/{filename}"  
    try:
        response = requests.get(url, timeout=5)  
        if response.status_code == 200:
            if not any(re.search(pattern, response.text, re.IGNORECASE) for pattern in patterns):
                content_length = len(response.content)
                valid_urls.append((url, content_length))
                length_count[content_length] += 1
    except requests.exceptions.RequestException as e:
        print(f"URL: {url}, 访问异常，请手动确认!")

with ThreadPoolExecutor(max_workers=10) as executor:
    executor.map(fetch_url, file_list)


filtered_urls = [(url, length) for url, length in valid_urls if length_count[length] <= 3]


filtered_urls.sort(key=lambda x: x[1])

for url, length in filtered_urls:
    print(f"URL: {url}, 疑似未授权访问页面!!")
