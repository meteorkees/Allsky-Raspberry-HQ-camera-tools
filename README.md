# Allsky-Raspberry-HQ-camera-tools

The script LightConditionTool.py will return an integer for the 5 different main light conditions:

  0. Day (sun above local horizon)
  1. Civil twilight (sun between 0 and 6 degrees below horizon)
  2. Nautical twilight (sun between 6 and 12 degrees below horiaon)
  3. Astronomical twilight (sun between 12 and 18 degreees below horizon)
  4. Night (sun more then 18 degrees below horizon)

the Python package Ephem is used. To install do: pip install ephem
Further information about this package can be found here: https://pypi.org/project/ephem/

Change the observer_location latitude and longtitude to compute the current 'light' condition (cs) for that location.
The script will return an integer [0-4].
