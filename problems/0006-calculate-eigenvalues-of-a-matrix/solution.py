import numpy as np
import math
def calculate_eigenvalues(matrix: list[list[float|int]]) -> list[float]:
    (a,b),(c,d) = matrix
    tr = a+d
    det = a * d - b * c
    disc = math.sqrt(tr**2 - 4 * det)

    eigenvalues = [(tr + disc) / 2, (tr - disc) / 2]
    return sorted(eigenvalues, reverse=True)