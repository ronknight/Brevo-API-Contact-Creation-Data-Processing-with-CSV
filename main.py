import requests
import csv
import json
import os
from datetime import date
from dotenv import load_dotenv

load_dotenv()  # Load API key and base URL from .env file

API_KEY = os.getenv("API_KEY")
BASE_URL = os.getenv("BASE_URL")
today = date.today().strftime("%Y-%m-%d")  # Format date as YYYY-MM-DD

def check_existing_email(email):
    url = f"{BASE_URL}/v3/contacts/{email}?startDate={today}&endDate={today}"
    headers = {
        'Accept': 'application/json',
        'api-key': API_KEY
    }

    try:
        response = requests.get(url, headers=headers)

        # Check for successful response (200) indicating existing contact
        if response.status_code == 200:
            if response.json():
                print(f"Email: {email} already exists.")
                return True  # Indicate email exists
            else:
                # Handle unexpected empty response for 200 (not necessarily an error)
                print(f"Unexpected empty response for email: {email}")
                return False  # Indicate check failed, consider logging the issue

        # Check for specific error codes
        elif response.status_code == 400:
            print(f"Error checking email: {email}. Bad Request (400).")
            return False  # Indicate check failed due to bad request

        elif response.status_code == 404:
            print(f"Email: {email} not found. Creating new contact...")
            return False  # Indicate email not found (new contact needed)

        # Handle other unexpected status codes
        else:
            print(f"Error checking email: {email}. Unexpected status code: {response.status_code}")
            return False  # Indicate check failed due to unexpected error

    except requests.exceptions.RequestException as e:
        print(f"Error checking email: {email}. Error: {e}")
        return False  # Indicate check failed due to request exception

def process_csv_data(csv_file):
    existing_emails = set()  # Create a set to store existing emails

    with open(csv_file, "r") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            email = row["email"]
            f_name = row["f_name"]
            l_name = row["l_name"]

            # Check if email already found in the set
            if email not in existing_emails:
                if not check_existing_email(email):
                    existing_emails.add(email)  # Add email to existing list after confirmation
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