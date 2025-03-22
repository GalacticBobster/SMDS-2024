

from pylab import *
import pandas as pd

# Read the CSV file
file_path = "../../data/NEO_approach.csv"
df = pd.read_csv(file_path, encoding='ISO-8859-1')


def parse_size(diameter):
    try:
        # Check for uncertainty
        if '*' in diameter:
            # Split the central value and uncertainty
            central_value, uncertainty = diameter.split('*')
            central_value = central_value.strip().replace(" m", "").replace(" km", "")
            uncertainty = uncertainty.strip().replace(" m", "").replace(" km", "")
            
            # Convert to float and handle units
            central_value = float(central_value) * (1000 if "km" in diameter else 1)
            uncertainty = float(uncertainty) * (1000 if "km" in diameter else 1)
            
            return central_value - uncertainty, central_value + uncertainty
        else:
            # Handle ranges (e.g., "0.3-0.5 km")
            if '-' in diameter:
                sizes = diameter.split("-")
                min_size = sizes[0].strip().replace(" m", "").replace(" km", "")
                max_size = sizes[1].strip().replace(" m", "").replace(" km", "")
                
                # Convert to float and handle units
                min_size = float(min_size) * (1000 if "km" in sizes[0] else 1)
                max_size = float(max_size) * (1000 if "km" in sizes[1] else 1)
                
                return min_size, max_size
            else:
                # Handle single value diameters (e.g., "0.3 km")
                diameter = diameter.strip().replace(" m", "").replace(" km", "")
                size = float(diameter) * (1000 if "km" in diameter else 1)
                return size, size
    except Exception as e:
        print(f"Error parsing diameter '{diameter}': {e}")
        return None, None

df[['Min Size (m)', 'Max Size (m)']] = df['Diameter'].apply(lambda x: pd.Series(parse_size(str(x).strip())))

H = df['H(mag)']
smin = df['Min Size (m)']
smax = df['Max Size (m)']



# Print results
for i in range(len(H)):
   plt.hlines(H[i], smin[i], smax[i], colors='k', linestyles='solid')
   plt.vlines(smin[i], H[i] - 0.5, H[i] + 0.5, colors='k', linestyles='solid')
   plt.vlines(smax[i], H[i] - 0.5, H[i] + 0.5, colors='k', linestyles='solid')

plt.hlines(22, 1e-2, 1e5, colors='r', linestyles='solid')
xscale('log')
xlabel('Size (m)')
ylabel('H (magnitude)')
xscale([1e-2, 1e4])
savefig('../../figs/NEO_HvSize.png')
#    print(f"{row['Object']}: {row['Min Size (m)']} m - {row['Max Size (m)']} m")