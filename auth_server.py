import os
import requests
import webbrowser
from flask import Flask, request
from dotenv import load_dotenv

# Load client_id and client_secret from .env
load_dotenv()

CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")
REDIRECT_URI = "http://localhost:5000/callback"

# ✅ Correct AUTH_URL with required scopes
AUTH_URL = (
    "https://www.linkedin.com/oauth/v2/authorization"
    f"?response_type=code"
    f"&client_id={CLIENT_ID}"
    f"&redirect_uri={REDIRECT_URI}"
    f"&scope=r_liteprofile%20r_emailaddress%20w_member_social"
)

TOKEN_URL = "https://www.linkedin.com/oauth/v2/accessToken"

app = Flask(__name__)

@app.route("/")
def home():
    return f'<a href="{AUTH_URL}">Login with LinkedIn</a>'

@app.route("/callback")
def callback():
    code = request.args.get("code")
    if not code:
        return "❌ No code received in callback."

    # Exchange code for access token
    response = requests.post(TOKEN_URL, data={
        "grant_type": "authorization_code",
        "code": code,
        "redirect_uri": REDIRECT_URI,
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET
    }, headers={"Content-Type": "application/x-www-form-urlencoded"})

    access_token = response.json().get("access_token")

    if access_token:
        # Save token to .env
        with open(".env", "a") as f:
            f.write(f"\nACCESS_TOKEN={access_token}\n")
        return "✅ Access token saved! You can now close this window."
    else:
        return f"❌ Failed to get access token: {response.text}"

if __name__ == "__main__":
    print("Starting auth server at http://localhost:5000 ...")
    webbrowser.open("http://localhost:5000")
    app.run(port=5000)
