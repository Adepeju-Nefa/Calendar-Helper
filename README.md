<h1> Calendar Event Notifier </h1>
<p>The Calendar Event Notifier is a Python script that fetches events from your Google Calendar and sends you a text message with your schedule for the day. It uses the Google Calendar API to retrieve events and the Twilio API to send text messages.
</p>

<h2>Features</h2>
<p>
Fetches events from your Google Calendar for the current day.
Sends a text message with your schedule to a specified recipient.
</p>

<h2> Prerequisites </h2>
Before using this script, make sure you have the following:
<ul>
<li>Google Cloud Platform project with the Google Calendar API enabled.</li>
<li>Service account credentials JSON file for the Google Calendar API.</li>
<li>Twilio account with an Account SID and Auth Token.</li>
<li>A Twilio phone number.</li>
<li>Python 3 installed on your machine.</li>
</ul>

<h2>Setup</h2>

<ol>
    <li>
    Clone this repository to your local machine:
  
  <code> git clone https://github.com/Adepeju-Nefa/calendar-helper.git </code>
    </li>
    <li>
    Navigate to the project directory:
    
  <code> cd calendar-helper </code>
    </li>
    <li>
    Install the required Python packages:
    
  <code> pip install -r requirements.txt
    </code>
    </li>
    <li>
    Configure the following environment variables:
    <ol>
        <li>TWILIO_ACCOUNT_SID: Your Twilio Account SID.</li>
        <li>TWILIO_AUTH_TOKEN: Your Twilio Auth Token.</li>
        <li>TWILIO_PHONE_NUMBER: Your Twilio phone number.</li>
        <li>RECIPIENT_PHONE_NUMBER: The recipient's phone number to receive the text message.</li>
    </ol>
    </li>
    <li>
    Place your Google Calendar API service account credentials JSON file in the project directory and name it credentials.json.
    </li>
</ol>


<h2>Usage</h2>
To use the Calendar Event Notifier:
<ul>
    <li>
    Run the script:
    </li>
    <code> python calendar_event_notifier.py</code>

   <p>The script will fetch your calendar events for the current day and send a text message with your schedule to the specified recipient.</p> 

</ul>
