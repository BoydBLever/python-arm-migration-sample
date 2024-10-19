import locale
import numpy as np

# Example of deprecated function usage in Python
def get_system_locale():
    """
    Get system locale, but using a deprecated function that needs to be replaced.
    """
    # Deprecated as of Python 3.11, planned removal in Python 3.15
    default_locale = locale.getdefaultlocale()
    print(f"System locale: {default_locale}")

# Example of CPU-intensive function
def matrix_multiplication():
    """
    Perform matrix multiplication, which could be optimized for ARM NEON instructions.
    """
    A = np.random.rand(1000, 1000)
    B = np.random.rand(1000, 1000)
    
    # This could be optimized with ARM-specific libraries
    C = np.dot(A, B)
    return C

if __name__ == "__main__":
    get_system_locale()
    result = matrix_multiplication()
    print("Matrix multiplication completed.")
