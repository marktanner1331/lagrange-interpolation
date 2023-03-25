import numpy as np
from numpy.polynomial import Polynomial

points = np.array([
	[0, 0.1],
	[0.5, 0.2],
	[1, 1]])

n = len(points)
poly = Polynomial(np.zeros(n))

for j in range(n):
    k = [k for k in range(n) if k != j]
    roots = -1 * points[k, 0]
  
    sub_poly = Polynomial.fromroots(points[k, 0])
    scale = points[j, 1] / np.prod(points[j, 0] - points[k, 0])
    sub_poly.coef *= scale
    
    poly.coef += sub_poly.coef

print(poly)
