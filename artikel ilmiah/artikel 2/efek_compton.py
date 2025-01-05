import numpy as np
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec

# Konstanta
h = 6.626e-34  # Konstanta Planck (Joule detik)
e = 1.602e-19  # Muatan elektron (Coulomb)
c = 3e8  # Kecepatan cahaya (m/s)
me = 9.11e-31  # Massa elektron (kg)

# Data percobaan
lambda_initial = 0.05e-9  # Panjang gelombang foton awal (dalam meter)
theta = 60  # Sudut hamburan (derajat)

# Menghitung panjang gelombang setelah tumbukan (λ')
theta_radian = np.radians(theta)  # Mengubah sudut ke radian
delta_lambda = (h / (me * c)) * (1 - np.cos(theta_radian))  # Perubahan panjang gelombang
lambda_final = lambda_initial + delta_lambda  # Panjang gelombang setelah tumbukan

# Menghitung energi foton terhambur (E')
E_initial = h * c / lambda_initial  # Energi foton awal
E_final = h * c / lambda_final  # Energi foton setelah tumbukan
E_scattered = E_initial - E_final  # Energi foton terhambur

# Output hasil perhitungan
print(f"Panjang gelombang foton awal: {lambda_initial*1e9:.2f} nm")
print(f"Panjang gelombang foton setelah tumbukan: {lambda_final*1e9:.2f} nm")
print(f"Energi foton terhambur: {E_scattered/e:.2f} eV")

# Membuat layout dengan dua kolom (gridspec)
fig = plt.figure(figsize=(10, 6))
gs = GridSpec(1, 2, width_ratios=[2, 1])  # Grafik lebih lebar dari penjelasan

# Membuat subplot untuk grafik
ax = fig.add_subplot(gs[0])
ax.set_xlim(-1, 6)
ax.set_ylim(-1, 5)

# Menambahkan garis foton datang
ax.plot([0, 5], [0, 0], color='blue', lw=2, label='Foton Datang')

# Menambahkan lingkaran untuk elektron
electron_circle = plt.Circle((5, 0), 0.3, color='black', label='Elektron', zorder=5)
ax.add_patch(electron_circle)

# Menghitung koordinat akhir garis foton terhambur
photon_x = 5 + np.cos(theta_radian) * 5
photon_y = np.sin(theta_radian) * 5

# Menghitung koordinat akhir garis elektron terhambur
electron_x = 5 + np.cos(np.radians(90 - theta)) * 5
electron_y = -np.sin(np.radians(90 - theta)) * 5

# Menambahkan garis hamburan foton dan elektron
ax.plot([5, photon_x], [0, photon_y], color='red', lw=2, label='Hamburan Foton')
ax.plot([5, electron_x], [0, electron_y], color='black', lw=2, label='Hamburan Elektron')

# Menambahkan label dan legend
ax.set_title("Simulasi Efek Compton")
ax.set_xlabel("Posisi (x)")
ax.set_ylabel("Posisi (y)")
ax.legend()

# Menambahkan penjelasan dalam kotak di samping grafik
text_ax = fig.add_subplot(gs[1])
text_ax.axis('off')  # Mematikan sumbu untuk area teks

# Menambahkan teks penjelasan
text_ax.text(0.05, 0.9, "Rumus yang digunakan:\n", fontsize=12, ha='left')
text_ax.text(0.05, 0.75, "λ' - λ = (h / (m * c)) * (1 - cos(θ))\n", fontsize=12, ha='left')
text_ax.text(0.05, 0.6, "λ = λ' - (h / (m * c)) * (1 - cos(θ))", fontsize=12, ha='left')
text_ax.text(0.05, 0.45, f"Kecepatan cahaya (c) = {c} m/s", fontsize=12, ha='left')
text_ax.text(0.05, 0.35, f"Konstanta Planck (h) = {h} J·s", fontsize=12, ha='left')
text_ax.text(0.05, 0.25, f"Massa Elektron (me) = {me} kg", fontsize=12, ha='left')
text_ax.text(0.05, 0.15, f"Panjang Gelombang Foton Awal (λ) = {lambda_initial * 1e9:.2f} nm", fontsize=12, ha='left')
text_ax.text(0.05, 0.05, f"Panjang Gelombang Foton Setelah Tumbukan (λ') = {lambda_final * 1e9:.2f} nm", fontsize=12, ha='left')
text_ax.text(0.05, -0.05, f"Energi Foton Terhambur = {E_scattered / e:.2f} eV", fontsize=12, ha='left')

# Menampilkan plot
plt.tight_layout()
plt.show()