import model

### Structural Variables
# VESSEL TYPES
PRESSURE1 = 1
PRESSURE2 = 2
SLENDER1 = 3
SLENDER2 = 4


class Vessel():
    """Vessel Class """
    def __init__(self, type,
                length, width,
                alpha1, alpha2, beta, pm,
                t0, tf, x0, y0, xf, yf):
        """
            Constructor for Vessel object
                Instance Variables & Parameters
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
                    t0           : initial time
                    tf           : final time
                    x0           : initial x
                    y0           : initial y
                    xf           : final x
                    yf           : final y
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
        self.t0 = t0
        self.tf = tf
        self.x0 = x0
        self.y0 = y0
        self.xf = xf
        self.yf = yf

    @classmethod
    def file_to_vessel(cls, filename):
        data = read_file_vessel(filename)
        return cls(type = data['type'], length = data['length'],
                   width = data['width'], alpha1 = data['alpha1'],
                   alpha2 = data['alpha2'], beta = beta['beta'],
                   pm = data['pm'], t0 = data['t0'], tf = data['tf'],
                   x0 = data['x0'], xf = data['y0'], xf = data['xf'],
                   yf = data['yf'])

    def read_file_vessel(filename):
        fp = open(filename, 'rb+')
        fp.close()
        # --- TODO --- #
