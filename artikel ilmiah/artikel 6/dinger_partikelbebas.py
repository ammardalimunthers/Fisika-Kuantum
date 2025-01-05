import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Parameter simulasi
L = 10           # Panjang ruang (domain), yaitu panjang dari area tempat partikel bergerak
N = 500          # Jumlah titik dalam domain, semakin besar N semakin halus resolusi ruang
dx = L / N       # Resolusi spasial, jarak antar titik dalam domain
x = np.linspace(0, L, N)  # Posisi dalam domain, membuat array dari 0 sampai L dengan N titik
dt = 0.05        # Interval waktu, perubahan waktu setiap frame animasi
Tmax = 50        # Total waktu untuk animasi, berapa banyak frame yang akan diputar
k0 = 5           # Bilangan gelombang awal, menentukan frekuensi ruang paket gelombang
A = 1             # Amplitudo awal, skala dari paket gelombang

# Konstanta fisika (dalam satuan alami)
hbar = 1          # Konstanta Planck tereduksi (hbar), yang diset 1 untuk mempermudah perhitungan
m = 1             # Massa partikel, diset 1 untuk penyederhanaan (satuan alami)

# Fungsi gelombang awal (paket gelombang)
def wave_packet(x, k0, A):
    """
    Fungsi untuk menghasilkan paket gelombang Gaussian.
    Menggunakan ekspresi A * exp(i*k0*x) * exp(-(x-L/2)^2 / 2),
    yang merupakan paket gelombang terlokalisasi di sekitar x = L/2.
    """
    return A * np.exp(1j * k0 * x) * np.exp(-(x - L/2)**2 / 2)

# Fungsi untuk menghitung evolusi gelombang menggunakan persamaan Schrödinger
def time_evolution(psi, dt, dx, hbar, m):
    """
    Fungsi untuk menghitung evolusi fungsi gelombang dalam waktu berdasarkan persamaan Schrödinger.
    Menggunakan transformasi Fourier untuk mengaplikasikan operator Hamiltonian dalam ruang gelombang.
    """
    # Menghitung bilangan gelombang dalam ruang Fourier
    k = np.fft.fftfreq(len(psi), dx) * 2 * np.pi  # Bilangan gelombang k
    k2 = k**2  # Kuadrat bilangan gelombang, digunakan dalam operator kinetik

    # Menghitung evolusi fungsi gelombang dalam ruang Fourier
    psi_k = np.fft.fft(psi)  # Transformasi Fourier dari fungsi gelombang
    psi_k *= np.exp(-1j * hbar * k2 * dt / (2 * m))  # Operator evolusi Schrödinger dalam ruang gelombang

    # Mengembalikan ke ruang posisi menggunakan transformasi Fourier terbalik
    return np.fft.ifft(psi_k)

# Inisialisasi fungsi gelombang awal
psi_0 = wave_packet(x, k0, A)  # Membuat fungsi gelombang awal, paket gelombang terlokalisasi

# Setup plot untuk visualisasi
fig, ax = plt.subplots(figsize=(8, 6))
line, = ax.plot(x, np.abs(psi_0)**2, label='Probabilitas |ψ(x,t)|²')  # Plot probabilitas |ψ(x,t)|²
ax.set_xlim(0, L)  # Membatasi sumbu x dari 0 sampai L
ax.set_ylim(0, 1.2 * np.max(np.abs(psi_0)**2))  # Membatasi sumbu y, sedikit lebih tinggi dari maksimum |ψ(x,t)|²
ax.set_xlabel('Posisi (x)')  # Label sumbu x
ax.set_ylabel('Probabilitas |ψ(x,t)|²')  # Label sumbu y
ax.set_title('Simulasi Partikel Bebas dengan Persamaan Schrödinger')  # Judul grafik

# Menambahkan teks penjelasan di samping grafik
explanation = """
Penjelasan Terkait dengan Gambar:
1. Paket Gelombang Awal: Pada awalnya, paket gelombang terlokalisasi di tengah ruang (x = L/2).
2. Evolusi Waktu: Paket gelombang menyebar seiring berjalannya waktu.
3. Probabilitas Posisi: Probabilitas keberadaan partikel pada posisi tertentu ditunjukkan dengan grafik |ψ(x,t)|².
4. Visualisasi: Puncak grafik menunjukkan area dengan probabilitas terbesar, di mana partikel lebih mungkin ditemukan.
5. Fisika Kuantum: Paket gelombang menggambarkan sifat gelombang-partikel dalam ruang.
"""
ax.text(0.75, 0.6, explanation, fontsize=10, bbox=dict(facecolor='white', alpha=0.8))  # Menambahkan penjelasan dalam teks

# Fungsi untuk animasi
def update(frame):
    """
    Fungsi update untuk animasi, yang akan dijalankan di setiap frame.
    Fungsi gelombang diperbarui dan probabilitasnya diplot ulang.
    """
    global psi_0  # Menyatakan bahwa psi_0 akan diubah dalam fungsi ini
    psi_0 = time_evolution(psi_0, dt, dx, hbar, m)  # Evolusi fungsi gelombang dalam waktu
    line.set_ydata(np.abs(psi_0)**2)  # Memperbarui data probabilitas pada grafik
    return line,  # Mengembalikan objek yang akan diperbarui di setiap frame

# Membuat animasi dengan interval tertentu (50 ms) dan banyak frame
ani = FuncAnimation(fig, update, frames=range(Tmax), interval=50, blit=True)

plt.show()  # Menampilkan animasi
