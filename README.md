# Gmail Email Scraper

This project is designed to authenticate with Gmail using the Gmail API, query specific emails (e.g., "info nouvelles commandes"), and extract relevant information such as event details, prices, and session times. The data is then saved into a JSON file for further processing or reporting.

## Features

- **OAuth 2.0 Gmail Authentication**: Securely authenticate with Gmail and request access to the inbox.
- **Query Emails**: Search the inbox for specific emails based on a subject.
- **Scrape Email Content**: Extract structured data (event, session, price, etc.) from HTML emails.
- **Save to JSON**: Parsed data is stored in a structured JSON file for further analysis.

---

## Setup

### Prerequisites

1. **Python**: Make sure you have Python 3.x installed on your system.
   
2. **Google API Credentials**:
    - Create a project in the [Google Developers Console](https://console.developers.google.com/).
    - Enable the **Gmail API** for your project.
    - Create OAuth 2.0 credentials and download the `credentials.json` file.
    - Place the `credentials.json` file in the root directory of your project.

3. **Required Python Libraries**: Install the necessary dependencies by running the following command:
   ```bash
   pip install google-auth google-auth-oauthlib google-auth-httplib2 google-api-python-client

## Installation

1. Clone the repository or download the project files.
   ```bash
   git clone https://github.com/your-username/gmail-email-scraper.git
   cd gmail-email-scraper
2. Install the required Python libraries (as mentioned in the prerequisites).
   ```bash
   pip install google-auth google-auth-oauthlib google-auth-httplib2 google-api-python-client
3. Place the credentials.json file (downloaded from Google API) in the root of the project directory.
   
---

### Usage

### Step 1: Authenticate with Gmail

The first time you run the project, it will initiate OAuth 2.0 authentication. Follow these steps:

1. Run the `main.py` file to start the process:
   ```bash
   python main.py
2. A browser window will open asking you to log into your Gmail account and authorize access.

3. Once authorized, a token.json file will be created, saving your credentials for future use. This avoids repeated logins for subsequent runs.

### Step 2: Query and Scrape Emails

- After authenticating, the script will query the last 5 emails in your inbox. It will only process emails with the subject "info nouvelles commandes".

- For each relevant email, it scrapes event details, session times, prices, and more, then saves this data to a parsed_emails.json file.

### Step 3: Check the Output

After the script completes:

- The parsed_emails.json file will contain all extracted information in JSON format. This file can be opened and analyzed in any text editor or integrated into a larger workflow.

### File Structure

📁 gmail-email-scraper
- authentication.py        # Handles Gmail OAuth authentication
- email_query.py           # Queries emails from the Gmail inbox
- email_scraper.py         # Scrapes relevant information from the email body
- main.py                  # Main script to coordinate authentication, querying, and scraping
- credentials.json         # Your Gmail API credentials file (do not share)
- parsed_emails.json       # Output file containing parsed email data (auto-generated)

---

### Troubleshooting

- Authentication Issues: If the browser does not open during the first authentication, check your Python environment and ensure that all required libraries are installed.

- Token Expiry: If your token expires or becomes invalid, simply delete the token.json file and run the script again. This will prompt a new login.

