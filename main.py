import requests
import csv
import json
import os
from dotenv import load_dotenv

load_dotenv()  # Load API key and base URL from .env file

API_KEY = os.getenv("API_KEY")
BASE_URL = os.getenv("BASE_URL")

def process_csv_data(csv_file):
    with open(csv_file, "r") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            email = row["email"]
            f_name = row["f_name"]
            l_name = row["l_name"]  # Replace with actual column names

            payload = json.dumps({
                "email": email,
                "attributes": {
                    "FIRSTNAME": f_name,
                    "LASTNAME": l_name
                },
                # ... other fields as needed
            })

            try:
                response = requests.post(
                    f"{BASE_URL}/v3/contacts",
                    headers={
                        'Content-Type': 'application/json',
                        'Accept': 'application/json',
                        'api-key': API_KEY
                    },
                    data=payload
                )

                response.raise_for_status()  # Raise an exception for non-200 status codes

                print(f"API request successful for email: {email}")
                with open("api_log.txt", "a") as logfile:
                    logfile.write(f"Email: {email}\nData: {payload}\nResponse: {response.text}\n====================\n")

            except requests.exceptions.RequestException as e:
                print(f"API request failed for email: {email}. Error: {e}")

if __name__ == "__main__":
    csv_file = "data.csv"  # Replace with your CSV file path
    process_csv_data(csv_file)
