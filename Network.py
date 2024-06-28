import socket
import time
import re
import requests
ip_address = ""
ports = []
service = ""
version = ""
info = {}
def scanMe(ip_address, ports):
    for port in ports:
        try:
            sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            sock.connect((ip_address,int(port)))
            print(f"Port {port} open on {ip_address}")
            try:
                sock.send(b"GET / HTTP/1.1\r\nHost:"+ip_address.encode()+b"\r\n\r\n")
                response = sock.recv(1024).decode('utf-8')
                if "ssh" in response.lower():
                    print(f"SSH detected at port {port}")
                    reg = r"(\w+)_(\d+\.\d+)"
                    input = re.findall(reg,response)[0]
                    service = input[0]
                    version = input[1]
                    print(service.lower(),version)
                    info[service.lower()] = version
                    sock.close()
                elif "HTTP/" in response:
                    print(f"Web Server detected at port {port}")
                    server_match = re.search(r'Server: (.*)', response)
                    if server_match:
                        reg = r"(\w+)/(\d+\.\d+(?:\.\d+))"
                        input = re.findall(reg,server_match.group(1))[0]
                        service = input[0]
                        version = input[1]
                        print(service,version)
                        info[service.lower()] = version
                        sock.close()
                elif "ftp" in response.lower():
                    print(f"FTP detected at port {port}")
                    res = sock.recv(1024).decode("UTF-8")
                    reg = r"220 (\w+) (\d+\.\d+(?:\.\d+))"
                    input = re.findall(reg,res)[0]
                    service = input[0]
                    version = input[1]
                    print(service,version)
                    info[service.lower()] = version
                    sock.close()
                elif "mail" in response.lower():
                    print(f"SMTP detected at port {port}")
            except Exception as e:
                print(e)
        except socket.error as e:
            print(f"Port {port} closed on {ip_address}")

def cpes(service, version):
    time.sleep(3)
    baseurl = "https://nvd.nist.gov/products/cpe/search/results"
    params = {"namingFormat": "2.3", "keyword": f"{service} {version}", "apikey":"00445e5c-19a7-48f4-a4fd-bea6cad40c23"}
    res = requests.get(baseurl, params = params)
    cpes = re.findall(r'cpe:(\d+\.\d+\:\w+\:\w+\:\w+)\:', res.text)
    for cpe in cpes:
        fetch_cves(cpe,version,service)

def fetch_cves(cpe,version,service):
    baseurl = "https://services.nvd.nist.gov/rest/json/cves/2.0"
    url = f"{baseurl}?virtualMatchString=cpe:{cpe}&versionEnd={version}&versionEndType=including"
    res = requests.get(url)
    if res.status_code == 200:
        data = res.json()
        vulnb = data['vulnerabilities']
        for vul in vulnb:
            cve_id = vul["cve"]["id"]
            print(f"{service}:{cve_id}")
    else:
        print(res.status_code)

if __name__ == "__main__":
    print("******NETWORK SCAN******")
    ip_address = "scanme.nmap.org"#"10.12.0.20"
    ports_value = input(f"Enter the Port Number(s)/range as 80-100 for {ip_address}: ")
    if "-" in ports_value:
        ports_range = ports_value.split("-")
        ports = list(range(int(ports_range[0]),int(ports_range[1])+1))
    elif "," in ports_value:
        ports = ports_value.split(",")
    else:
        ports = [ports_value]
    scanMe(ip_address, ports)
    for service, version in info.items():
        cpes(service,version)
