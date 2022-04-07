# funwavepy
### FUNWAVE-TVD Python wrapper with post-processing capabilites
Fortran libraries referenced and built from [FUNWAVE-TVD](https://github.com/fengyanshi/FUNWAVE-TVD).

Todo:
- Process FUNWAVE-TVD .F files through F2PY for module use
- Handle [Input Parameters](https://fengyanshi.github.io/build/html/definition.html)
  - Parameters for Central Module
  - Spherical Coordinate Case (maybe make a seperate model object?)
  - Shipwakes
  - Sediment Transport and Morphological Change
  - Wind and Pressure Field
  - Lagrangian Tracer Setup
  - Landslide
- Handle multi-threaded processing (parallel info in input.txt)
- figure out license issues lol

Structure:
- funwavepy Modules - acts as the 'main.F'. Inputs to methods in this class are below.
  - running the model happens here! important flags/considerations
    - parallel processing
    - output formats (numpy output vs original FUNWAVE-TVD binary file output for people who already have post-processing scripts)
  - main.F def needs to be altered, and I need to make multiple main files
- Implement Model Modules (replacing input.txt)
  - Model Class will handle all model related variables in Model object, as well as provide the necessary helper methods to adjust each Parameter for Central Module.
    - !will need to figure out a good spread of defaults and need to changes with their respective error messsages!
  - Model Class will also house Classes for Shipwake models, landslides, etc, so these can be added to the model to allow for modularity
  - Should also make use of existing File i/o from .F, allowing users to use the wrapped main.F without having to convert old input files into Python objects.
- Implement Post-processing modules
