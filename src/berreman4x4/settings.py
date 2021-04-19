# Encoding: utf-8

"""
Settings used during runtime.
Change in script by accessing the settings dict.


expmBackend:
    Library used to calculate the matrix exponential

    scipy (default) - not vectorized, thus slow
    tensorflow      - faster, but experimental and maybe loss of accuracy
    pytorch         - experimental

"""

# Default settings

settings = {
    'expmBackend': 'scipy'
}
