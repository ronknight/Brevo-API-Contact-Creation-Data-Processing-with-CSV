import requests
import csv
import json
import os
from dotenv import load_dotenv

from datetime import date, datetime  # Import both date and datetime


load_dotenv()  # Load API key and base URL from .env file

API_KEY = os.getenv("API_KEY")
BASE_URL = os.getenv("BASE_URL")
today = date.today().strftime("%Y-%m-%d")  # Format date as YYYY-MM-DD

def check_existing_email(email):
    # Construct the URL for checking existing contact
    url = f"{BASE_URL}/v3/contacts/{email}?startDate={today}&endDate={today}"
    headers = {
        'Accept': 'application/json',
        'api-key': API_KEY
    }

    try:
        response = requests.get(url, headers=headers)

        # Check if the response is successful
        if response.status_code == 200:
            print(f"API request successful for email: {email}")
            log_error(email, f"Contact already exist: {response.text}")

            return True
        else:
            print(f"Contact doesn't exist: {email}")
            log_error(email, f"API request failed: {response.text}")
            return False

    except requests.exceptions.RequestException as e:
        print(f"Request exception for email: {email}, Error: {e}")
        return False

def process_csv_data(csv_file):
    existing_emails = set()  # Create a set to store existing emails

    with open(csv_file, "r") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            email = row["email"]
            f_name = row["f_name"]
            l_name = row["l_name"]
            sic = row["sic"]
            company = row["company"]
            title = row["title"]
            state = row["state"]
            industry = row["industry"]
            country = row["country"]
            city = row["city"]
            zip = row["zip"]            
            county = row["county"]
            id = row["id"]

            # Check if email already found in the set
            if email not in existing_emails:
                if not check_existing_email(email):
                    existing_emails.add(email)  # Add email to existing list after confirmation
                    payload = json.dumps({
                        "email": email,
                        "attributes": {
                            "FIRSTNAME": f_name,
                            "LASTNAME": l_name,
                            "SIC": sic,
                            "COMPANY": company,
                            "TITLE": title,
                            "STATE": state,
                            "INDUSTRY": industry,
                            "COUNTRY": country,
                            "CITY": city,
                            "ZIP": zip,
                            "COUNTY": county,
                            "ID": id

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
                            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                            logfile.write(f"{timestamp} - Email: {email}\tData: {payload}\tResponse: {response.text}\n====================\n")

                    except requests.exceptions.RequestException as e:
                        log_error(email, f"API request failed: {e}")

def log_error(email, error_message):
    with open("api_error_log.txt", "a") as error_log:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        error_log.write(f"{timestamp} - Email: {email}\tError: {error_message}\n====================\n")

if __name__ == "__main__":
    csv_file = "data.csv"  # Replace with your CSV file path
    process_csv_data(csv_file)
