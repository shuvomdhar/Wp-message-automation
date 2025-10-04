# WhatsApp Message Scheduler

A Python script that schedules and sends WhatsApp messages at a specified date and time using the Twilio API.

## Features

- Schedule WhatsApp messages to be sent at a future date and time
- Interactive command-line interface for easy message scheduling
- Error handling for failed message delivery
- Validates that scheduled time is in the future

## Prerequisites

- Python 3.6 or higher
- A Twilio account with WhatsApp sandbox enabled
- Twilio Account SID and Auth Token

## Installation

1. Clone or download this repository

2. Install required dependencies:
```bash
pip install twilio python-dotenv
```

3. Create a `.env` file in the project root directory:
```env
TWILIO_ACCOUNT_SID=your_account_sid_here
TWILIO_AUTH_TOKEN=your_auth_token_here
```

## Configuration

### Getting Twilio Credentials

1. Sign up for a [Twilio account](https://www.twilio.com/try-twilio)
2. Navigate to your [Twilio Console](https://console.twilio.com/)
3. Copy your Account SID and Auth Token
4. Set up the [Twilio WhatsApp Sandbox](https://www.twilio.com/console/sms/whatsapp/sandbox)
5. Follow the instructions to connect your WhatsApp number to the sandbox

### Environment Variables

The script requires the following environment variables in your `.env` file:

- `TWILIO_ACCOUNT_SID`: Your Twilio Account SID
- `TWILIO_AUTH_TOKEN`: Your Twilio Auth Token

## Usage

Run the script:
```bash
python script_name.py
```

The script will prompt you for the following information:

1. **Name**: Recipient's name (for display purposes)
2. **Recipient's Number**: Phone number with country code (e.g., +1234567890)
3. **Message Body**: The text message you want to send
4. **Date**: Date to send the message (format: YYYY-MM-DD)
5. **Time**: Time to send the message (format: HH:MM in 24-hour format)

### Example

```
Enter your name: John
Enter the recipient's number with country code: +1234567890
Enter the message body: Hello! This is a scheduled message.
Enter the date (YYYY-MM-DD) to send the message: 2025-10-05
Enter the time (HH:MM) to send the message: 14:30
```

## How It Works

1. The script loads Twilio credentials from the `.env` file
2. It prompts the user for recipient information and message details
3. It calculates the time difference between now and the scheduled time
4. The script waits (sleeps) until the scheduled time arrives
5. Once the time is reached, it sends the WhatsApp message via Twilio API

## Important Notes

- **Twilio Sandbox Limitation**: The Twilio WhatsApp sandbox sender number (+14155238886) is used by default. For production use, you'll need to register your own WhatsApp Business number with Twilio.
- **Recipients Must Opt-in**: Recipients must first join your WhatsApp sandbox by sending a specific code to the Twilio number.
- **Script Must Stay Running**: The script must remain running until the scheduled time arrives. If you close the script, the message will not be sent.
- **Time Zone**: The script uses your local system time. Ensure your system clock is set correctly.

## Error Handling

The script includes error handling for:
- Failed message delivery attempts
- Invalid past dates/times (will display an error message)
- Twilio API errors

## Limitations

- The script must remain running until the message is sent
- Only supports scheduling one message per execution
- Uses local system time (no timezone conversion)
- Not suitable for long-term scheduling (consider using a task scheduler like cron for that)

## Future Improvements

Potential enhancements could include:
- Multiple message scheduling
- Database storage for scheduled messages
- Background process/daemon mode
- Timezone support
- Message templates
- Recurring messages

## License

This project is open-source and available for educational use. Feel free to modify and distribute according to your needs.

## Support

For issues related to:
- **Twilio API**: Check the [Twilio Documentation](https://www.twilio.com/docs)
- **WhatsApp Business API**: Visit [Twilio WhatsApp Documentation](https://www.twilio.com/docs/whatsapp)

## Disclaimer

This script is for educational purposes. Ensure you comply with Twilio's terms of service and WhatsApp's policies when sending messages.