from __future__ import print_function

import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

import base64
from email.message import EmailMessage
from email.mime.text import MIMEText
import google.auth

from radar import Radar
from db import Db

from datetime import date

import application

from application import email


# If modifying these scopes, delete the file token.json.
SCOPES = ['https://mail.google.com/']
    

def main(Body):
    """Shows basic usage of the Gmail API.
    Lists the user's Gmail labels.
    """
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    try:
        # Call the Gmail API
        service = build('gmail', 'v1', credentials=creds)
        results = service.users().labels().list(userId='me').execute()
        labels = results.get('labels', [])

        gmail_send_message(service, Body)

    except HttpError as error:
        # TODO(developer) - Handle errors from gmail API.
        print(f'An error occurred: {error}')

def gmail_send_message(service, Body):
    """Create and send an email message
    Print the returned  message id
    Returns: Message object, including message id

    Load pre-authorized user credentials from the environment.
    TODO(developer) - See https://developers.google.com/identity
    for guides on implementing OAuth2 for the application.
    """

    EmailList = Db.getSubs()
    RadarList = Radar.get()

    EmailContent = ""
    Header = "<h1>Worldometer API</h1>"
    Body
    Footer = "<h2>Goodbye</h2>"

    for Email in EmailList:
        try:

            EmailContent = (Header + Body + Footer)

            message = MIMEText(EmailContent, 'html')

            message['To'] = application.email
            message['From'] = 'bbzwtest@gmail.com'
            message['Subject'] = 'Worldometer API'

            # encoded message
            encoded_message = base64.urlsafe_b64encode(message.as_bytes()) \
                .decode()

            create_message = {
                'raw': encoded_message
            }
            # pylint: disable=E1101
            send_message = (service.users().messages().send
                            (userId="me", body=create_message).execute())
            print(F'Message Id: {send_message["id"]}')
        except HttpError as error:
            print(F'An error occurred: {error}')
            send_message = None
    return send_message

if __name__ == '__main__':
    main()