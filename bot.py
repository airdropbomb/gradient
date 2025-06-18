import requests
import time

# ADB Node - Testing Phase Only: Do Not Use for Commercial Purposes
print("="*60)
print("🌲 ADB Node × Gradient 🌲")
print("⚠️  Testing Phase Only - Do Not Use for Commercial Purposes ⚠️")
print("="*60)

# Don't give credits but please don't sell
print("\nProudly Made By ADB Node (https://t.me/airdropbombnode)")
print("👤 Developed by: itsmesatyavir\n")
print("="*60)

# Function to read Bearer tokens from data.txt (each token on a new line)
def load_bearer_tokens():
    try:
        with open("data.txt", "r") as file:
            tokens = [token.strip() for token in file.readlines()]
            return tokens
    except Exception as e:
        print(f"❌ Error loading Bearer tokens: {e}")
        return []

# Load Bearer tokens
auth_tokens = load_bearer_tokens()

if not auth_tokens:
    print("❌ No tokens found in data.txt. Please check your file!")
    exit()

# API endpoint
url = "https://api.gradient.network/api/status"

# Function to fetch API status
def fetch_status(auth_token):
    headers = {
        "Authorization": f"Bearer {auth_token}",
        "Accept": "application/json",
    }

    try:
        response = requests.get(url, headers=headers)  # No proxies
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
        fetch_status(auth_token)
        time.sleep(10)  # Wait 10 seconds before sending the next request
