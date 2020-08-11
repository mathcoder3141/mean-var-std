import numpy as np
import pprint as pp

lst = []
while len(lst) < 9:
	if len(lst) == 0:
		num = input("Enter a number: ")
	else:
		num = input("Enter another number: ")
	lst.append(float(num))

def calculate(lst):
	if len(lst) == 9:
		grid = np.asarray(lst, dtype=float)
		grid.shape = (3, 3)
		mean = [[np.mean(grid[:,x]) for x in range(0,3)], [np.mean(grid[x]) for x in range(0,3)],  np.mean(grid)]
		variance = [[np.var(grid[:,x]) for x in range(0,3)], [np.var(grid[x]) for x in range(0,3)],  np.var(grid)]
		std_dev = [[np.std(grid[:,x]) for x in range(0,3)], [np.std(grid[x]) for x in range(0,3)],  np.std(grid)]
		maximum = [[np.max(grid[:,x]) for x in range(0,3)], [np.max(grid[x]) for x in range(0,3)],  np.max(grid)]
		minimum = [[np.min(grid[:,x]) for x in range(0,3)], [np.min(grid[x]) for x in range(0,3)],  np.min(grid)]
		summation = [[np.sum(grid[:,x]) for x in range(0,3)], [np.sum(grid[x]) for x in range(0,3)],  np.sum(grid)]
		calculations = {
		'mean' : mean,
		'variance' : variance,
		'standard deviation' : std_dev,
		'max' : maximum,
		'min' : minimum,
		'sum' : summation
		}
		pp.pprint(calculations)
	else:
		raise ValueError("List must contain nine numbers.")
	return calculations

calculate(lst)