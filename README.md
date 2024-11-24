# Product Availability Checker with Twilio

This Python script monitors the availability of specified products on a website and sends an SMS notification using Twilio when the product is available.

## Features
- Sends HTTP requests to a specific endpoint to check product availability.
- Analyzes the response to determine product stock status.
- Sends SMS notifications when a product becomes available.

## Prerequisites
1. Python 3.8 or higher.
2. Twilio account with valid credentials.
3. `requests` and `twilio` Python packages installed.

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/product-availability-checker-twilio.git
   cd product-availability-checker-twilio

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   
3. Create a config.json file in the root directory with the following structure:
   ```bash
   {
       "account_sid": "your_twilio_account_sid",
       "auth_token": "your_twilio_auth_token",
       "twilio_phone_number": "your_twilio_phone_number",
       "your_phone_number": "your_personal_phone_number"
   }

## Usage
   ```bash
   python main.py



