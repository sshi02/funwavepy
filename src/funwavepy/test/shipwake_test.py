import pandas as pd
import sys
sys.path.insert(1, '../funwavetvd/')

from shipwake import *

###
print("Vessel Instance and __str__ test")
###
test_pdf = pd.DataFrame({'nt': [0.0, 100.0, 120.0], 'nx': [50.00, 1050.0, 2000.0], 'ny': [120.0, 120.0, 120.0]})
test_vessel = Vessel(PRESSURE1, 220.0, 10.0, 0.9, 0.9, 0.5, 3.0, test_pdf)
print("begin output:")
print(test_vessel)
print("end output")

###
print("Shipwake Instance Test")
###
test_shipwake = Shipwake()
test_shipwake.append_vessel(test_vessel)
test_shipwake.vessel_forcing(None, None, None, None, None)
