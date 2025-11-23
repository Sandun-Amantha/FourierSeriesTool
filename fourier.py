import numpy as np
from scipy.integrate import quad

def compute_fourier_coefficients(f, L, N):
    """
    Compute Fourier series coefficients a0, an, bn for a periodic function f
    over interval [-L, L] using N terms.
    """
    # a0 coefficient
    a0 = (1 / L) * quad(f, -L, L)[0]

    # Initialize arrays for an and bn
    an = np.zeros(N)
    bn = np.zeros(N)

    # Compute coefficients
    for n in range(1, N + 1):
        an[n-1] = (1 / L) * quad(lambda x: f(x) * np.cos(n * np.pi * x / L), -L, L)[0]
        bn[n-1] = (1 / L) * quad(lambda x: f(x) * np.sin(n * np.pi * x / L), -L, L)[0]

    return a0, an, bn

def fourier_series(a0, an, bn, L, x):
    """
    Reconstruct Fourier series at points x given coefficients a0, an, bn.
    """
    y = np.full_like(x, a0 / 2)  # start with a0/2
    N = len(an)
    for n in range(1, N + 1):
        y += an[n-1] * np.cos(n * np.pi * x / L) + bn[n-1] * np.sin(n * np.pi * x / L)
    return y
