from icalendar import Calendar
import requests

year = 24
# Download the 2024.ical file from the given URL
url = 'https://www.emfcamp.org/schedule/2024.ical'
response = requests.get(url)
with open('./2024.ical', 'wb') as file:
    file.write(response.content)

# Open the existing .ical file and parse it into a Calendar object
with open('./2024.ical', 'r') as file:
    cal = Calendar.from_ical(file.read())

# Print to a csv the list of different locations, do not have overlap, 
# and are not empty
locations = set()
for event in cal.walk('vevent'):
    location = event.get('location', '')
    if location:
        locations.add(location)
locations = list(locations)
locations.sort()
with open('./locations.csv', 'w') as file:
    file.write('\n'.join(locations))