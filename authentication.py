from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

class GmailAuth:
    SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']

    def __init__(self, creds_file='credentials.json', token_file='token.json'):
        self.creds_file = creds_file
        self.token_file = token_file
        self.creds = None

    def authenticate(self):
        try:
            self.creds = Credentials.from_authorized_user_file(self.token_file, self.SCOPES)
        except FileNotFoundError:
            flow = InstalledAppFlow.from_client_secrets_file(self.creds_file, self.SCOPES)
            self.creds = flow.run_local_server(port=0)
            with open(self.token_file, 'w') as token:
                token.write(self.creds.to_json())

        service = build('gmail', 'v1', credentials=self.creds)
        return service
