import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

# Konstanta
h = 6.626e-34  # Konstanta Planck (Joule detik)
me = 9.11e-31  # Massa elektron (kg)

# Fungsi untuk menghitung panjang gelombang de Broglie
def de_broglie_lambda(mass, velocity):
    return h / (mass * velocity)

# Membuat figure dengan dua kolom (grafik di kiri, kontainer teks di kanan)
fig, (ax, ax_text) = plt.subplots(1, 2, figsize=(12, 6))

# Mengatur sumbu untuk grafik
ax.set_xlim(0, 1e8)
ax.set_ylim(0, 1e-9)

# Menambahkan label untuk grafik
ax.set_xlabel("Kecepatan Partikel (m/s)")
ax.set_ylabel("Panjang Gelombang de Broglie (m)")
ax.set_title("Simulasi Hipotesis de Broglie")

# Menambahkan area kontainer teks di sebelah grafik
ax_text.axis('off')  # Menyembunyikan sumbu untuk area teks

# Menambahkan kotak teks (kontainer)
from matplotlib.patches import FancyBboxPatch

# Membuat kotak (kontainer) untuk teks
bbox = FancyBboxPatch((0, 0), 1, 1, boxstyle="round,pad=0.05", edgecolor="black", facecolor="lightgrey", lw=2)
ax_text.add_patch(bbox)

# Fungsi untuk memperbarui teks di kontainer
def update_text(velocity, mass, lambda_de_broglie):
    # Clear kontainer teks sebelum menambahkan teks baru
    ax_text.clear()
    ax_text.add_patch(bbox)  # Menambahkan kotak lagi setelah dibersihkan
    # Menambahkan teks di dalam kotak
    ax_text.text(0.05, 0.9, f"Kecepatan Partikel: {velocity:.2e} m/s\nMassa Partikel: {mass:.2e} kg\n" +
                 f"Panjang Gelombang de Broglie: {lambda_de_broglie:.2e} m", fontsize=12, color='black', va='top')

# Membuat slider untuk kecepatan dan massa
ax_slider_velocity = plt.axes([0.1, 0.02, 0.65, 0.03], facecolor='lightgoldenrodyellow')
slider_velocity = Slider(ax_slider_velocity, 'Kecepatan (m/s)', 1e5, 1e8, valinit=1e7)

# Slider massa (misalnya, kita bisa pilih antara massa elektron dan massa proton)
ax_slider_mass = plt.axes([0.1, 0.06, 0.65, 0.03], facecolor='lightgoldenrodyellow')
slider_mass = Slider(ax_slider_mass, 'Massa Partikel (kg)', 1e-30, 1e-27, valinit=me)

# Fungsi untuk update panjang gelombang dan grafik berdasarkan input kecepatan dan massa
def update(val):
    mass = slider_mass.val
    velocity = slider_velocity.val
    
    # Menghitung panjang gelombang de Broglie
    lambda_de_broglie = de_broglie_lambda(mass, velocity)
    
    # Update plot
    ax.clear()  # Clear the previous plot
    ax.plot(velocity, lambda_de_broglie, 'ro')  # Plot titik panjang gelombang
    ax.set_xlim(0, 1e8)
    ax.set_ylim(0, 1e-9)
    ax.set_xlabel("Kecepatan Partikel (m/s)")
    ax.set_ylabel("Panjang Gelombang de Broglie (m)")
    ax.set_title("Simulasi Hipotesis de Broglie")
    
    # Menambahkan garis horizontal untuk titik yang baru dihitung
    ax.plot([0, velocity], [lambda_de_broglie, lambda_de_broglie], 'r--', label=f'λ = {lambda_de_broglie:.2e} m')
    
    # Menampilkan garis teks untuk nilai panjang gelombang
    ax.text(velocity * 0.7, lambda_de_broglie, f"λ = {lambda_de_broglie:.2e} m", color='blue', fontsize=10)

    # Memperbarui teks di kontainer
    update_text(velocity, mass, lambda_de_broglie)

    # Update grafik setiap perubahan nilai
    fig.canvas.draw_idle()

# Hubungkan sliders dengan fungsi update
slider_velocity.on_changed(update)
slider_mass.on_changed(update)

# Menampilkan plot
plt.show()
