import numpy as np
import matplotlib.pyplot as plt

# Fungsi untuk menghitung energi tingkat n dalam atom hidrogen
def energy_hydrogen(n):
    # Energi dalam eV untuk atom hidrogen (model Bohr)
    return -13.6 / (n ** 2)

# Fungsi untuk menghitung panjang gelombang spektrum emisi
def wavelength_emission(n1, n2):
    # Menggunakan rumus Rydberg untuk menghitung panjang gelombang spektrum emisi
    Rydberg_constant = 1.097373e7  # dalam 1/m
    return 1 / (Rydberg_constant * (1 / (n1 ** 2) - 1 / (n2 ** 2)))

# Nilai n (bilangan kuantum utama) untuk tingkat energi
n_values = np.arange(1, 6)  # Tingkat energi n = 1, 2, 3, 4, 5

# Menghitung energi untuk tingkat-tingkat tersebut
energies = [energy_hydrogen(n) for n in n_values]

# Plotting Energi Tingkat
plt.figure(figsize=(8, 6))
plt.plot(n_values, energies, 'bo-', label='Energi Tingkat')
plt.axhline(0, color='black', linewidth=1)  # Garis energi nol
plt.title('Tingkat Energi Atom Hidrogen')
plt.xlabel('Bilangan Kuantum (n)')
plt.ylabel('Energi (eV)')
plt.grid(True)
plt.legend()
plt.show()

# Menghitung spektrum emisi untuk transisi antar tingkat
n_max = 5  # Maksimum tingkat energi untuk simulasi
transitions = []

# Menghitung panjang gelombang spektrum untuk transisi dari n2 ke n1
for n2 in range(2, n_max + 1):
    for n1 in range(1, n2):
        wavelength = wavelength_emission(n1, n2)
        transitions.append((n1, n2, wavelength))

# Plotting Spektrum Emisi
plt.figure(figsize=(8, 6))
for n1, n2, wavelength in transitions:
    plt.plot([wavelength, wavelength], [n1, n2], color='red', linewidth=2)

plt.title('Spektrum Emisi Atom Hidrogen')
plt.xlabel('Panjang Gelombang (m)')
plt.ylabel('Transisi Tingkat Energi (n1 -> n2)')
plt.grid(True)
plt.show()