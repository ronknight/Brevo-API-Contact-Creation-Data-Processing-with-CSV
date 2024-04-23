<p><a target="_blank" href="https://app.eraser.io/workspace/QubUJbw5JUYWaFWjMIRj" id="edit-in-eraser-github-link"><img alt="Edit in Eraser" src="https://firebasestorage.googleapis.com/v0/b/second-petal-295822.appspot.com/o/images%2Fgithub%2FOpen%20in%20Eraser.svg?alt=media&amp;token=968381c8-a7e7-472a-8ed6-4a6626da5501"></a></p>

# Brevo-API-Contact-Creation-Data-Processing-with-CSV
This file provides an overview of the Python program for processing CSV data containing contact information and interacting with an API for contact management.

## Project Description
This script automates creating contacts in a CRM system by iterating through a CSV file and performing the following actions:

1. Checks for Existing Email: Before creating a new contact, the script verifies if the email address already exists in the system using a separate API call.
2. Creates New Contact (if not existing): If the email doesn't exist, the script constructs a JSON payload based on the data in the CSV file and sends a POST request to a specified API endpoint to create a new contact.
3. Secure Credentials and Logging: The script utilizes the python-dotenv library to securely store API credentials from a separate .env file. Additionally, it logs successful API requests with details and sent data for future reference, and logs errors encountered during processing.
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
pip install -r requirements.txt
```
Create a file named .env in the same directory as your script. Add the following lines, replacing  and  with your actual values:

```bash
API_KEY=<YOUR_API_KEY>
BASE_URL=<YOUR_BASE_URL>
```
## Usage
1. Update CSV Path: Modify the csv_file variable in the script with the path to your CSV file.
2. Ensure CSV Format: The CSV file should have column names matching the script's expectations (e.g., "email", "first_name", "last_name"). Refer to the Example CSV Format section for details.
Run the Script: Execute the script using:

```bash
python main.py
```
## Output
- The script will print messages indicating successful or failed API requests for each email address:
-- Existing email messages: "Email: {email} already exists."
-- New contact creation messages: "Email: {email} not found. Creating new contact..."
-- Error messages for any issues encountered during processing.
- A file named api_log.txt will be created or appended to, containing details of successful API calls, including email address, sent data, and response. A separate file named api_error_log.txt will log errors encountered.
## Additional Notes
- This script assumes a specific API endpoint structure and payload format. You may need to modify it based on your specific API.
The script includes error handling for API requests, logging exceptions for debugging purposes. Additionally, informative error messages are provided for the user.
By default, the script uses the current date for startDate and endDate in the email existence check. You can modify the code to use a different date range if needed.
## Optional: Dynamic Date Generation
(Refer to comments in the provided Python code)

## License
This project is licensed under the MIT License (see LICENSE file for details).

## Example CSV Format
The CSV file should have the following columns:

- email (string): The email address of the contact (required).
- first_name (string): The first name of the contact.
- last_name (string): The last name of the contact.
- sic (string): The contact's Standard Industrial Classification code (optional).
- company (string): The contact's company name (optional).
- state (string): The contact's state (optional).
- industry (string): The contact's industry (optional).
- country (string): The contact's country (optional).
- city (string): The contact's city (optional).
- zip (string): The contact's zip code (optional).
- county (string): The contact's county (optional).
- id (string): The contact's ID (optional).
## Security Considerations
While storing API keys in a .env file improves security, refer to the documentation for your specific framework or deployment environment for any additional best practices.


<!-- eraser-additional-content -->
## Diagrams
<!-- eraser-additional-files -->
<a href="/README-Brevo API Contact Creation Data Processing with CSV-1.eraserdiagram" data-element-id="LjueM3pOSZslOxHtmEukW"><img src="/.eraser/QubUJbw5JUYWaFWjMIRj___3Jivg2tjMecMlrHwbIVIBR8f7U03___---diagram----b25973538bb6a044d3900b4fa9f5c081-Brevo-API-Contact-Creation-Data-Processing-with-CSV.png" alt="" data-element-id="LjueM3pOSZslOxHtmEukW" /></a>
<!-- end-eraser-additional-files -->
<!-- end-eraser-additional-content -->
<!--- Eraser file: https://app.eraser.io/workspace/QubUJbw5JUYWaFWjMIRj --->