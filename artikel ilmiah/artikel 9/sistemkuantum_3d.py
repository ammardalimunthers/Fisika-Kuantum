import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Parameter
hbar = 1.0545718e-34  # Konstanta Planck tereduksi (J.s)
m = 9.10938356e-31    # Massa elektron (kg)
L = 1e-10             # Panjang sisi kubus (m)
V0 = 1e20             # Potensial besar (J)
num_points = 30       # Jumlah titik grid per dimensi
x_min, x_max = -L/2, L/2  # Batas grid

# Membuat grid 3D
x = np.linspace(x_min, x_max, num_points)
y = np.linspace(x_min, x_max, num_points)
z = np.linspace(x_min, x_max, num_points)

X, Y, Z = np.meshgrid(x, y, z)
dx = x[1] - x[0]  # Jarak antar titik

# Potensial (kotak 3D)
V = np.zeros((num_points, num_points, num_points))
V[int(num_points/4):int(3*num_points/4), int(num_points/4):int(3*num_points/4), int(num_points/4):int(3*num_points/4)] = V0

# Matriks Hamiltonian
H = np.zeros((num_points**3, num_points**3))

# Fungsi untuk mengubah indeks 3D menjadi 1D
def index(i, j, k):
    return i * num_points**2 + j * num_points + k

# Mengisi matriks Hamiltonian (beda hingga 3D)
for i in range(1, num_points - 1):
    for j in range(1, num_points - 1):
        for k in range(1, num_points - 1):
            idx = index(i, j, k)
            H[idx, idx] = -6 / (dx**2) + V[i, j, k]  # Energi diagonal (termasuk potensi)
            if i > 0:
                H[idx, index(i-1, j, k)] = 1 / (dx**2)
            if i < num_points - 1:
                H[idx, index(i+1, j, k)] = 1 / (dx**2)
            if j > 0:
                H[idx, index(i, j-1, k)] = 1 / (dx**2)
            if j < num_points - 1:
                H[idx, index(i, j+1, k)] = 1 / (dx**2)
            if k > 0:
                H[idx, index(i, j, k-1)] = 1 / (dx**2)
            if k < num_points - 1:
                H[idx, index(i, j, k+1)] = 1 / (dx**2)

# Menghitung eigenvalue dan eigenvector
eigenvalues, eigenvectors = np.linalg.eigh(H)

# Mengambil eigenvector untuk energi terendah
ground_state = eigenvectors[:, 0].reshape((num_points, num_points, num_points))

# Visualisasi fungsi gelombang untuk salah satu slice
fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111, projection='3d')

# Menampilkan fungsi gelombang pada satu lapisan (slice) z = 0
X_slice, Y_slice = np.meshgrid(x, y)
Z_slice = ground_state[num_points//2, :, :]

# Plot fungsi gelombang
ax.plot_surface(X_slice, Y_slice, Z_slice, cmap='viridis', edgecolor='k')

# Label dan title
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('ψ(x, y, z)')
ax.set_title('Fungsi Gelombang pada Sistem Kuantum 3D')

# Menampilkan energi terendah di samping gambar
ax.text2D(0.05, 0.95, f'Energi terendah: {eigenvalues[0]:.2e} J', transform=ax.transAxes)

plt.show()

# Menampilkan energi terendah di terminal
print(f"Energi terendah: {eigenvalues[0]:.2e} J")
