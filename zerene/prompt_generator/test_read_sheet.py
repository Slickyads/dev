#!/usr/bin/env python3
"""
Test script to read Google Sheet data.

You'll need to:
1. Enable Google Sheets API in Google Cloud Console
2. Create a service account and download the JSON key
3. Set environment variable: GOOGLE_APPLICATION_CREDENTIALS=path/to/service-account.json
4. Run: pip install google-api-python-client google-auth-httplib2 google-auth-oauthlib
"""

import os
import sys

try:
    from google.auth.transport.requests import Request
    from google.oauth2 import service_account
    from googleapiclient.discovery import build
    from googleapiclient.errors import HttpError
    print("Google API libraries available")
except ImportError as e:
    print(f"Missing Google API libraries: {e}")
    print("Install with: pip install google-api-python-client google-auth")
    sys.exit(1)

# Sheet ID from .env
SHEET_ID = "1yAJ1LwDG3KI_aAQGKNnu2adc0SzSUdZI2EAPK4aWdRQ"
RANGE = "Prompts!A:Z"

def test_read_sheet():
    """Read data from Google Sheet"""
    try:
        # Check for credentials
        creds_path = os.getenv("GOOGLE_APPLICATION_CREDENTIALS")
        if not creds_path:
            print("❌ GOOGLE_APPLICATION_CREDENTIALS env var not set")
            print("Please download a Google Cloud service account key and set this env var")
            return False

        if not os.path.exists(creds_path):
            print(f"❌ Credentials file not found: {creds_path}")
            return False

        print(f"✅ Found credentials: {creds_path}")

        # Authenticate with service account
        print("🔐 Authenticating with Google Sheets API...")
        scopes = ['https://www.googleapis.com/auth/spreadsheets.readonly']
        credentials = service_account.Credentials.from_service_account_file(
            creds_path, scopes=scopes
        )

        # Build the Sheets API client
        service = build('sheets', 'v4', credentials=credentials)
        sheet = service.spreadsheets()

        # Fetch sheet metadata
        print("📊 Fetching sheet metadata...")
        spreadsheet = sheet.get(spreadsheetId=SHEET_ID).execute()
        print(f"✅ Sheet name: {spreadsheet.get('properties', {}).get('title', 'Unknown')}")

        # Try to read data (might fail if no data exists)
        try:
            print(f"📖 Reading range: {RANGE}")
            result = sheet.values().get(
                spreadsheetId=SHEET_ID,
                range=RANGE
            ).execute()

            rows = result.get('values', [])
            if rows:
                print(f"✅ Found {len(rows)} rows")
                print(f"📝 First few rows:")
                for i, row in enumerate(rows[:3]):
                    print(f"   Row {i+1}: {row}")
                return True
            else:
                print("⚠️  No data found in sheet")
                print("This is normal - the workflow writes data when generating prompts")
                print("✅ Authentication successful, but sheet is empty")
                return True

        except HttpError as e:
            print(f"❌ API Error: {e}")
            return False

    except Exception as e:
        print(f"❌ Error: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    print("🔍 Testing Google Sheets read access")
    print(f"Sheet ID: {SHEET_ID}")
    print("-" * 50)

    success = test_read_sheet()

    if success:
        print("\n✅ Test successful - sheet access confirmed")
    else:
        print("\n❌ Test failed")
        sys.exit(1)