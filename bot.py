import requests
import time

# FORESTARMY - Testing Phase Only: Do Not Use for Commercial Purposes
print("="*60)
print("🌲 ADBNode × Gradient 🌲")
print("⚠️  Testing Phase Only - Do Not Use for Commercial Purposes ⚠️")
print("="*60)

#dont give credits but please don't sell 
print("\nProudly Made By ADB Node (https://t.me/airdropbombnode)")
print("👤 Developed by: itsmesatyavir\n")
print("="*60)

# Function to read the Bearer token from data.txt
def load_bearer_token():
    try:
        with open("data.txt", "r") as file:
            token = file.readline().strip()  # Read the first line of the file for the Bearer token
            return token
    except Exception as e:
        print(f"❌ Error loading Bearer token: {e}")
        return None

# Load Bearer token
auth_token = load_bearer_token()

if not auth_token:
    print("❌ Bearer token not found. Please check your data.txt file.")
    exit()

# API endpoint and headers
url = "https://api.gradient.network/api/status"
headers = {
    "Authorization": f"Bearer {auth_token}",
    "Accept": "application/json",
}

# Load the proxy from the proxy.txt file
def load_proxy():
    try:
        with open("proxy.txt", "r") as file:
            proxy = file.readline().strip()  # Read the first proxy from the file
            return proxy
    except Exception as e:
        print(f"❌ Error loading proxy: {e}")
        return None

# Get the proxy from the file
proxy = load_proxy()

# Setup proxies dictionary with authentication if proxy is provided
if proxy:
    proxies = {
        "http": proxy,
        "https": proxy,
    }
else:
    proxies = None  # No proxy if not found

def fetch_status():
    try:
        # Try making the request using the proxy, if available
        response = requests.get(url, headers=headers, proxies=proxies)
        if response.status_code == 200:
            data = response.json()
            print("✔️ Status Retrieved:", data)  # Tick symbol for successful response
        else:
            print(f"❌ Error: Status Code {response.status_code}")
    except requests.exceptions.RequestException:
        # Skip the error message and directly retry without the proxy
        print("🔄 Retrying without proxy...")

        # Retry without the proxy
        try:
            response = requests.get(url, headers=headers)
            if response.status_code == 200:
                data = response.json()
                print("✔️ Status Retrieved (without proxy):", data)
            else:
                print(f"❌ Error: Status Code {response.status_code}")
        except Exception as e:
            print(f"❌ An error occurred without proxy: {e}")

# Polling loop - fetches data every 10 seconds
while True:
    fetch_status()
    time.sleep(10)  # Wait 10 seconds before sending the next request
