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
            proxies = [proxy.strip() for proxy in file.readlines()]
            return proxies
    except FileNotFoundError:
        print("⚠️ proxy.txt not found. Proceeding without proxies.")
        return []
    except Exception as e:
        print(f"❌ Error loading proxies: {e}")
        return []

# Load Bearer tokens
auth_tokens = load_bearer_tokens()
if not auth_tokens:
    print("❌ No tokens found in data.txt. Please check your file!")
    exit()

# Load proxies (optional)
proxies_list = load_proxies()

# API endpoint
url = "https://api.gradient.network/api/status"

# Function to fetch API status
def fetch_status(auth_token, proxies_list):
    headers = {
        "Authorization": f"Bearer {auth_token}",
        "Accept": "application/json",
    }

    # Use proxy only if proxies_list is not empty
    proxy_dict = {}
    if proxies_list:
        proxy = random.choice(proxies_list)
        proxy_dict = {
            "http": proxy,
            "https": proxy
        }
        print(f"🌐 Using proxy: {proxy}")
    else:
        print("🌐 No proxy used.")

    try:
        response = requests.get(url, headers=headers, proxies=proxy_dict if proxy_dict else None, timeout=10)
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
