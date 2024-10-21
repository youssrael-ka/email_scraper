from googleapiclient.discovery import build

class EmailQuery:
    def __init__(self, service):
        self.service = service

    def query_last_ten_emails(self):
        try:
            # Limit the results to the last 10 emails
            results = self.service.users().messages().list(userId='me', maxResults=10).execute()
            messages = results.get('messages', [])
            email_list = []

            for msg in messages:
                msg = self.service.users().messages().get(userId='me', id=msg['id']).execute()
                headers = msg['payload']['headers']
                subject = None
                for header in headers:
                    if header['name'] == 'Subject':
                        subject = header['value']
                # Check if the subject is "info nouvelles commandes"
                if  "info nouvelles commandes" in subject:
                    email_list.append(msg)
            return email_list
        except Exception as e:
            print(f"An error occurred while querying: {e}")
            return []
