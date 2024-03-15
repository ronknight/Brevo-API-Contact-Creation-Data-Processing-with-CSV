# Brevo-API-Contact-Creation-Data-Processing-with-CSV

This file provides an overview of the Python program for processing CSV data and interacting with an API for contact management.

## Project Description

This script takes a CSV file containing contact information and iterates through each record. It performs the following actions:

1. Checks for Existing Email: Before creating a new contact, the script verifies if the email address already exists in the system using a separate API call.
2. Creates New Contact (if not existing): If the email doesn't exist, the script constructs a payload based on the data and sends a POST request to a specified API endpoint to create a new contact.
3. Secure Credentials and Logging: The script utilizes the python-dotenv library to securely store API credentials from a .env file. Additionally, it logs successful API requests and sent data for future reference.

## Requirements

Python 3.x
Libraries:
- requests
- csv
- python-dotenv
- datetime (optional for dynamic date generation)

## Installation

Install the required libraries using pip:

```bash
pip install requests csv python-dotenv
```
(If using dynamic date generation, also install datetime: pip install datetime)
Use code with caution.

Create a file named .env in the same directory as your script. Add the following lines, replacing <YOUR_API_KEY> and <YOUR_BASE_URL> with your actual values:

```bash
API_KEY=<YOUR_API_KEY>
BASE_URL=<YOUR_BASE_URL>
```

## Usage

Update the csv_file variable in the script with the path to your CSV file.

Ensure the CSV file has appropriate column names (e.g., "email", "first_name", "last_name") that match the code.

Run the script:

```bash
python main.py
```
Use code with caution.

## Output

- The script will print messages indicating successful or failed API requests for each email address.
-- Existing email messages: "Email: {email} already exists."
-- New contact creation messages: "Email: {email} not found. Creating new contact..."
-- Error messages for any issues.
- A file named api_log.txt will be created or appended to, containing details of successful API calls, including email address, sent data, and response.

## Additional Notes

- This script assumes a specific API endpoint structure and payload format. You may need to modify it based on your specific API.
- Error handling is included for API requests, logging exceptions for debugging purposes.
- By default, the script uses the current date for startDate and endDate in the email existence check. You can modify the code to use a different date range if needed.

- Optional: Dynamic Date Generation

The script can be modified to dynamically generate the current date for startDate and endDate in the email existence check. This requires adding the datetime library and updating the code accordingly (refer to the comments in the provided Python code).