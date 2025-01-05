import numpy as np
import matplotlib.pyplot as plt

# Parameter
hbar = 1.0545718e-34  # Konstanta Planck tereduksi (J.s)
m = 9.10938356e-31    # Massa elektron (kg)
L = 1e-10             # Panjang penghalang (m)
V0 = 10 * hbar**2 / (2 * m * L**2)  # Tinggi penghalang (J)
num_points = 1000     # Jumlah titik grid
x_min = -2e-10        # Batas kiri dari domain (m)
x_max = 2e-10         # Batas kanan dari domain (m)

# Membuat grid
x = np.linspace(x_min, x_max, num_points)
dx = x[1] - x[0]  # Jarak antar titik grid

# Membuat potensi
V = np.zeros(num_points)
V[int(num_points/2) - int(num_points/20):int(num_points/2) + int(num_points/20)] = V0

# Matriks Hamiltonian
H = np.zeros((num_points, num_points))

# Mengisi matriks Hamiltonian
for i in range(1, num_points - 1):
    H[i, i] = -2 * hbar**2 / (2 * m * dx**2) + V[i]
    H[i, i - 1] = hbar**2 / (2 * m * dx**2)
    H[i, i + 1] = hbar**2 / (2 * m * dx**2)

# Menghitung eigenvalue dan eigenvector
eigenvalues, eigenvectors = np.linalg.eigh(H)

# Visualisasi fungsi gelombang untuk energi rendah
plt.figure(figsize=(10, 6))
for n in range(3):
    plt.plot(x, eigenvectors[:, n]**2, label=f'Level Energi {n+1} (E = {eigenvalues[n]:.2e} J)')

# Plot potensi
plt.plot(x, V / V0, color='black', label="Potensi (V(x))", linestyle='--')

plt.title('Fungsi Gelombang pada Penghalang Potensial')
plt.xlabel('Posisi (m)')
plt.ylabel('Probabilitas (|ψ(x)|²)')
plt.legend()
plt.grid(True)
plt.show()
