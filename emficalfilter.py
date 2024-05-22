from icalendar import Calendar
import requests

year = 24
# Download the 2024.ical file from the given URL
url = 'https://www.emfcamp.org/schedule/2022.ical'
response = requests.get(url)
with open('./2024.ical', 'wb') as file:
    file.write(response.content)

# Open the existing .ical file and parse it into a Calendar object
with open('./2024.ical', 'r') as file:
    cal = Calendar.from_ical(file.read())

# Create a new Calendar object for the filtered events
stage_cal = Calendar()
workshop_cal = Calendar()
nullsector_cal = Calendar()
# Iterate over the events in the existing calendar
for event in cal.walk('vevent'):
    # If the event's location contains "stage", add it to the filtered calendar
    if 'stage' in event.get('location', '').lower():
        stage_cal.add_component(event)
for event in cal.walk('vevent'):
    if 'workshop' in event.get('location', '').lower():
        workshop_cal.add_component(event)
for event in cal.walk('vevent'):
    if 'sector' in event.get('location', '').lower():
        nullsector_cal.add_component(event)
# Write the filtered calendar to a new .ical file
with open('stage.ical', 'wb') as file:
    file.write(stage_cal.to_ical())
with open('workshop.ical', 'wb') as file:
    file.write(workshop_cal.to_ical())
with open('nullsector.ical', 'wb') as file:
    file.write(nullsector_cal.to_ical())
