import numpy as np

def matrix_transpose(A):
    """
    Return the transpose of matrix A (swap m and columns).
    """
    # Write code here
    A = np.asarray(A)

    m, n = A.shape
    result = np.zeros((n, m), dtype=A.dtype)

    for i in range(m):
        for j in range(n):
            result[j, i] = A[i, j]

    return result
        
    pass
