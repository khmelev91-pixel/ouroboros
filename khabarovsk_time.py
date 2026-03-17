#!/usr/bin/env python3
"""
Script to show the current time in Khabarovsk.
"""
import datetime
try:
    from zoneinfo import ZoneInfo
except ImportError:
    # Fallback for older Python versions (though we are on 3.12)
    try:
        import pytz
        ZoneInfo = lambda tz: pytz.timezone(tz)
    except ImportError:
        print("Error: Neither zoneinfo nor pytz is available.")
        print("Install pytz with: pip install pytz")
        exit(1)

def main():
    # Get current time in UTC
    utc_now = datetime.datetime.now(datetime.timezone.utc)
    # Convert to Khabarovsk time (UTC+10)
    khabarovsk_tz = ZoneInfo('Asia/Vladivostok')  # Khabarovsk uses Vladivostok time zone
    khabarovsk_now = utc_now.astimezone(khabarovsk_tz)
    # Format and print
    print(f"Current time in Khabarovsk: {khabarovsk_now.strftime('%Y-%m-%d %H:%M:%S %Z%z')}")

if __name__ == "__main__":
    main()