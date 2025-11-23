import matplotlib.pyplot as plt
import numpy as np
import sounddevice as sd

def plot_fourier(x, y_original, y_fourier, N):
    """
    Plot the original function and its Fourier series approximation.
    plot sand audio play simultaneously.
    """
    plt.figure(figsize=(10,5))
    plt.plot(x, y_original, label="Original function", color="blue")
    plt.plot(x, y_fourier, label=f"Fourier Series Approx (N={N})", color="red", linestyle="--")
    plt.title("Fourier Series Approximation")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.grid(True)
    plt.legend()
    plt.show(block=False)  

def play_sound(y, duration=3, fs=44100):
    """
    Play audio from a waveform y.
    
    """
    y = y - np.mean(y)           
    max_val = np.max(np.abs(y))
    if max_val == 0:
        max_val = 1              # Prevent division by zero
    y = 0.8 * y / max_val        # Scale to 80% volume
    
    # Ensure duration is float and calculate total samples
    duration = float(duration)
    total_samples = int(fs * duration)
    samples = np.interp(np.linspace(0, len(y), total_samples), np.arange(len(y)), y)
    
    print("Playing audio...")
    sd.play(samples, fs)
    sd.wait()
    print("Audio finished.")

def fourier_to_audio(a0, an, bn, duration=3, fs=44100, base_freq=220):
    """
    Convert Fourier series coefficients into audible sound.
    
    Parameters:
    - a0, an, bn: Fourier coefficients
    - duration: seconds (float)
    - fs: sampling rate
    - base_freq: fundamental frequency in Hz
    """
    duration = float(duration)
    t = np.linspace(0, duration, int(fs*duration))
    y = np.zeros_like(t)
    
    # Add a0 component
    y += a0 / 2
    
    # Sum all Fourier terms
    for n in range(1, len(an)+1):
        y += an[n-1] * np.cos(2 * np.pi * n * base_freq * t)
        y += bn[n-1] * np.sin(2 * np.pi * n * base_freq * t)
    
    # Normalize amplitude
    y = y - np.mean(y)
    y = 0.8 * y / np.max(np.abs(y))
    return y
