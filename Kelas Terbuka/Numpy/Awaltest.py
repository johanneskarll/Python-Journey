import numpy as np

vector_a = np.array([1,2,3,4])
list_a = [1,2,3,4]

print(f"list_a = {list_a}") # list ada koma komanya
print(f"vector_a = {vector_a}")

# print(list_a**2) <- ini gabisa
print(f"a pangkat 2 = {vector_a**2}") # yang ini malah bisa~

matrix_b = np.array([(1,2),(3,4)])
print(f"matrix b = \n{matrix_b}")
print(f"matrix b^2 = \n{matrix_b**2}")

zeros_c = np.zeros((3,3))
print(f"zeros c = \n{zeros_c}")

ones_d = np.ones((2,2))
print(f"ones c = \n{ones_d}")

nambahin = matrix_b + matrix_b**2 + ones_d
print(nambahin)