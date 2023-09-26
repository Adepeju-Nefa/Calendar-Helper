import datetime
from google.oauth2 import service_account
from googleapiclient.discovery import build
import pytz
from twilio.rest import Client
import os.path


def get_google_calendar():
    scopes = ['https://www.googleapis.com/auth/calendar.readonly']
    creds_file = 'credentials.json'
    creds = service_account.Credentials.from_service_account_file(creds_file, scopes=scopes)
    service = build(''
                    'calendar',
                    'v3',
                    credentials=creds)
    return service


def get_events(service):
    est = pytz.timezone('America/Toronto')
    current_time_toronto = datetime.datetime.now(est)
    end_of_day = datetime.datetime(current_time_toronto.year, current_time_toronto.month, current_time_toronto.day, 23, 0, 0)

    try:
        events_result = service.events().list(
            calendarId='primary',
            timeMin=current_time_toronto.isoformat(),
            timeMax=end_of_day.isoformat(),
            singleEvents=True,
            orderBy='startTime'
        ).execute()

        events = events_result.get('items', [])
        return events
    except Exception as e:
        print(f"Error accessing Google Calendar API: {str(e)}")



def send_schedule_text(schedule):
    account_sid = os.environ['TWILIO_ACCOUNT_SID']
    auth_token = os.environ['TWILIO_AUTH_TOKEN']
    twilio_phone_number = os.environ['TWILIO_PHONE_NUMBER']
    recepient_phone_number = os.environ['PHONE_NUMBER']



    print(account_sid)
    print('hi')

    client = Client(account_sid, auth_token)

    if not schedule:
        message = 'You have no events scheduled for today so take a break dear :)'

    else:
        message = 'Your schedule for today:\n'
        for event in schedule:
            start_time = event['start'].get('dateTime', event['start'].get('date'))
            end_time = event['end'].get('dateTime', event['end'].get('end'))
            event_summary = event['summary']
            message += f"{start_time} - {end_time}: {event_summary}\n"

    message = client.messages.create(body=message, from_=twilio_phone_number, to=recepient_phone_number)


def main():
    cal_service = get_google_calendar()
    schedule = get_events(cal_service)
    send_schedule_text(schedule)

    return


if __name__ == "__main__":
    main()