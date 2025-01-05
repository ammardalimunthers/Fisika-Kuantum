import numpy as np
import matplotlib.pyplot as plt

# Parameter
hbar = 1.0545718e-34  # Konstanta Planck tereduksi (J.s)
m = 9.10938356e-31    # Massa elektron (kg)
sigma_x = 1e-10       # Ketidakpastian posisi (m)
x0 = 0                # Posisi awal paket gelombang (m)
p0 = 1e-24            # Momentum awal paket gelombang (kg.m/s)
num_points = 200      # Jumlah titik pada grid
L = 5e-10             # Panjang domain (m)
x = np.linspace(-L/2, L/2, num_points)  # Grid posisi

# Fungsi untuk menghitung paket gelombang Gaussian
def gaussian_wave_packet(x, x0, p0, sigma_x):
    # Gaussian wave packet untuk posisi dan momentum
    sigma_p = hbar / (2 * sigma_x)  # Ketidakpastian momentum
    prefactor = (1 / (2 * np.pi * sigma_x ** 2)) ** 0.25
    exponent = - (x - x0) ** 2 / (2 * sigma_x ** 2) + 1j * p0 * (x - x0) / hbar
    return prefactor * np.exp(exponent)

# Fungsi untuk evolusi waktu paket gelombang
def evolve_wave_packet(wave_packet, t, p0, sigma_x, m):
    # Evolusi paket gelombang dengan mempertimbangkan momentum p0
    delta_x = hbar * t / (2 * m * sigma_x**2)
    return wave_packet * np.exp(-1j * p0 * t / hbar) * np.exp(-1j * delta_x)

# Simulasi paket gelombang pada waktu t = 0 dan t = 1e-16 detik
t0 = 0
t1 = 1e-16  # Waktu berikutnya

# Menghitung paket gelombang pada t0
wave_packet_t0 = gaussian_wave_packet(x, x0, p0, sigma_x)

# Menghitung paket gelombang pada t1
wave_packet_t1 = evolve_wave_packet(wave_packet_t0, t1, p0, sigma_x, m)

# Visualisasi paket gelombang pada waktu t0 dan t1
fig, ax = plt.subplots(figsize=(10, 6))

# Plot paket gelombang pada t = 0
ax.plot(x, np.abs(wave_packet_t0)**2, label="t = 0", color='blue', linewidth=2)

# Plot paket gelombang pada t = t1
ax.plot(x, np.abs(wave_packet_t1)**2, label="t = 1e-16 s", color='red', linewidth=2)

# Menambahkan label dan title
ax.set_xlabel("Posisi (m)")
ax.set_ylabel("Probabilitas Posisi $|\psi(x)|^2$")
ax.set_title("Simulasi Paket Gelombang Evolusi Waktu")
ax.legend()

# Menampilkan plot
plt.show()
