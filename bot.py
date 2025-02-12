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

# Prompt user for Authorization token
auth_token = "Please enter your Authorization token"

# Load the proxy from the proxy.txt file
def load_proxy():
    try:
        with open("proxy.txt", "r") as file:
            proxy = file.readline().strip()  # Read the first proxy from the file
            return proxy
    except Exception as e:
        print(f"❌ Error loading proxy: {e}")
        return None

# API endpoint and headers
url = "https://api.gradient.network/api/status"
headers = {
    "Authorization": f"Bearer {auth_token}",
    "Accept": "application/json",
}

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
        # Pass the proxies to the requests.get() method if available
        response = requests.get(url, headers=headers, proxies=proxies)
        if response.status_code == 200:
            data = response.json()
            print("✔️ Status Retrieved:", data)  # Tick symbol for successful response
        else:
            print(f"❌ Error: Status Code {response.status_code}")
    except Exception as e:
        print(f"❌ An error occurred: {e}")

# Polling loop - fetches data every 10 seconds
while True:
    fetch_status()
    time.sleep(10)  # Wait 10 seconds before sending the next request
