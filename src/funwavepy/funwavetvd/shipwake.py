import model
import numpy as np
import pandas as pd

### Structural Values
# VESSEL TYPES
PRESSURE1 = 1
PRESSURE2 = 2
SLENDER1 = 3
SLENDER2 = 4

class Vessel():
    """
    Vessel class - Houses Vessel Object and Methods
    __init__ : see print(__init__.__doc__)

    """
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self, type,
                length, width,
                alpha1, alpha2, beta, pm, pdf):
        """
        Constructor for Vessel object
            Instance Parameters
                int type     : type of Vessel, below are globally defined constants
                    1 == PRESSURE1
                    2 == PRESSURE2
                    3 == SLENDER1
                    4 == SLENDER2
                    other == PRESSURE1
                float length : length of vessel in meters
                float width  : width of vessel in meters
                float alpha1
                float alpha2
                float beta
                float pm
                DataFrame pdf : vessel path dataframe
                    - Structure of pdf:
                |  time  |   x(m)   |   y(m)   |

            Other Instance Variables
            float t1_vessel : vessel time1
            float t2_vessel : vessel time2

        """
        if type < 0 or type > 4:
            self.type = PRESSURE1
        else:
            self.type = type
        self.length = length
        self.width = width
        self.alpha1 = alpha1
        self.alpha2 = alpha2
        self.beta = beta
        self.pm = pm
        self.pdf = pdf
        self.pdf.columns = ['time', 'x', 'y']

    @classmethod
    def file_to_vessel(cls, filename):
        data = read_file_vessel(filename)
        return cls(type = data['type'], length = data['length'],
                   width = data['width'], alpha1 = data['alpha1'],
                   alpha2 = data['alpha2'], beta = beta['beta'],
                   pm = data['pm'], t0 = data['t0'], tf = data['tf'],
                   x0 = data['x0'], xf = data['y0'], y0 = data['y0'],
                   yf = data['yf'])

    def read_file_vessel(filename):
        fp = open(filename, 'rb+')
        fp.close()
        # --- TODO --- #

    def __str__(self):
        type_string = None
        if (self.type == PRESSURE1):
            type_string = "PRESSURE, 1"
        elif (self.type == PRESSURE2):
            type_string = "PRESSURE 2"
        elif (self.type == SLENDER1):
            type_string = "SLENDER, 1"
        elif (self.type == SLENDER2):
            type_string = "SLENDER, 2"

        txy = ""
        for i, row in self.pdf.iterrows():
            txy += f'{row[0]:9}{row[1]:11}{row[2]:10}' + '\n'

        return ("Vessel Type: " + type_string + "\n" +
            "Length(m)   Width(m)   Alpha1   Alpha2   Beta   P(m)\n" +
            f'{self.length:9}{self.width:11}{self.alpha1:9}{self.alpha2:9}{self.beta:7}{self.pm:7}' + "\n" +
            "Time        X(m)       Y(m) \n" +
            txy)

class Shipwake:
    """Shipwake class"""
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self):
        self.vessel_arr = np.array([], dtype = object)
        deep_draft_vessel_flag = False

        ## fast(er) memory allocation
        # by how much? i dont know lol
        self.x0_vessel = np.array([], dtype = float)
        self.y0_vessel = np.array([], dtype = float)
        self.x1_vessel = np.array([], dtype = float)
        self.y1_vessel = np.array([], dtype = float)
        self.a1_vessel = np.array([], dtype = float)
        self.a2_vessel = np.array([], dtype = float)
        self.b_vessel = np.arrray([], dtype = float)
        self.p_vessel = np.array([], dtype = float)
        self.l_vessel = np.array([], dtype = float)
        self.w_vessel = np.array([], dtype = float)
        self.t0_vessel = np.array([], dtype = float)
        self.t1_vessel = np.array([], dtype = float)
        self.theta_vessel = np.array([], dtype = float)

    def append_vessel(self, vessel):
        self.vessel_arr = np.append(self.vessel_arr, [vessel])

    def append_vessel_arr(self, arr):
        self.vessel_arr = np.append(self.vessel_arr, arr)

    def clear_shipwake(self):
        self.vessel_arr = np.array([], dtype = object)

    def reset_shipwake(self):


    def vessel_forcing(self, mloc, nloc, time, dt, depth):
        # allocating local variables
        flux_gradient = model.ZERO
        pressure_total = model.ZERO

        # iterate through vessels
        for vessel in np.nditer(self.vessel_arr, flags = ['refs_ok']):
            # --- TO DO --- #
