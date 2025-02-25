import requests
import pandas as pd
from astroquery.jplhorizons import Horizons
from datetime import datetime, timedelta
from astropy.time import Time
from astroquery.jplsbdb import SBDB


# Define API URL
url = "https://ssd-api.jpl.nasa.gov/cad.api"

# Define query parameters
params = {
    "dist-max": "0.01",  # Max approach distance (AU) (0.01 AU ~ 1.5 million km)
    "date-min": "2025-01-01",  # Start search from 2025
    "date-max": "2035-01-10",  # Look ahead 10 years
    "sort": "date",  # Sort by closest approach date
    "diameter": "true"

    #"full-prec": "true"  # Get full precision data
    }

# Send request
response = requests.get(url, params=params)
data = response.json()
#print(data)
# Convert response to DataFrame
df_approach = pd.DataFrame(data['data'], columns=data['fields'])
date_approach = df_approach['cd']
obj_id = df_approach['des']
print(df_approach.head())

#Propagate the trajectory for all these objects one or two year before 
for i in range(len(obj_id)):
    #if (df_approach['des'][i] == '2025 DK1'):
    #data = SBDB.query(obj_id[i], phys=True)  # Query physical parameters
    #spectral_type = data.get("phys_par", {}).get("spec_B", "N/A")  # Bus-Demeo taxonomy
    #spectral_type_tholen = data.get("phys_par", {}).get("spec_T", "N/A")  # Tholen taxonomy
    #print(f"Asteroid {obj_id} - Bus-Demeo: {spectral_type}, Tholen: {spectral_type_tholen}")

    #print(df_approach['des'][i],df_approach['diameter'][i], df_approach['h'][i])
    date_approach_dt = datetime.strptime(date_approach[i], "%Y-%b-%d %H:%M")
    date_approach_dt = date_approach_dt.replace(hour=0, minute=0, second=0, microsecond=0)
    start_date = (date_approach_dt - timedelta(days=60)).strftime("%Y-%m-%d")
    end_date = (date_approach_dt + timedelta(days=60)).strftime("%Y-%m-%d")
    obj = Horizons(id=obj_id[i], location='500', epochs={'start': start_date, 'stop': end_date, 'step': "1d"})
    eph = obj.ephemerides()
    vectors = obj.vectors()


# Print first few results
