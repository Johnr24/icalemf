# Description: This script is used to get the village data from the EMF Camp API
import requests
import json
import csv
def villageget():
    url = 'https://www.emfcamp.org/api/villages'
    response = requests.get(url)
    return response.json()
print(villageget())

data = villageget()
with open('/Users/johnrogers/Documents/EMF_2024/icalemf/villagelistget/villages.json', 'w') as file:
    json.dump(data, file)

    # Print a list of village names to a CSV file

    # Get the village data
    data = villageget()

    # Extract the village names
    village_names = [village['name'] for village in data]

    # Define the CSV file path
    csv_file_path = '/Users/johnrogers/Documents/EMF_2024/icalemf/villagelistget/village_names.csv'

    # Write the village names to the CSV file
    with open(csv_file_path, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Village Names'])
        writer.writerows([[name] for name in village_names])

    print('Village names have been written to', csv_file_path)