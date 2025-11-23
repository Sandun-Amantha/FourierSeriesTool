import numpy as np
from fourier import compute_fourier_coefficients, fourier_series
from utils import plot_fourier, play_sound, fourier_to_audio
import matplotlib.pyplot as plt
import time

# user inputs
print("=== Fourier Series Tool ===")
func_input = input("Enter a periodic function of x (e.g., 'np.sin(x)', 'x', 'x**2'): ")
N = int(input("Enter number of Fourier terms N (e.g., 20): "))
duration = float(input("Enter audio duration in seconds (e.g., 3): "))

# Define the function
def f(x):
    return eval(func_input)

# Fourier series parameters
T = 2 * np.pi
L = T / 2

# Compute Fourier coefficients
a0, an, bn = compute_fourier_coefficients(f, L, N)

# Reconstruct Fourier series for plotting
x = np.linspace(-L, L, 1000)
y_original = f(x)
y_fourier = fourier_series(a0, an, bn, L, x)

# Plot original vs Fourier approximation
plot_fourier(x, y_original, y_fourier, N)

# Wait 1 second before playing audio 
time.sleep(1)

# Generate audible Fourier sound 
y_audio = fourier_to_audio(a0, an, bn, duration=duration, base_freq=220)
play_sound(y_audio, duration=duration)


plt.show()
