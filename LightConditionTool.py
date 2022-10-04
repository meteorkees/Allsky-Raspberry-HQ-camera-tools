import ephem
from math import pi


observer_location = ephem.Observer()
observer_location.lat='51.501805'
observer_location.lon='3.949865'
# %% these parameters are for super-precise estimates, not necessary.
observer_location.elevation = 6 # meters
#observer_location.pressure = 1010 # millibar
#observer_location.temp = 12 # deg. Celcius

sun = ephem.Sun()
sun.compute(observer_location)
alt = (sun.alt)
alt_sun = float(alt /pi *180) #radians to degrees, https://rhodesmill.org/pyephem/angle
print(alt_sun) #check results
#The variable cs (current_situation) will be an integer from 0, daytime, till 4, nighttime.
#1, 2, and 3 stand for the different twilights between daytime-nighttime-daytime.
#This integer can be used to determine what camera configuration can be used for each of these 'light' conditions.
if alt_sun >= 0:
    cs = 0 #daytime
elif (0 > alt_sun >= -6):
    cs = 1 #civil twilight
elif (-6 > alt_sun >= -12):
    cs = 2 #nautical twilight
elif (-12 > alt_sun >= -18):
    cs = 3 #astronomical twilight
else:
    cs = 4 #nighttime
print(cs)


