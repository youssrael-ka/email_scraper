from bs4 import BeautifulSoup
import base64
import json

class EmailScraper:
    
    def __init__(self, email_message):
        # Initialize the EmailScraper with the email message
        self.email_message = email_message

    def scrape_email_content(self):
        """Extract reservation data from the HTML content of the email."""
        try:
            body = None
            # Check if the email message contains parts in the payload
            if 'parts' in self.email_message['payload']:
                # Iterate through each part of the email
                for part in self.email_message['payload']['parts']:
                    # Look for the part that contains HTML content
                    if part['mimeType'] == 'text/html':
                        # Decode the base64 encoded HTML body
                        body = base64.urlsafe_b64decode(part['body']['data']).decode('utf-8')
                        break
            # If no HTML content was found, set a default message        
            if body is None:
                body = "No HTML content available"
            # Use BeautifulSoup to parse the decoded HTML
            soup = BeautifulSoup(body, 'html.parser')
            # Find the table header cell that contains the text 'Evènement'
            event_th = soup.find('th', string='Evènement')
            entet = []
            dataReservation = []
            # Check if the header cell was found
            if event_th:
                # Get the parent row of the found header cell
                row_th = event_th.parent
                for col in row_th.find_all("th"):
                    entet.append(col.text)
                # Find the parent table of the header row then put all rows in the table    
                tableP = row_th.parent
                rows = tableP.find_all("tr")
                
                # Iterate over each row starting from the second one (index 1)
                for row in rows[1:]:
                    index = 0
                    reservation = {}

                    # Find all data cells in the current row
                    for col in row.find_all("td"):
                        reservation[entet[index]]=col.text.strip().replace("\n", " ").replace("\t", " ")
                        index += 1
                    # Append the reservation dictionary to the list of data    
                    dataReservation.append(reservation)

                return dataReservation
            
        except Exception as e:
            # Print an error message if something goes wrong
            print(f"An error occurred while scraping email content: {e}")
            return None
        
    def save_to_json(self, data, output_file='event_data.json'):
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
        print(f"Data has been written to {output_file}")
