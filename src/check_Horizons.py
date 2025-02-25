from astroquery.jplhorizons import Horizons
import numpy as np

# Define target asteroid (by name or ID)
target_id = "2006 RH120"  # You can use a numerical ID too

# Define observer location ('500' = geocentric, '399' = Earth center)
observer = '500'  # Geocentric (Earth-centered)

# Define time range
start_time = "2025-01-01"
end_time = "2026-01-10"
step = "1d"  # Steps of 1 day

# Query ephemeris
obj = Horizons(id=target_id, location=observer, epochs={'start': start_time, 'stop': end_time, 'step': step})
eph = obj.ephemerides()
vectors = obj.vectors()

# Extract position and velocity vectors (ECI/ICRF)
times = vectors['datetime_jd']
positions = np.array([vectors['x'], vectors['y'], vectors['z']]).T  # km
velocities = np.array([vectors['vx'], vectors['vy'], vectors['vz']]).T  # km/s


# Print first entry as example
print(f"Time (JD): {times}")
print(f"Position (km): {positions}")
print(f"Velocity (km/s): {velocities}")

