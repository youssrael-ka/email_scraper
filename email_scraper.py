from bs4 import BeautifulSoup
import base64
import re
import json

class EmailScraper:
    
    def __init__(self, email_message):
        self.email_message = email_message

    def scrape_email_content(self):
        try:
            body = None
            if 'parts' in self.email_message['payload']:
                for part in self.email_message['payload']['parts']:
                    if part['mimeType'] == 'text/html':
                        # Decode the HTML body and keep it as HTML
                        body = base64.urlsafe_b64decode(part['body']['data']).decode('utf-8')
                        break  # Stop as soon as we find the HTML part
            if body is None:
                body = "No HTML content available"
            # Use BeautifulSoup to parse the decoded HTML
            soup = BeautifulSoup(body, 'html.parser')
            event_th = soup.find('th', string='Evènement')
            entet = []
            dataReservation = []
            # Vérification si la balise <th> a été trouvée
            if event_th:
                # Sélection de la balise parente
                row_th = event_th.parent
                for col in row_th.find_all("th"):
                    entet.append(col.text)
                # print(entet)
                tableP = row_th.parent
                rows = tableP.find_all("tr")
                # Affichage de la balise parente
                # print(tableP)
                for row in rows[1:]:  # On commence à partir de l'index 1
                    index = 0
                    reservation = {}
                    for col in row.find_all("td"):
                        reservation[entet[index]]=col.text.strip().replace("\n", " ").replace("\t", " ")
                        index += 1
                        ##print(col.text)
                    dataReservation.append(reservation)
                return dataReservation
        except Exception as e:
            print(f"An error occurred while scraping email content: {e}")
            return None    

    """def scrape_email_content(self):
        try:
            email_data = self.email_message['payload']['parts'][0]['body']['data']
            decoded_data = base64.urlsafe_b64decode(email_data.encode('UTF-8')).decode('UTF-8')

            # Use BeautifulSoup to parse the decoded HTML
            soup = BeautifulSoup(decoded_data, 'html.parser')
            text_content = soup.get_text()

            return text_content.strip()
        except Exception as e:
            print(f"An error occurred while scraping email content: {e}")
            return None
    """
    """def query_emails(self, email_text):
        # Define regex patterns to extract the fields from the email
        patterns = {
            "event": r"Événement\s*:\s*(.*)",
            "session": r"Séance\s*:\s*([\d\/]{10}\s[\d:]{5})",
            "category": r"Prix\s*:\s*([^\d]+)",
            "price_per_seat": r"Prix\s*:\s*.*?(\d+,\d+|\d+\.\d{2})€",
            "total_seats": r"Places\s*:\s*(\d+)",
            "total_price": r"A payer par BilletReduc\s*:\s*(\d+,\d+|\d+\.\d{2})€",
            "name": r"Nom\s*:\s*([^\n]+)",
            "reference": r"Ref\s*:\s*([\w@]+)",
            "quota": r"Prise\s*/\s*Quota\s*Cat\s*:\s*(\d+)/(\d+)"
        }

        # Extract data using regex
        data = {}
        for key, pattern in patterns.items():
            match = re.search(pattern, email_text, re.MULTILINE)
            if match:
                data[key] = match.groups() if len(match.groups()) > 1 else match.group(1)

        # Convert numbers to proper formats
        data["price_per_seat"] = float(data.get("price_per_seat", "0").replace(',', '.'))
        data["total_price"] = float(data.get("total_price", "0").replace(',', '.'))
        data["total_seats"] = int(data.get("total_seats", "0"))

        # Process the quota to split taken and total
        if "quota" in data:
            data["quota"] = {
                "taken": int(data["quota"][0]),
                "total": int(data["quota"][1])
            }

        return data
        """
        
    def save_to_json(self, data, output_file='event_data.json'):
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
        print(f"Data has been written to {output_file}")
