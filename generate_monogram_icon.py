import matplotlib.pyplot as plt
import numpy as np
from matplotlib.collections import LineCollection
from matplotlib.colors import LinearSegmentedColormap

# 1. دالة مخصصة لإنشاء ورسم خطوط هندسية بتدرج لوني انسيابي ناعم
def draw_pure_monogram_gradient(ax, x, y, colors, lw=20):
    points = np.array([x, y]).T.reshape(-1, 1, 2)
    segments = np.concatenate([points[:-1], points[1:]], axis=1)

    # بناء لوحة التدرج اللوني الرقمي بناءً على مدخلات الـ HEX
    cmap = LinearSegmentedColormap.from_list("p8_pure_gradient", colors, N=256)
    norm = plt.Normalize(0, len(x))

    # رسم المسار المتجهي بأطراف دائرية مرنة ومترابطة
    lc = LineCollection(segments, cmap=cmap, norm=norm, linewidth=lw)
    lc.set_capstyle('round')
    lc.set_array(np.arange(len(x)))
    ax.add_collection(lc)

# 2. تهيئة مساحة الرسم بنسبة أبعاد مربعة تماماً (1:1) تناسب أيقونات المواقع والتطبيقات
fig, ax = plt.subplots(figsize=(7, 7), facecolor='#0B132B')
ax.set_facecolor('#0B132B')

# 3. تحديد تدرجات الألوان الحصرية الملكية (مجموعة الفخامة والثقة)
blue_palette = ['#102A63', '#1E3A8A', '#4285F4']  # التدرج البصري للأزرق الملكي
gold_palette = ['#8C6F23', '#D4AF37', '#FAE49E']  # التدرج المعدني للذهب المطفأ الفاخر

# 4. الحسابات الرياضية الدقيقة لمنحنيات الـ مونوغرام لضمان عدم وجود فجوات
theta = np.linspace(0, 2 * np.pi, 400)

# هندسة الدائرة العلوية للرقم 8
x_top = 0.45 * np.cos(theta) + 3.0
y_top = 0.45 * np.sin(theta) + 3.4
draw_pure_monogram_gradient(ax, x_top, y_top, gold_palette, lw=20)

# هندسة الدائرة السفلية للرقم 8
x_bottom = 0.55 * np.cos(theta) + 3.0
y_bottom = 0.55 * np.sin(theta) + 2.5
draw_pure_monogram_gradient(ax, x_bottom, y_bottom, gold_palette, lw=20)

# هندسة الخط العمودي الأساسي لحرف P
x_p_stem = np.linspace(2.2, 2.2, 120)
y_p_stem = np.linspace(2.0, 3.85, 120)
draw_pure_monogram_gradient(ax, x_p_stem, y_p_stem, blue_palette, lw=20)

# هندسة القوس الجانبي المكمل لحرف P والمتداخل هندسياً مع دوائر الـ 8
theta_p = np.linspace(-np.pi / 2, np.pi / 2, 200)
x_p_loop = 0.42 * np.cos(theta_p) + 2.2
y_p_loop = 0.42 * np.sin(theta_p) + 3.43
draw_pure_monogram_gradient(ax, x_p_loop, y_p_loop, blue_palette, lw=20)

# 5. تنظيف وتوسيط الكادر وإخفاء محاور الرسم لإبراز الرمز كأيقونة حرة
ax.axis('off')
ax.set_xlim(1.3, 4.0)
ax.set_ylim(1.5, 4.3)

# 6. تصدير الأيقونة بأعلى دقة متجهة وجودة وضوح للواجهات
plt.savefig('P8_Pure_Monogram_Icon.png', dpi=300, bbox_inches='tight', pad_inches=0.1,
            facecolor=fig.get_facecolor(), edgecolor='none')

print("تم استخراج وحفظ مونوغرام P8 الصافي كأيقونة بالاسم: P8_Pure_Monogram_Icon.png")
