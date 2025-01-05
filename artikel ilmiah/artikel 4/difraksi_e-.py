import numpy as np
import matplotlib.pyplot as plt

# Konstanta
h = 6.626e-34  # Konstanta Planck (Joule detik)
e = 1.602e-19  # Muatan elektron (Coulomb)
m_e = 9.11e-31  # Massa elektron (kg)
V = 100e3  # Tegangan percepatan (volt), 100 kV
d = 1e-6  # Jarak antar garis kisi (m)
theta_1_deg = 70  # Sudut difraksi pertama (derajat)

# Menghitung panjang gelombang (λ) menggunakan persamaan Bragg
theta_1_rad = np.radians(theta_1_deg)  # Mengubah sudut ke radian
lambda_broglie = 2 * d * np.sin(theta_1_rad)  # Panjang gelombang

# Menghitung momentum elektron (p)
p = h / lambda_broglie

# Menghitung energi kinetik (E_k)
E_k = p**2 / (2 * m_e)

# Menghitung energi dalam eV
E_k_eV = E_k / e  # Energi dalam eV

# Output hasil perhitungan
print(f"Panjang gelombang de Broglie: {lambda_broglie:.2e} m")
print(f"Energi Kinetik Elektron: {E_k:.2e} J")
print(f"Energi Kinetik Elektron: {E_k_eV:.2f} eV")

# Membuat visualisasi pola difraksi
x = np.linspace(-5, 5, 1000)
y = np.sinc(x / lambda_broglie)**2  # Fungsi sinc untuk pola difraksi

# Membuat plot dengan ukuran lebih kecil
fig, ax = plt.subplots(figsize=(12, 6))

# Menampilkan grafik pola difraksi
ax.plot(x, y, label=f"Pola Difraksi (λ = {lambda_broglie:.2e} m)")
ax.set_title("Pola Difraksi Elektron")
ax.set_xlabel("Posisi (m)")
ax.set_ylabel("Intensitas")
ax.legend()
plt.grid(True)

# Menambahkan teks penjelasan di samping grafik
text = f"""
Panjang Gelombang de Broglie: {lambda_broglie:.2e} m
Energi Kinetik Elektron: {E_k:.2e} J
Energi Kinetik Elektron: {E_k_eV:.2f} eV

Pola difraksi ini dihasilkan oleh elektron yang dipercepat
dengan tegangan 100 kV dan mengalami difraksi pada kisi
dengan jarak antar garis sebesar 1 μm. Sudut difraksi
pertama (n=1) adalah {theta_1_deg}.
"""

# Menambahkan teks di samping grafik
fig.text(0.75, 0.5, text, ha='left', va='center', fontsize=12, bbox=dict(facecolor='white', alpha=0.8, edgecolor='black'))

# Menampilkan grafik dan teks
plt.show()
