import numpy as np
import matplotlib.pyplot as plt

NAVY = "#050C1A"
GOLD = "#D4AF37"
BLUE = "#1E3A8A"

def draw_mark(ax, lw=26):
    ax.set_facecolor(NAVY)
    # 8 circles (gold)
    ax.add_patch(plt.Circle((235, 166), 46, fill=False, lw=lw,
                            edgecolor=GOLD, zorder=3, capstyle="round"))
    ax.add_patch(plt.Circle((235, 256), 56, fill=False, lw=lw,
                            edgecolor=GOLD, zorder=3, capstyle="round"))
    # P stem + arrow (blue): stem + 2 arrow segments
    ax.plot([140, 140], [280, 120], lw=lw, solid_capstyle="round", color=BLUE, zorder=4)
    ax.plot([140, 120], [120, 140], lw=lw, solid_capstyle="round", color=BLUE, zorder=4)
    ax.plot([140, 160], [120, 140], lw=lw, solid_capstyle="round", color=BLUE, zorder=4)
    # P arc: from (140,120) to (186,166) to (140,212) on circle centered (140,166) r=46
    ang = np.linspace(np.pi / 2, -np.pi, 300)  # sweep from top
    cx, cy, r = 140, 166, 46
    x = cx + r * np.cos(ang)
    y = cy + r * np.sin(ang)
    ax.plot(x, y, lw=lw, solid_capstyle="round", color=BLUE, zorder=4)
    ax.set_xlim(100, 300)
    ax.set_ylim(70, 340)
    ax.set_aspect("equal")
    ax.axis("off")

# mark only (favicon set)
for sz in (180, 96, 48, 32, 16):
    fig, ax = plt.subplots(figsize=(sz / 96, sz / 96), dpi=96, facecolor=NAVY)
    draw_mark(ax)
    fig.savefig(f"PER8/logo-mark_{sz}.png", dpi=96, facecolor=NAVY,
                edgecolor="none", bbox_inches="tight", pad_inches=0.02)
    plt.close(fig)
    print(f"saved PER8/logo-mark_{sz}.png")
