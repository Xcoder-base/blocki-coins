import requests
import base64
import json

# Replace with your Daraja API credentials
consumer_key = "YOUR_CONSUMER_KEY"
consumer_secret = "YOUR_CONSUMER_SECRET"
shortcode = "YOUR_SHORTCODE"
lipa_na_mpesa_online_passkey = "YOUR_PASSKEY"
lipa_na_mpesa_online_shortcode = "YOUR_LIPA_SHORTCODE"
initiator_name = "YOUR_INITIATOR_NAME"
security_credential = "YOUR_SECURITY_CREDENTIAL"

# Generate the security credential
timestamp = "YOUR_TIMESTAMP"  # Replace with a timestamp
password = base64.b64encode(f"{lipa_na_mpesa_online_shortcode}{lipa_na_mpesa_online_passkey}{timestamp}".encode()).decode()

# Define the endpoint URLs for B2C and C2B
b2c_url = "https://sandbox.safaricom.co.ke/mpesa/b2c/v1/paymentrequest"
c2b_url = "https://sandbox.safaricom.co.ke/mpesa/c2b/v1/simulate"

# Prepare headers for both B2C and C2B
headers = {
    "Authorization": f"Bearer {base64.b64encode(f'{consumer_key}:{consumer_secret}'.encode()).decode()}",
    "Content-Type": "application/json"
}

# B2C Operation
def perform_b2c_transaction():
    payload = {
        "InitiatorName": initiator_name,
        "SecurityCredential": security_credential,
        "CommandID": "SalaryPayment",
        "Amount": "1000",  # Replace with the amount
        "PartyA": shortcode,
        "PartyB": "PHONE_NUMBER",  # Replace with the recipient's phone number
        "Remarks": "Salary Payment",
        "QueueTimeOutURL": "YOUR_B2C_CALLBACK_URL",
        "ResultURL": "YOUR_B2C_CALLBACK_URL",
        "Occasion": "Salary"
    }
    response = requests.post(b2c_url, json=payload, headers=headers)
    print("B2C Response:")
    print(response.json())

# C2B Operation
def perform_c2b_transaction():
    payload = {
        "ShortCode": shortcode,
        "CommandID": "CustomerPayBillOnline",
        "Amount": "100",  # Replace with the amount
        "Msisdn": "PHONE_NUMBER",  # Replace with the customer's phone number
        "BillRefNumber": "123456"  # Replace with a unique reference number
    }
    response = requests.post(c2b_url, json=payload, headers=headers)
    print("C2B Response:")
    print(response.json())

# Call the B2C and C2B functions to perform the transactions
perform_b2c_transaction()
perform_c2b_transaction()
