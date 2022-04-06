import time
import multiprocessing
## - todo: establish classes for these for the corresponding .F ...
#import vessel
#import sediment
#import meteo
#import tracer
#import tide
#import bathycorrection

class FunwaveModel():
    def __init__(self):
        """FunwaveModel class --- initialize using x = FunwaveModel()"""
        ### Initializing Necessary Model Variables
        # Timer:
        tbegin
        tend

        ## modules
        useVessel = False
        useSediment = False
        useMeteo = False
        useTracer = False
        useTide = True

        ## parallel processing
        # - by default, will split cores by following:
        #   - ncores = py * px such that py is a power of two
        useParallel = True
        ncores = multiprocessing.cpu_count()
        if ncores % 2 == 1 :
            px = ncores
            py = py
        else:
            x = ncores
            factor = 1
            while x % 2:
                x = x / 2
                factor = factor * 2
            px = ncores / factor
            py = factor

        ## HotStartTime
        # --- TO DO ----

        ## initizialization
        # --- TO DO ---
        # need to a lot of heavy lifiting here from init.F @ INITIZIALIZATION


        ### Getters and Setters
        ## setParallel
        def setParallel(px, py) :
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
