import requests
import time
import random

# ADB Node - Testing Phase Only: Do Not Use for Commercial Purposes
print("="*60)
print("🌲 ADB Node × Gradient 🌲")
print("⚠️  Testing Phase Only - Do Not Use for Commercial Purposes ⚠️")
print("="*60)

# Don't give credits but please don't sell
print("\nProudly Made By ADB Node (https://t.me/airdropbombnode)")
print("👤 Developed by: itsmesatyavir\n")
print("="*60)

# Function to read Bearer tokens from data.txt
def load_bearer_tokens():
    try:
        with open("data.txt", "r") as file:
            tokens = [token.strip() for token in file.readlines()]
            return tokens
    except Exception as e:
        print(f"❌ Error loading Bearer tokens: {e}")
        return []

# Function to read proxies from proxy.txt (optional)
def load_proxies():
    try:
        with open("proxy.txt", "r") as file:
            proxies = [proxy.strip() for proxy in file.readlines() if proxy.strip()]
            return proxies
    except FileNotFoundError:
        print("⚠️ proxy.txt not found. Proceeding without proxies.")
        return []
    except Exception as e:
        print(f"❌ Error loading proxies: {e}")
        return []

# Validate proxy format
def is_valid_proxy(proxy):
    # Basic check for proxy format (e.g., http://username:password@ip:port or http://ip:port)
    if not proxy:
        return False
    if not (proxy.startswith("http://") or proxy.startswith("https://") or proxy.startswith("socks5://")):
        return False
    parts = proxy.split("@")
    if len(parts) == 2:  # With username:password
        auth, ip_port = parts
        if not (":" in ip_port and auth.count(":") == 1):
            return False
    elif len(parts) == 1:  # Without username:password
        ip_port = parts[0]
        if not ":" in ip_port:
            return False
    return True

# Load Bearer tokens
auth_tokens = load_bearer_tokens()
if not auth_tokens:
    print("❌ No tokens found in data.txt. Please check your file!")
    exit()

# Load proxies (optional)
proxies_list = load_proxies()
# Filter valid proxies
proxies_list = [proxy for proxy in proxies_list if is_valid_proxy(proxy)]
if not proxies_list:
    print("⚠️ No valid proxies found. Proceeding without proxies.")

# API endpoint
url = "https://api.gradient.network/api/status"

# Function to fetch API status
def fetch_status(auth_token, proxies_list):
    headers = {
        "Authorization": f"Bearer {auth_token}",
        "Accept": "application/json",
    }

    # Try with proxy if available, fallback to no proxy if it fails
    if proxies_list:
        proxy = random.choice(proxies_list)
        proxy_dict = {
            "http": proxy,
            "https": proxy
        }
        print(f"🌐 Trying with proxy: {proxy}")
        try:
            response = requests.get(url, headers=headers, proxies=proxy_dict, timeout=10)
            if response.status_code == 200:
                data = response.json()
                print("✔️ Status Retrieved:", data)  # ✅ Success message
                return
            else:
                print(f"❌ Error with proxy {proxy}: Status Code {response.status_code}")
        except Exception as e:
            print(f"❌ Proxy {proxy} failed: {e}. Falling back to no proxy.")
    
    # Fallback to no proxy
    print("🌐 No proxy used.")
    try:
        response = requests.get(url, headers=headers, timeout=10)
        if response.status_code == 200:
            data = response.json()
            print("✔️ Status Retrieved:", data)  # ✅ Success message
        else:
            print(f"❌ Error: Status Code {response.status_code}")  # ❌ Error message
    except Exception as e:
        print(f"❌ An error occurred for token {auth_token[:10]}...: {e}")

# Polling loop - fetches data for all tokens every 10 seconds
while True:
    for auth_token in auth_tokens:
        fetch_status(auth_token, proxies_list)
        time.sleep(10)  # Wait 10 seconds before sending the next request
