import time
import multiprocessing
import numpy as np
## - todo: establish classes for these for the corresponding .F ...
import shipwake
#import sediment
#import meteo
#import tracer
#import tide
#import bathycorrection

### Global VARIABLES
# - extracted from mod_param
PI = 3.141592653
R_EARTH = 6371000.0
SMALL = 0.000001
LARGE = 999999.0
GRAV = 9.81
ZERO = 0.0
RHO_AW = 0.0012041  # relative to water
RHO_AIR = 1.15      # absolute value
RHO_WATER = 1000.0
DEG2RAD = 0.0175
# iteration?????? double check here

class FunwaveModel():
    """FunwaveModel Class"""
    def __init__(self, output_filename):
        """FunwaveModel Constructor"""
        ### Initializing Necessary Model Variables
        # Timer:
        self.t_begin = None
        self.t_end = None

        # ------------------------ #
        # flags for central module
        # ------------------------------------------------------- #
        ## title
        self.title = None

        ## grid and computation time
        # --- TODO --- #
        self.mglob = None
        self.nglob = None
        self.dx = None
        self.dy = None

        ## physics
        # --- TODO --- #
        self.dispersion_flag = True
        self.gamma1 = 1.0
        self.gamma2 = 1.0
        self.gamma3 = 1.0
        self.beta_ref = -0.531
        self.viscosity_breaking_flag = True
        self.cbrk1 = 0.45
        self.cbrk2 = 0.35
        self.swe_eta_dep = 0.80
        self.roller_effect_flag = False
        self.friction_matrix_flag = False
        self.friction_file = None

        ## numerical parameters
        # --- TODO --- #

        ## wave-maker specification
        # --- TODO --- #

        ## periodic boundry condition
        # --- TODO --- #

        ## tide and surge boundary conditions
        # --- TODO --- #

        ## wave statitistics
        # --- TODO --- #

        ## sponge layer
        # --- TODO --- #

        ## breakwater and obstacle
        # --- TODO --- #

        ## bathymetry collection
        # --- TODO --- #

        ## output
        # --- TODO --- #
        self.output_filename = output_filename

        # --------------- #
        # modules & flags
        # ------------------------------------------------------- #
        ## shipwake module
        self.use_vessel = False
                # -- TODO -- #

        ## sediment module
        self.use_sediment = False
                # -- TODO -- #

        ## meteo module
        self.use_meteo = False
                # -- TODO -- #

        ## lagrangian tracer module
        self.use_tracer = False
                # -- TODO -- #

        ## tide module
        self.use_tide = True
                # -- TODO -- #

        # --------------------- #
        # spherical coordinates
        # ------------------------------------------------------- #
        # -- TODO -- #

        # -------------------- #
        # parallel processing
        # ------------------------------------------------------- #
        # - by default, will split cores by following:
        #   - ncores = py * px such that py is a power of two
        self.useParallel = True
        ncores = multiprocessing.cpu_count()
        if ncores % 2 == 1 :
            self.px = ncores
            self.py = py
        else:
            x = ncores
            factor = 1
            while x % 2:
                x = x / 2
                factor = factor * 2
            self.px = ncores / factor
            self.py = factor

        ## HotStartTime
                # -- TODO -- #

        ## initizialization
                # -- TODO -- #
        # need to a lot of heavy lifiting here from init.F @ INITIZIALIZATION


        ### Getters and Setters
        ## set_time
        def set_time(bt, et):
            self.t_begin = bt
            self.t_end = et

        ## set_parallel
        def set_parallel(px, py) :
            """
                Setter method for core allocation in parallel postprocess

                    Parameters:
                        px (int): cores allocated for processing on x
                        py (int): cores allocated for processing on y

                    Returns:
                        void
            """
            self.px = px
            self.py = py

        ## append_vessel
        def append_vessel(vesselobj):
            """
                Setter method for appending vessels to vessel_arr

                    Parameters:
                        vesselobj : vesselobj of class Vessel() from vessel.py

                    Returns:
                        void
            """
            self.use_vessel = True
            np.append(self.vessel_arr, [vesselobj])
