import requests
import re
with open("directory.txt", "r") as file:
    directory = file.read().split("\n")
    for dir in directory:
        url = f"http://10.12.0.20/{dir}/flag.txt"
        resp = requests.get(url)
        if resp.status_code == 200:
            data = resp.text
            regex= r"cns{\w{32}}"
            flag = re.findall(regex, data)
            if flag:
                print(f"Flag Received at {url}: {flag}")
