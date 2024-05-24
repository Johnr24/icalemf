from icalendar import Calendar
import requests
import csv
# Download the 2024.ical file from the given URL
url = 'https://www.emfcamp.org/schedule/2024.ical'
response = requests.get(url)
with open('./2024.ical', 'wb') as file:
    file.write(response.content)

# Fetch the village names from the API
url = 'https://www.emfcamp.org/api/villages'
response = requests.get(url)
village_names = [village['name'] for village in response.json()]

# Open the existing .ical file and parse it into a Calendar object
with open('./2024.ical', 'r') as file:
    cal = Calendar.from_ical(file.read())

# Create a set for the village locations
village_locations = set()

# Iterate over the events in the calendar
for event in cal.walk('vevent'):
    location = event.get('location', '')
    # If the location is a village name, add it to the set
    if location in village_names:
        village_locations.add(location)

# Write the village locations to a new CSV file
with open('./village_locations.csv', 'w') as file:
    writer = csv.writer(file)
    for location in sorted(village_locations):
        writer.writerow([location])


# Read locations from the CSV file
with open('locations.csv', 'r') as file:
    reader = csv.reader(file)
    locations = [row[0] for row in reader]

# Remove the village locations from the locations list
locations = [location for location in locations if location not in village_locations]

# Write the remaining locations back to the CSV file
with open('locations.csv', 'w') as file:
    writer = csv.writer(file)
    for location in locations:
        writer.writerow([location])