import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
import matplotlib.patches as patches
from matplotlib.offsetbox import OffsetImage, AnnotationBbox

# Konstanta
h = 6.626e-34  # Konstanta Planck (Joule detik)
e = 1.602e-19  # Muatan elektron (Coulomb)
c = 3e8  # Kecepatan cahaya (m/s)

# Frekuensi cahaya (Hz)
freq = np.linspace(4e14, 1e15, 500)  # Frekuensi dari 4e14 Hz hingga 1e15 Hz

# Fungsi kerja logam awal (dalam Joule)
Φ_default = 2.5 * e

# Energi foton (E = hf)
E_foton = h * freq

# Fungsi untuk menghitung energi kinetik
def calculate_KE(Φ):
    KE = E_foton - Φ
    KE[KE < 0] = 0
    return KE / e  # Energi kinetik dalam eV

# Data awal
KE = calculate_KE(Φ_default)

# Membuat plot
fig, ax = plt.subplots(figsize=(6, 4))
plt.subplots_adjust(left=0.1, right=0.45, bottom=0.25)

# Plot awal
line, = ax.plot(freq, KE, label='Energi Kinetik Elektron (eV)', color='blue')
threshold_line = ax.axvline(x=Φ_default / h, color='red', linestyle='--', label=f'Frekuensi Ambang = {Φ_default / h:.2e} Hz')
ax.set_title('Simulasi Dinamis Efek Fotolistrik')
ax.set_xlabel('Frekuensi Cahaya (Hz)')
ax.set_ylabel('Energi Kinetik Elektron (eV)')
ax.grid(True)
ax.legend()

# Slider untuk fungsi kerja
ax_slider = plt.axes([0.1, 0.1, 0.35, 0.03])
slider = Slider(ax_slider, 'Fungsi Kerja (eV)', 1, 5, valinit=Φ_default / e)

# Membuat kontainer untuk penjelasan di samping grafik
ax_container = plt.axes([0.5, 0.25, 0.45, 0.5])
ax_container.set_xlim(0, 1)
ax_container.set_ylim(0, 1)
ax_container.axis('off')

# Tambahkan kotak kontainer dengan teks penjelasan
explanation_text = (
    "Frekuensi ambang (f_0) adalah nilai frekuensi minimum cahaya yang diperlukan untuk \n"
    "melepaskan elektron dari permukaan logam.\n"
    "Frekuensi ini dihitung menggunakan persamaan: \n"
    "\n"
    "    f_0 = Φ / h \n"
    "\n"
    "Di mana:\n"
    "- Φ: Fungsi kerja logam (dalam Joule)\n"
    "- h: Konstanta Planck (6.626e-34 Js)\n"
    "\n"
    "Pada awal simulasi, Φ = 2.5 eV, sehingga f_0 \u2248 6.00e+14 Hz.\n"
    "Garis vertikal merah menandai frekuensi ambang ini.\n"
)

# Gambar kotak
rect = patches.Rectangle((0, 0), 1, 1, linewidth=1, edgecolor='black', facecolor='lightgrey')
ax_container.add_patch(rect)

# Tambahkan teks ke dalam kotak
ax_container.text(0.05, 0.95, explanation_text, fontsize=8, family='monospace', va='top')

# Tambahkan gambar di bawah teks
image_path = "Sejarah-Penemuan-Efek-Fotolistrik-768x318.webp"
img = plt.imread(image_path)
image_ax = fig.add_axes([0.5, 0.05, 0.45, 0.2])  # Lokasi untuk menempatkan gambar
image_ax.imshow(img)
image_ax.axis('off')

# Fungsi update
def update(val):
    Φ = slider.val * e  # Konversi dari eV ke Joule
    KE = calculate_KE(Φ)
    line.set_ydata(KE)
    threshold_line.set_xdata([Φ / h])  # Update garis frekuensi ambang
    threshold_line.set_label(f'Frekuensi Ambang = {Φ / h:.2e} Hz')
    ax.legend()
    fig.canvas.draw_idle()

# Hubungkan slider dengan fungsi update
slider.on_changed(update)

plt.show()