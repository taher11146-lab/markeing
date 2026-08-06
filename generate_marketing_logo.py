import matplotlib.pyplot as plt
import numpy as np
from matplotlib.collections import LineCollection
from matplotlib.colors import LinearSegmentedColormap

def draw_brand_gradient(ax, x, y, colors, lw=18):
    points = np.array([x, y]).T.reshape(-1, 1, 2)
    segments = np.concatenate([points[:-1], points[1:]], axis=1)
    cmap = LinearSegmentedColormap.from_list("brand_mix", colors, N=256)
    norm = plt.Normalize(0, len(x))
    lc = LineCollection(segments, cmap=cmap, norm=norm, linewidth=lw)
    lc.set_capstyle('round')
    lc.set_array(np.arange(len(x)))
    ax.add_collection(lc)

fig, ax = plt.subplots(figsize=(8, 9), facecolor='#0B132B')
ax.set_facecolor('#0B132B')

blue_shades = ['#102A63', '#1E3A8A', '#4285F4']
gold_shades = ['#8C6F23', '#D4AF37', '#FAE49E']

theta = np.linspace(0, 2 * np.pi, 350)
x_top = 0.45 * np.cos(theta) + 3.0
y_top = 0.45 * np.sin(theta) + 3.4
draw_brand_gradient(ax, x_top, y_top, gold_shades, lw=18)

x_bottom = 0.55 * np.cos(theta) + 3.0
y_bottom = 0.55 * np.sin(theta) + 2.5
draw_brand_gradient(ax, x_bottom, y_bottom, gold_shades, lw=18)

x_p_line = np.linspace(2.2, 2.2, 100)
y_p_line = np.linspace(2.0, 3.85, 100)
draw_brand_gradient(ax, x_p_line, y_p_line, blue_shades, lw=18)

theta_p = np.linspace(-np.pi / 2, np.pi / 2, 150)
x_p_arc = 0.42 * np.cos(theta_p) + 2.2
y_p_arc = 0.42 * np.sin(theta_p) + 3.43
draw_brand_gradient(ax, x_p_arc, y_p_arc, blue_shades, lw=18)

ax.text(2.65, 1.1, 'P8 MARKETING', fontsize=44, fontweight='bold', color='#D4AF37', ha='center', va='center')

subtitle = 'DIGITAL PERFORMANCE AGENCY'
spaced = ' '.join(list(subtitle))
ax.text(2.65, 0.75, spaced, fontsize=9, color='#F3F4F6', ha='center', va='center')

ax.axis('off')
ax.set_xlim(1.2, 4.1)
ax.set_ylim(0.4, 4.5)

plt.savefig('P8_MARKETING_Official_Logo.png', dpi=300, bbox_inches='tight',
            facecolor=fig.get_facecolor(), edgecolor='none')

print("تم حفظ شعار P8 MARKETING الرسمي: P8_MARKETING_Official_Logo.png")
