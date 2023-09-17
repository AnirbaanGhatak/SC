import numpy as np

def perceptron_and(A, B):
    w = np.array([0.5, 0.5])
    b = -0.7
    if B == 0:
        B = 1
    else:
        B = 0
    x = np.array([A,B])
    result = np.dot(w, x) + b
    if result > 0:
      return 1
    else:
      return 0
    

print(perceptron_and(0,0))
print(perceptron_and(0,1))
print(perceptron_and(1,0))
print(perceptron_and(1,1))