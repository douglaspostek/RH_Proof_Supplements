import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)

# Load datasets (replace with actual file paths)
freqs = np.array([float(line.split(',')[0]) for line in open('fourier_data.csv').readlines()[1:]])
power = np.array([float(line.split(',')[1]) for line in open('fourier_data.csv').readlines()[1:]])
prime_indices = np.array([float(line.split(',')[0]) for line in open('prime_data.csv').readlines()[1:]])
primes = np.array([float(line.split(',')[1]) for line in open('prime_data.csv').readlines()[1:]])
gaps = np.array([float(line.split(',')[2]) if line.split(',')[2] else np.nan for line in open('prime_data.csv').readlines()[1:]])
t_values = np.array([float(line.split(',')[1]) for line in open('zeros_data.csv').readlines()[1:]])
spacings = np.diff(t_values)
k_values = np.arange(51)
H_04 = np.array([float(line.split(',')[1]) for line in open('h_sk_data.csv').readlines()[1:]])
H_05 = np.array([float(line.split(',')[2]) for line in open('h_sk_data.csv').readlines()[1:]])
H_06 = np.array([float(line.split(',')[3]) for line in open('h_sk_data.csv').readlines()[1:]])

# Figure 2A: Prime Gaps
plt.figure(figsize=(10, 6))
plt.scatter(prime_indices[1:], gaps[1:], c='black', s=10)
plt.grid(True)
plt.title("Prime Gaps: First 1000 Primes")
plt.xlabel("Prime Index")
plt.ylabel("Gap Size")
plt.ylim(0, 35)
plt.savefig("Figure_2A.png")
plt.close()

# Figure 2B: RH Zeros (First 1000)
plt.figure(figsize=(10, 6))
plt.scatter(np.full(1000, 0.5), t_values, c='red', s=10)
plt.grid(True)
plt.title("RH Zeros: σ = 1/2, First 1000")
plt.xlabel("Re(s)")
plt.ylabel("Im(s)")
plt.ylim(0, 1000)
plt.savefig("Figure_2B.png")
plt.close()

# Figure 2C: Stabilization of |H(s, k)|
plt.figure(figsize=(10, 6))
plt.plot(k_values, H_04, 'b-', label="σ = 0.4")
plt.plot(k_values, H_05, 'g-', label="σ = 0.5")
plt.plot(k_values, H_06, 'r-', label="σ = 0.6")
plt.grid(True)
plt.legend()
plt.title("Stabilization of |H(s, k)|")
plt.xlabel("Iteration k")
plt.ylabel("Magnitude")
plt.savefig("Figure_2C.png")
plt.close()

# Figure 3A: RH Zeros (First 100)
plt.figure(figsize=(10, 6))
plt.scatter(np.full(100, 0.5), t_values[:100], c='red', s=10)
plt.grid(True)
plt.title("RH Zeros: σ = 1/2, First 100")
plt.xlabel("Re(s)")
plt.ylabel("Im(s)")
plt.ylim(0, 200)
plt.savefig("Figure_3A.png")
plt.close()

# Figure 4A: DFT of RH Zero Spacings
plt.figure(figsize=(10, 6))
plt.plot(freqs, power, 'b-', label="DFT")
plt.plot(2 * np.pi * np.log(primes[:50]) / (2 * np.pi), np.ones(50) * 50000, 'ro', label="Theoretical Peaks")
plt.grid(True)
plt.title("DFT of RH Zero Spacings")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Power")
plt.legend()
plt.xlim(0, 0.5)
plt.savefig("Figure_4A.png")
plt.close()

# Figure 4B: Gaps vs. Zero Spacings
plt.figure(figsize=(10, 6))
plt.scatter(spacings, gaps[1:], c='black', s=10)
plt.grid(True)
plt.title("Gaps vs. Zero Spacings")
plt.xlabel("Zero Spacing")
plt.ylabel("Gap Size")
plt.xlim(-20, 35)
plt.ylim(0, 35)
plt.savefig("Figure_4B.png")
plt.close()

# Figure 4C: Convergence at σ = 1/2
plt.figure(figsize=(10, 6))
plt.plot(k_values, H_05, 'g-', label="σ = 0.5")
plt.plot(k_values, H_04, 'b-', label="σ = 0.4")
plt.plot(k_values, H_06, 'r-', label="σ = 0.6")
plt.grid(True)
plt.legend()
plt.title("Convergence at σ = 1/2")
plt.xlabel("Iteration k")
plt.ylabel("Magnitude")
plt.savefig("Figure_4C.png")
plt.close()