from astroquery.jplsbdb import SBDB

# List of asteroid IDs
asteroid_ids = ["2006 RH120", "99942 Apophis"]

# Loop through each asteroid and retrieve spectral type
for obj_id in asteroid_ids:
    try:
        data = SBDB.query(obj_id, phys=True)  # Query physical parameters
        spectral_type = data.get("phys_par", {}).get("spec_B", "N/A")  # Bus-Demeo taxonomy
        spectral_type_tholen = data.get("phys_par", {}).get("spec_T", "N/A")  # Tholen taxonomy

        print(f"Asteroid {obj_id} - Bus-Demeo: {spectral_type}, Tholen: {spectral_type_tholen}")
    
    except Exception as e:
        print(f"Error retrieving data for {obj_id}: {e}")

