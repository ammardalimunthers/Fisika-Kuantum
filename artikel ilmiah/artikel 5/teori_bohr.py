import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.gridspec import GridSpec

# Data untuk orbit dan energi
orbits = [1, 2, 3, 4]  # Orbit yang akan divisualisasikan
colors = ['gold', 'deepskyblue', 'limegreen', 'red']  # Warna orbit
energy_levels = [-13.6 / n**2 for n in orbits]  # Energi masing-masing orbit

# Setup grid untuk animasi dan teks penjelasan
fig = plt.figure(figsize=(12, 6))
gs = GridSpec(1, 2, width_ratios=[2, 1])

# Plot area animasi (kiri)
ax_anim = fig.add_subplot(gs[0, 0])
ax_anim.set_xlim(-5, 5)
ax_anim.set_ylim(-5, 5)
ax_anim.set_aspect('equal')
ax_anim.axis('off')

# Plotkan inti atom
nucleus = plt.Circle((0, 0), 0.2, color='black')
ax_anim.add_artist(nucleus)

# Plotkan orbit
orbit_circles = [plt.Circle((0, 0), n, color=colors[i], fill=False, lw=1.5) for i, n in enumerate(orbits)]
for circle in orbit_circles:
    ax_anim.add_artist(circle)

# Elektron
electron, = ax_anim.plot([], [], 'o', color='blue', markersize=8)

# Teks energi
energy_text = ax_anim.text(-4.5, -4.5, '', fontsize=12, color='black')

# Plot area penjelasan (kanan)
ax_text = fig.add_subplot(gs[0, 1])
ax_text.axis('off')

# Teks penjelasan teori
explanation = """
**Teori Atom Bohr**:
1. Elektron mengelilingi inti atom pada orbit tertentu.
2. Orbit ditentukan oleh tingkat energi tertentu (n = 1, 2, 3, ...).
3. Energi masing-masing orbit dihitung dengan rumus: E = -13.6/n^2 eV.
4. Elektron dapat berpindah antara orbit jika menyerap atau melepaskan energi.

Pada visualisasi:
- Inti atom (hitam) merepresentasikan proton dan neutron.
- Orbit berwarna menggambarkan jalur elektron.
- Elektron biru bergerak di salah satu orbit dengan energi yang sesuai.

Tingkat Energi:
- Orbit 1 (n=1): {0:.2f} eV
- Orbit 2 (n=2): {1:.2f} eV
- Orbit 3 (n=3): {2:.2f} eV
- Orbit 4 (n=4): {3:.2f} eV
""".format(*energy_levels)

# Tambahkan teks ke area kanan
ax_text.text(0, 0.5, explanation, fontsize=10, va='center', ha='left', wrap=True)

# Fungsi untuk animasi
def update(frame):
    n = frame % len(orbits) + 1  # Orbit saat ini
    theta = np.radians(frame * 10)  # Sudut rotasi elektron
    x, y = [n * np.cos(theta)], [n * np.sin(theta)]  # Koordinat elektron
    electron.set_data(x, y)

    # Perbarui teks energi
    energy_text.set_text(f'Level Energi: {energy_levels[n - 1]:.2f} eV')

    return electron, energy_text

# Jalankan animasi dengan interval lebih lambat
ani = FuncAnimation(fig, update, frames=range(0, 360), interval=500, blit=True)

plt.tight_layout()
plt.show()