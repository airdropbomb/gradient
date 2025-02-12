import requests
import time

# ADB Node - Testing Phase Only: Do Not Use for Commercial Purposes
print("="*60)
print("🌲 ADBNode × Gradient 🌲")
print("⚠️  Testing Phase Only - Do Not Use for Commercial Purposes ⚠️")
print("="*60)

#dont give credits but please don't sell 
print("\nProudly Made By ADB Node (https://t.me/airdropbombnode)")
print("👤 Developed by: itsmesatyavir\n")
print("="*60)

# Function to read Bearer tokens from data.txt (each token on a new line)
def load_bearer_tokens():
    try:
        with open("data.txt", "r") as file:
            tokens = file.readlines()  # Read all lines from the file
            tokens = [token.strip() for token in tokens]  # Remove any extra spaces or newlines
            return tokens
    except Exception as e:
        print(f"❌ Error loading Bearer tokens: {e}")
        return []

# Function to read proxies from proxy.txt (each proxy on a new line)
def load_proxies():
    try:
        with open("proxy.txt", "r") as file:
            proxies = file.readlines()  # Read all lines from the file
            proxies = [proxy.strip() for proxy in proxies]  # Clean up any extra spaces or newlines
            return proxies
    except Exception as e:
        print(f"❌ Error loading proxies: {e}")
        return []

# Load Bearer tokens and proxies
auth_tokens = load_bearer_tokens()
proxies = load_proxies()

if not auth_tokens or not proxies or len(auth_tokens) != len(proxies):
    print("❌ Mismatch in the number of Bearer tokens and proxies. Please ensure you have the same number of tokens and proxies.")
    exit()

# API endpoint and headers
url = "https://api.gradient.network/api/status"

def fetch_status(auth_token, proxy):
    headers = {
        "Authorization": f"Bearer {auth_token}",
        "Accept": "application/json",
    }

    proxies_dict = {
        "http": proxy,
        "https": proxy,
    }

    try:
        # Make the request using the specific proxy for the account
        response = requests.get(url, headers=headers, proxies=proxies_dict)
        if response.status_code == 200:
            data = response.json()
            print(f"✔️ Status Retrieved for token: {auth_token[:10]}...")  # Show only part of the token for privacy
        else:
            print(f"❌ Error: Status Code {response.status_code} for token: {auth_token[:10]}...")
    except requests.exceptions.RequestException:
        # Skip the error message and directly retry without the proxy
        print(f"🔄 Retrying without proxy for token: {auth_token[:10]}...")

        # Retry without the proxy
        try:
            response = requests.get(url, headers=headers)
            if response.status_code == 200:
                data = response.json()
                print(f"✔️ Status Retrieved (without proxy) for token: {auth_token[:10]}...")
            else:
                print(f"❌ Error: Status Code {response.status_code} for token: {auth_token[:10]}...")
        except Exception as e:
            print(f"❌ An error occurred without proxy for token: {auth_token[:10]}... {e}")

# Polling loop - fetches data for all tokens every 10 seconds
while True:
    for auth_token, proxy in zip(auth_tokens, proxies):
        fetch_status(auth_token, proxy)
        time.sleep(10)  # Wait 10 seconds before sending the next request
