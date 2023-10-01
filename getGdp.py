import pandas as pd
import requests
import os
from dotenv import load_dotenv
import json

load_dotenv()
api_key = os.getenv('API_KEY')

# Use the Federal Reserve Economic Data (FRED) API to download the data. We can use the pandas library in Python to get the data as a Pandas DataFrame:
url = f"https://api.stlouisfed.org/fred/series/observations?series_id=GDP&api_key={api_key}&file_type=json"

data = requests.get(url).json()

with open('us_gdp_raw.json', 'w') as f:

    # Convert dict to JSON object
    json.dump(data, f)

df = pd.DataFrame(data['observations'])
df.to_csv('us_gdp_raw.csv')

# Clean up the DataFrame - set index to date, convert billions of dollars to trillions:
df['value'] = df['value'] / 1000
df = df.set_index('date')

# The DataFrame df now contains the annual US GDP data from 1929 to latest quarter, in trillions of dollars.
# For data before 1929, we can extract it from an existing dataset and append to df
historical = pd.DataFrame({'date':pd.date_range('1900-01-01', '1928-12-31', freq='AS'),
                           'value': [0.023, 0.026, 0.029, 0.033, 0.036, 0.042, 0.049, 0.054, 0.060,
                                     0.070, 0.078, 0.087, 0.100, 0.116, 0.130, 0.140, 0.158, 0.182,
                                     0.197, 0.204, 0.223, 0.252, 0.273, 0.299, 0.337, 0.370, 0.413,
                                     0.456]})

df = pd.concat([historical, df])

df.to_csv('us_gdp.csv')
