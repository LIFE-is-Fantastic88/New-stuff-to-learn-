import requests
import pandas as pd
import datetime

url = "https://api.data.gov.sg/v1/transport/taxi-availability"

params = {"date_time": datetime.datetime.now().strftime('%Y-%m-%dT%H:%M:%S')}

response = requests.get(url, params=params)

df = pd.DataFrame(response.json()['features'][0]['geometry']['coordinates'], columns=['longitude', 'latitude'])

counts = df.groupby(['longitude', 'latitude']).size().reset_index(name='count')

counts['address'] = ''
counts['road'] = ''
counts['postcode'] = ''
counts['county'] = ''

datenow = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

counts['datenow'] = datenow

# use the Nominatim API to get the address based on lat & long
for i, row in counts.iterrows():
    lat = row['latitude']
    lon = row['longitude']
    url = f'https://nominatim.openstreetmap.org/reverse?format=jsonv2&lat={lat}&lon={lon}'
    response = requests.get(url).json()
    counts.at[i, 'address'] = response['display_name']

    if "road" in response['address']:
        counts.at[i, 'road'] = response['address']['road']
    else:
        counts.at[i, 'road'] = ""

    if "postcode" in response['address']:
        counts.at[i, 'postcode'] = response['address']['postcode']
    else:
        counts.at[i, 'postcode'] = ""

    if "county" in response['address']:
        counts.at[i, 'county'] = response['address']['county']
    else:
        counts.at[i, 'county'] = ""

counts.to_csv('taxi_counts_with_address_new1.csv', index=False)
