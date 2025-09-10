import requests

# Your latest access token (paste from LinkedIn developer portal)
access_token = "AQVYb8YsT0HJOH99QeQS1mxFjcxOh6zRw0hFGfznoJlJvuGfkkkhf7-rzQPyaWtmc9d5RYnp34-h5k05RjaNEM28CNdL9jR4svf3MQSFDSJG1pNco5_g0Rak4JKHbL_ataqOWsqeOTkpSJCzWHbkImi_l_s9kY81v8hxkjliM5GDMTmxNteE5PjEnJw6SjZJjiKFVCIMar5ZVSktM_ZXRd9ocDwEpki6ulzpZW8lpikXsR_Eot2E7mJD-dsyYWoz6-Oi-RMWuDyaG3gjL9NMf1d7ukHDp12uX5AiDPRio_jH4THv4Gb4usEInTW8WCn7oo1kdkhwakwNUpg02jx9uRHIQubyRQ"

# LinkedIn API endpoint to fetch profile
url = "https://api.linkedin.com/v2/me"

# Headers with authorization
headers = {
    "Authorization": f"Bearer {access_token}",
    "Connection": "Keep-Alive",
    "X-Restli-Protocol-Version": "2.0.0"
}

# Make the request
response = requests.get(url, headers=headers)

# Print result
print("Status Code:", response.status_code)
print("Response JSON:", response.json())
