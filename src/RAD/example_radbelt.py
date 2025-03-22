from radbelt import get_flux
from astropy import units as u
from astropy.coordinates import EarthLocation
from astropy.time import Time
coords = EarthLocation(-45 * u.deg, -30 * u.deg, 500 * u.km)
time = Time('2021-03-01')
energy = 20 * u.MeV
a = get_flux(coords, time, energy, 'p', 'max')  
print(a)
