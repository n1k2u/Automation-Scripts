# Cybersecurity Automation Toolkit

This repository contains a collection of Python scripts for various cybersecurity automation tasks. These tools were developed as part of an Advanced Cybersecurity Automation course project.

## Scripts

### 1. Ansible Automation (ansible_automation.py)
- Configures a target system using Ansible
- Tasks include:
  - Adding a new user with sudo permissions
  - Configuring SSH to disallow root logins
  - Stopping and disabling the Apache service

### 2. Network Scanner (Network.py)
- Performs port scanning on specified IP addresses
- Detects services (SSH, Web Server, FTP, SMTP)
- Retrieves service versions
- Searches for related CPEs and CVEs

### 3. Log Parser (logparser.py)
- Traverses specified directories to find log files
- Removes entries containing a specific IP address from log files

### 4. SQL Injection Tool (simple_sqlinjection.py)
- Demonstrates a basic SQL injection technique
- Extracts hidden flag information from a vulnerable web application

### 5. Malware Scanner (malwaretest.py)
- Scans files using the VirusTotal API
- Calculates the percentage of positive detections
- Identifies potentially malicious files based on scan results

## Setup and Usage

1. Ensure you have Python 3.x installed.
2. Install required dependencies:
   ```
   pip install ansible pyyaml requests
   ```
3. Set up necessary API keys (e.g., VirusTotal API key in malwaretest.py).
4. Run individual scripts as needed.

## Note

These scripts are for educational purposes and should be used responsibly and ethically. Always ensure you have permission before scanning or testing systems you do not own.

## License

[MIT](https://choosealicense.com/licenses/mit/)
