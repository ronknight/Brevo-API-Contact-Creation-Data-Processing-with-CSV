# Brevo-API-Contact-Creation-Data-Processing-with-CSV

This file provides an overview of the Python program for processing CSV data and creating new contact with Brevo API.

## Project Description

This script takes a CSV file containing contact information and iterates through each record. It constructs a payload based on the data and sends a POST request to a specified API endpoint to create new contacts. The script utilizes the python-dotenv library to securely store API credentials from a .env file. Additionally, it logs successful API requests and sent data for future reference.

## Requirements

Python 3.x
Libraries:
requests
csv
python-dotenv

## Installation

Install the required libraries using pip:

```bash
pip install requests csv python-dotenv
```

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

The script will print messages indicating successful or failed API requests for each email address.
A file named api_log.txt will be created or appended to, containing details of successful API calls, including email address, sent data, and response.

## Additional Notes

This script assumes a specific API endpoint structure and payload format. You may need to modify it based on your specific API.
Error handling is included for API requests, logging exceptions for debugging purposes.
