import os
import boto3
import json
from datetime import datetime

from_email = "sender@gmail.com"
# config_set_name = os.environ["SES_CONFIG_SET_NAME"]
client = boto3.client('ses')

def send_mail(error_code, subject, message):
    body_html = f"""
            <html>
                <head>
                    <meta charset="utf-8">
                    <title>SES Mail</title>
                    <style>
                      
                    </style>
                </head>
                 <body>
                      <h1>Hello SES</h1>
                </body>
                </html>
                    """

    email_message = {
        'Body': {
            'Html': {
                'Charset': 'utf-8',
                'Data': body_html,
            },
        },
        'Subject': {
            'Charset': 'utf-8',
            'Data': "Hello from AWS SES",
        },
    }

    ses_response = client.send_email(
        Destination={
            'ToAddresses': ['receiver@gmail.com'],
        },
        Message=email_message,
        Source=from_email
        # ConfigurationSetName=config_set_name,
    )

    print(f"ses response id received: {ses_response['MessageId']}.")
    return ses_response
