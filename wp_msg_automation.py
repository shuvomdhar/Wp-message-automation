from twilio.rest import Client
from datetime import datetime
from dotenv import load_dotenv
import time
import os

load_dotenv()

account_sid = os.getenv("TWILIO_ACCOUNT_SID")
auth_token = os.getenv("TWILIO_AUTH_TOKEN")

client = Client(account_sid, auth_token)

def send_message(recipient_number, message_body):
    try:
        message = client.messages.create(
            from_='whatsapp:+14155238886',
            body=message_body,
            to=f'whatsapp:{recipient_number}'
        )
        print(f'Message sent to {recipient_number} at {datetime.now()} successfully')
    except Exception as e:
        print(f'Error sending message to {recipient_number}: {str(e)}')

name = input("Enter your name: ")
recipient_number = input("Enter the recipient's number with country code: ")
message_body = input("Enter the message body: ")

date_str = input("Enter the date (YYYY-MM-DD) to send the message: ")
time_str = input("Enter the time (HH:MM) to send the message: ")

schedule_datetime = datetime.strptime(f'{date_str} {time_str}', '%Y-%m-%d %H:%M')
current_datetime = datetime.now()

time_difference = schedule_datetime - current_datetime
delay_seconds = time_difference.total_seconds()

if delay_seconds <= 0:
    print("The specific time is in the past. Please enter a future date and time.")
else:
    print(f"Message scheduled to be sent to {name} at {schedule_datetime}.")

    time.sleep(delay_seconds)

    send_message(recipient_number, message_body)