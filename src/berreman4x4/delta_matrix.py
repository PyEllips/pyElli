# Encoding: utf-8
import numpy as np

def buildDeltaMatrix(Kx, eps):
    """Returns Delta matrix for given permittivity and reduced wave number.

    'Kx' : reduce wave number, Kx = kx/k0
    'eps' : permittivity tensor

    Returns : Delta 4x4 matrix, generator of infinitesimal translations
    """
    if np.shape(Kx) == ():
        i = 1
    else:
        i = np.shape(Kx)[0]

    Delta = np.array(
        [[-Kx * eps[:, 2, 0] / eps[:, 2, 2], -Kx * eps[:, 2, 1] / eps[:, 2, 2],
          np.tile(0, i), np.tile(1, i) - Kx**2 / eps[:, 2, 2]],
         [np.tile(0, i), np.tile(0, i), np.tile(-1, i), np.tile(0, i)],
         [eps[:, 1, 2] * eps[:, 2, 0] / eps[:, 2, 2] - eps[:, 1, 0],
          Kx**2 - eps[:, 1, 1] + eps[:, 1, 2] * eps[:, 2, 1] / eps[:, 2, 2],
          np.tile(0, i), Kx * eps[:, 1, 2] / eps[:, 2, 2]],
         [eps[:, 0, 0] - eps[:, 0, 2] * eps[:, 2, 0] / eps[:, 2, 2],
          eps[:, 0, 1] - eps[:, 0, 2] * eps[:, 2, 1] / eps[:, 2, 2],
          np.tile(0, i), -Kx * eps[:, 0, 2] / eps[:, 2, 2]]])
    Delta = np.moveaxis(Delta, 2, 0)
    return Delta