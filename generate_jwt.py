import jwt
import time
import json
from datetime import datetime, timedelta

# Replace these with your own values
ISSUER_ID = "YOUR_ISSUER_ID"
KEY_ID = "YOUR_KEY_ID"
KEY_FILE = "AuthKey_YOUR_KEY_ID.p8"

# Load the private key
with open(KEY_FILE, 'r') as f:
    PRIVATE_KEY = f.read()

# Prepare the payload
payload = {
    "iss": ISSUER_ID,
    "exp": int((datetime.now() + timedelta(minutes=20)).timestamp()),
    "aud": "appstoreconnect-v1"
}

# Generate the JWT
token = jwt.encode(payload, PRIVATE_KEY, algorithm='ES256', headers={'kid': KEY_ID})

print(token)
