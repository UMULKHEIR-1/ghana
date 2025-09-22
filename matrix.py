import numpy as np

# Create two 2x2 arrays
A = np.array([[15, 2],
              [10, 4]])

B = np.array([[51, 8],
              [9, 13]])

print("Array A:")
print(A)

print("\nArray B:")
print(B)

# Elementwise addition
add = A + B
print("\nElementwise addition (A + B):")
print(add)

# Elementwise multiplication
multiply = A * B
print("\nElementwise multiplication (A * B):")
print(multiply)

# Matrix product (dot product)
matmul = A @ B
print("\nMatrix product (A @ B):")
print(matmul)