import requests
import pandas as pd


# Define API URL
url = "https://ssd-api.jpl.nasa.gov/sbdb_query.api"

# Define query parameters
params = {
    "fields": "full_name,epoch,e,q,a,i,moid,diameter,rot_per",  # Get orbital elements and size/rotation
    "limit": 1000  # Number of objects to retrieve (adjust as needed)
}

# Send request
response = requests.get(url, params=params)
data = response.json()


# Convert to DataFrame
df = pd.DataFrame(data['data'], columns=data['fields'])

df["moid"] = pd.to_numeric(df["moid"], errors="coerce")
# Filter for objects entering near Earth's orbit (MOID < 0.02 AU)
df_near_earth = df[df["moid"] < 1]  # 0.02 AU ~ 3 million km

# Print first few results
print(df_near_earth.head())
