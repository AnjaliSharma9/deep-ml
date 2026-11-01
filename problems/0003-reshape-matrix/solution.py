import numpy as np

def reshape_matrix(a: list[list[int|float]], new_shape: tuple[int, int]) -> list[list[int|float]]:
	#Write your code here and return a python list after reshaping by using numpy's tolist() method
	arr = np.array(a) #convert to array 
	if arr.size != new_shape[0]*new_shape[1]: #check if the size matches 
		return []
	return arr.reshape(new_shape).tolist() #reshape and then return as a list 