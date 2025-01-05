import numpy as np
import matplotlib.pyplot as plt

# Parameter dasar
hbar = 1.0  # konstanta Planck tereduksi (dalam satuan natural)
m = 1.0     # massa partikel (dalam satuan natural)
L = 10.0    # panjang sumur atau panjang tangga potensial
V0 = 10.0   # tinggi potensi tangga
E = 2.0     # energi partikel

# Fungsi gelombang dalam sumur potensial tak terbatas
def wave_function(x, n, L):
    """ Fungsi gelombang untuk sumur potensial tak terbatas """
    if 0 <= x <= L:
        return np.sqrt(2/L) * np.sin(n * np.pi * x / L)
    else:
        return 0

# Fungsi untuk sumur potensial terbatas
def finite_well_wave_function(x, L, V0, E):
    """ Fungsi gelombang untuk sumur potensial terbatas """
    if 0 <= x <= L:
        # Dalam sumur, potensi V(x) = 0, jadi fungsi gelombang sinusoidal
        return np.sqrt(2/L) * np.sin(np.pi * x / L)
    else:
        # Di luar sumur, potensi V(x) > E, jadi fungsi gelombang teredam
        kappa = np.sqrt(2 * m * (V0 - E) / hbar**2)
        return np.exp(-kappa * abs(x - L))

# Fungsi untuk tangga potensial
def potential_step_wave_function(x, V0, E):
    """ Fungsi gelombang untuk tangga potensial """
    if x < 0:
        # Daerah kiri tangga (energi E lebih besar dari potensi)
        return np.cos(np.sqrt(2 * m * E) * x / hbar)
    else:
        # Daerah kanan tangga (energi E lebih kecil dari potensi)
        if E < V0:
            kappa = np.sqrt(2 * m * (V0 - E) / hbar**2)
            return np.exp(-kappa * x)  # Fungsi gelombang teredam
        else:
            return np.cos(np.sqrt(2 * m * (E - V0)) * x / hbar)

# Membuat sumbu x untuk plot
x_values = np.linspace(-L, 2*L, 500)

# Plot Sumur Potensial Terbatas
y_values_sumur = [finite_well_wave_function(x, L, V0, E) for x in x_values]

# Plot Tangga Potensial
y_values_tangga = [potential_step_wave_function(x, V0, E) for x in x_values]

# Visualisasi
fig, axs = plt.subplots(2, 1, figsize=(8, 8))

# Plot Sumur Potensial Terbatas
axs[0].plot(x_values, y_values_sumur, label="Fungsi Gelombang (Sumur Potensial Terbatas)")
axs[0].set_title("Sumur Potensial Terbatas")
axs[0].set_xlabel("Posisi (x)")
axs[0].set_ylabel("Fungsi Gelombang")
axs[0].legend()

# Plot Tangga Potensial
axs[1].plot(x_values, y_values_tangga, label="Fungsi Gelombang (Tangga Potensial)", color='orange')
axs[1].set_title("Tangga Potensial")
axs[1].set_xlabel("Posisi (x)")
axs[1].set_ylabel("Fungsi Gelombang")
axs[1].legend()

plt.tight_layout()
plt.show()
