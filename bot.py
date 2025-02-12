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

# Prompt user for Authorization token
auth_token = input("🔑 Please enter your Authorization token: ")

# API endpoint and headers
url = "https://api.gradient.network/api/status"
headers = {
    "Authorization": f"Bearer {auth_token}",
    "Accept": "application/json",
}

def fetch_status():
    try:
        response = requests.get(url, headers=headers)
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
