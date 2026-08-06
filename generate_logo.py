import matplotlib.pyplot as plt
import numpy as np
from matplotlib.collections import LineCollection
from matplotlib.colors import LinearSegmentedColormap

# 1. دالة مخصصة لرسم خطوط بتدرج لوني انسيابي مخصص ومحسّن
def draw_brand_gradient(ax, x, y, colors, lw=18):
    points = np.array([x, y]).T.reshape(-1, 1, 2)
    segments = np.concatenate([points[:-1], points[1:]], axis=1)

    # بناء التدرج اللوني الرقمي
    cmap = LinearSegmentedColormap.from_list("brand_mix", colors, N=256)
    norm = plt.Normalize(0, len(x))

    lc = LineCollection(segments, cmap=cmap, norm=norm, linewidth=lw)
    lc.set_capstyle('round')
    lc.set_array(np.arange(len(x)))
    ax.add_collection(lc)

# 2. تهيئة لوحة الرسم بالخلفية الكحلية الرسمية للوكالة (#0B132B)
fig, ax = plt.subplots(figsize=(8, 9), facecolor='#0B132B')
ax.set_facecolor('#0B132B')

# 3. تحديد لوحات التدرج اللوني (مجموعة الفخامة والثقة)
blue_shades = ['#102A63', '#1E3A8A', '#4285F4']  # تدرج الأزرق الملكي الرقمي
gold_shades = ['#8C6F23', '#D4AF37', '#FAE49E']  # تدرج الذهب المعدني الفاخر

# 4. حساب المسارات الهندسية الدقيقة لدمج P8
theta = np.linspace(0, 2 * np.pi, 350)

# الدائرة العلوية للرقم 8 (التدرج الذهبي)
x_top = 0.45 * np.cos(theta) + 3.0
y_top = 0.45 * np.sin(theta) + 3.4
draw_brand_gradient(ax, x_top, y_top, gold_shades, lw=18)

# الدائرة السفلية للرقم 8 (التدرج الذهبي)
x_bottom = 0.55 * np.cos(theta) + 3.0
y_bottom = 0.55 * np.sin(theta) + 2.5
draw_brand_gradient(ax, x_bottom, y_bottom, gold_shades, lw=18)

# العمود العمودي لحرف P (التدرج الأزرق)
x_p_line = np.linspace(2.2, 2.2, 100)
y_p_line = np.linspace(2.0, 3.85, 100)
draw_brand_gradient(ax, x_p_line, y_p_line, blue_shades, lw=18)

# القوس المنحني المكمل لحرف P والمتداخل مع رقم 8
theta_p = np.linspace(-np.pi / 2, np.pi / 2, 150)
x_p_arc = 0.42 * np.cos(theta_p) + 2.2
y_p_arc = 0.42 * np.sin(theta_p) + 3.43
draw_brand_gradient(ax, x_p_arc, y_p_arc, blue_shades, lw=18)

# 5. طباعة الخطوط والنصوص الرسمية (Typography) أسفل الرمز المعماري
# اسم الكيان التجاري الأساسي
ax.text(2.65, 1.1, 'PER8', fontsize=46, fontweight='bold',
        color='#D4AF37', ha='center', va='center', fontname='sans-serif')

# التوصيف العملي للوكالة بالتوزيع المتباعد العصري (letterspacing ليس مدعوماً في matplotlib)
subtitle = 'GLOBAL DIGITAL MARKETING AGENCY'
spaced = ' '.join(list(subtitle))
ax.text(2.65, 0.75, spaced, fontsize=9, fontweight='medium',
        color='#F3F4F6', ha='center', va='center', fontname='sans-serif')

# 6. تهيئة الهوامش والمحاور لضمان دقة الطباعة والتصدير
ax.axis('off')
ax.set_xlim(1.2, 4.1)
ax.set_ylim(0.4, 4.5)

# 7. تصدير وحفظ الشعار الفاخر بأعلى دقة متجهة بدون حواف ميتة
plt.savefig('PER8_Official_Corporate_Logo.png', dpi=300, bbox_inches='tight',
            facecolor=fig.get_facecolor(), edgecolor='none')

print("تم حفظ الشعار البرمجي الرسمي بنجاح تحت اسم: PER8_Official_Corporate_Logo.png")
