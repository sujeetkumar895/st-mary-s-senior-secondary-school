import requests

# Your SBI API credentials and endpoint
api_key = "your_api_key"
api_secret = "your_api_secret"
account_number = "your_account_number"
endpoint = "https://api.sbi.co.in/account/balance"

# Headers including the authorization (assuming API requires it)
headers = {
    "API-Key": api_key,
    "Authorization": f"Bearer {api_secret}",
    "Content-Type": "application/json"
}

# Request body
data = {
    "accountNumber": account_number
}

# Make the API call
response = requests.post(endpoint, headers=headers, json=data)

# Check the response
if response.status_code == 200:
    balance_info = response.json()
    print(f"Account Balance: {balance_info['balance']}")
else:
    print(f"Failed to fetch balance. Status code: {response.status_code}, Error: {response.text}")
