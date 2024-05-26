from icalendar import Calendar
import requests
import csv

# Read village names from the CSV file
with open('village_names.csv', 'r') as file:
    reader = csv.reader(file)
    village_names = [row[0] for row in reader]  # Flatten the list of lists
    village_names.append('Lockpicking Village Tent')
    village_names.append('Tekhnē-cal Village')

# Download the 2024.ical file from the given URL
url = 'https://www.emfcamp.org/schedule/2024.ical'
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
village_cal = Calendar()
youth_workshop_cal = Calendar()
sense_cal = Calendar()
main_bar_cal = Calendar()
Lounges_cal = Calendar()

# Iterate over the events in the existing calendar
for event in cal.walk('vevent'):
    # If the event's location contains "stage", add it to the filtered calendar
    if 'stage' in event.get('location', '').lower():
        stage_cal.add_component(event)
for event in cal.walk('vevent'):
    if 'workshop' in event.get('location', '').lower() and 'youth' not in event.get('location', '').lower():
        workshop_cal.add_component(event)
for event in cal.walk('vevent'):
    if 'sector' in event.get('location', '').lower():
        nullsector_cal.add_component(event)
# for villages, if the event's location contains the name of a village, add it to the filtered calendar the list can be found in the village_names.csv file however if the word "workshop" is in the location, it will not be added to the village calendar
for event in cal.walk('vevent'):
    if any(village in event.get('location', '').lower() for village in village_names) and 'workshop' not in event.get('location', '').lower():
        village_cal.add_component(event)
for event in cal.walk('vevent'):
    if 'youth' in event.get('location', '').lower():
        youth_workshop_cal.add_component(event)
for event in cal.walk('vevent'):
    if 'sense' in event.get('location', '').lower():
        sense_cal.add_component(event)
for event in cal.walk('vevent'):
    if 'main bar' in event.get('location', '').lower():
        main_bar_cal.add_component(event)
for event in cal.walk('vevent'):
    if 'lounges' in event.get('location', '').lower():
        Lounges_cal.add_component(event)


        
# Write the filtered calendar to a new .ical file
with open('./feeds/stage.ical', 'wb') as file:
    file.write(stage_cal.to_ical())
with open('./feeds/workshop.ical', 'wb') as file:
    file.write(workshop_cal.to_ical())
with open('./feeds/nullsector.ical', 'wb') as file:
    file.write(nullsector_cal.to_ical())
with open('./feeds/villages.ical', 'wb') as file:
    file.write(village_cal.to_ical())
with open('./feeds/youth_workshop.ical', 'wb') as file:
    file.write(youth_workshop_cal.to_ical())
with open('./feeds/sensewithoutsite.ical', 'wb') as file:
    file.write(sense_cal.to_ical())
with open('./feeds/main_bar.ical', 'wb') as file:
    file.write(main_bar_cal.to_ical())
with open('./feeds/Lounges.ical', 'wb') as file:
    file.write(Lounges_cal.to_ical())