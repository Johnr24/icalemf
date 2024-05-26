from icalendar import Calendar
import requests
import csv
# Download the 2024.ical file from the given URL
url = 'https://www.emfcamp.org/schedule/2024.ical'
response = requests.get(url)
with open('./2024.ical', 'wb') as file:
    file.write(response.content)

#please scan through the descriptions of each event and give me a list of values that contain "Attending this workshop will cost:" and the value that follows it"
with open('./2024.ical', 'rb') as file:
    cal = Calendar.from_ical(file.read())

cost_values = []
for component in cal.walk():
    if component.name == 'VEVENT':
        description = component.get('description')
        if description and 'Attending this workshop will cost:' in description:
            cost_index = description.index('Attending this workshop will cost:') + len('Attending this workshop will cost:')
            cost_value = description[cost_index:].strip()
            cost_values.append(cost_value)


print(cost_values)
# write to a csv file
with open('./cost_values.csv', 'w') as file:
    writer = csv.writer(file)
    for value in cost_values:
        writer.writerow([value])