import numpy as np
def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
	toarray = np.array(matrix)
	if mode == 'row':
		means = toarray.mean(axis=1)
	else:
		means = toarray.mean(axis=0)
		
	return means