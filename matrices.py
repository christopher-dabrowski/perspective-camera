"""Module for easily creating transformation matrices"""

import numpy as np


def translation_matrix(dx: float, dy: float, dz: float) -> np.array:
    matrix = np.eye(4)
    matrix[-1][:3] = dx, dy, dz

    return matrix
