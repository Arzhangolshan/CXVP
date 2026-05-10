# .github/scripts/keep_alive.py
import requests
import time
import os
import sys
import json

def keep_codespace_alive(codespace_name, token):
    url = f"https://api.github.com/repos/edrisranjbar/g2ray/codespaces/{codespace_name}/commands"
    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/vnd.github+json",
        "Content-Type": "application/json"
    }
    payload = json.dumps({"command": "echo 'keep-alive signal at' $(date)"})
    
    while True:
        try:
            response = requests.post(url, headers=headers, data=payload)
            print(f"Keep-alive signal sent at {time.ctime()}. Status code: {response.status_code}")
        except Exception as e:
            print(f"Error: {e}")
        time.sleep(600) # هر ۱۰ دقیقه یک بار اجرا می‌شه

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python keep_alive.py <CODESPACE_NAME>")
        sys.exit(1)
    codespace_name = sys.argv[1]
    token = os.environ.get("GITHUB_TOKEN") # یا از secret خودت استفاده کن
    if not token:
        print("GITHUB_TOKEN not found.")
        sys.exit(1)
    keep_codespace_alive(codespace_name, token)
