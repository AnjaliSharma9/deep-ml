import numpy as np
def scalar_multiply(matrix: list[list[int|float]], scalar: int|float) -> list[list[int|float]]:
	new_matrix = np.array(matrix)*scalar
	result = np.array(new_matrix).tolist()
	return result
	
	pass