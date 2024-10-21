import json
from authentication import GmailAuth
from email_query import EmailQuery
from email_scraper import EmailScraper

def save_to_json(data, filename='parsed_emails.json'):
    #"""Saves the provided data to a JSON file."""

    try:
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
        print(f"Data successfully written to {filename}")
    except Exception as e:
        print(f"An error occurred while saving to JSON: {e}")

def main():
    print("Starting Gmail authentication...")
    
    # Authenticate Gmail API
    gmail_auth = GmailAuth()
    try:
        service = gmail_auth.authenticate()
        print("Authentication successful.")
    except Exception as e:
        print(f"Authentication failed: {e}")
        return

    # Query the last 10 emails
    print("Querying the last 10 emails...")
    email_query = EmailQuery(service)
    emails = email_query.query_last_ten_emails()

    if emails:
        print(f"Found {len(emails)} emails.")
        parsed_emails = []

        for email in emails:
            print(f"Processing email ID: {email['id']}")
            scraper = EmailScraper(email)
            scraped_data = scraper.scrape_email_content()

            if scraped_data:
                parsed_email = {
                    "email_id": email['id'],
                    "snippet": email['snippet'],
                    "content": scraped_data  # Directly saving the extracted data
                }
                parsed_emails.append(parsed_email)

        # Save the parsed results to a JSON file
        save_to_json(parsed_emails)

    else:
        print("No emails found.")

if __name__ == "__main__":
    main()
