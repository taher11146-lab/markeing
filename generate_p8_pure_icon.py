import matplotlib.pyplot as plt
import numpy as np
from matplotlib.collections import LineCollection
from matplotlib.colors import LinearSegmentedColormap

# 1. دالة لرسم مسارات هندسية بتدرج ناعم يعكس لمعان المعدن الفاخر (Chrome Gold)
def draw_pure_p8_icon(ax, x, y, colors, lw=22):
    points = np.array([x, y]).T.reshape(-1, 1, 2)
    segments = np.concatenate([points[:-1], points[1:]], axis=1)

    cmap = LinearSegmentedColormap.from_list("p8_gold_gradient", colors, N=512)
    norm = plt.Normalize(0, len(x))

    lc = LineCollection(segments, cmap=cmap, norm=norm, linewidth=lw, capstyle='round')
    lc.set_array(np.arange(len(x)))
    ax.add_collection(lc)

# 2. إعداد مساحة الرسم بخلفية الويب الداكنة الفاخرة المعتمدة للوكالة
fig, ax = plt.subplots(figsize=(7, 7), facecolor='#0B132B')
ax.set_facecolor('#0B132B')

# 3. لوحة تدرج الذهب الكرومي النقي (محاكاة بريق المعدن الذهبي المصقول)
premium_gold = ['#735613', '#D4AF37', '#FFF3B3', '#D4AF37', '#9E781D', '#FFF3B3', '#543F0C']

# 4. الحسابات الرياضية المتقدمة لضبط مراكز التداخل لرمز P8
t = np.linspace(0, 2 * np.pi, 400)

# هندسة الدائرة العلوية للرقم 8
x_top = 0.45 * np.cos(t) + 3.0
y_top = 0.45 * np.sin(t) + 3.4
draw_pure_p8_icon(ax, x_top, y_top, premium_gold, lw=22)

# هندسة الدائرة السفلية للرقم 8
x_bottom = 0.55 * np.cos(t) + 3.0
y_bottom = 0.55 * np.sin(t) + 2.5
draw_pure_p8_icon(ax, x_bottom, y_bottom, premium_gold, lw=22)

# هندسة الخط العمودي الأساسي (Stem) لحرف P
x_stem = np.linspace(2.2, 2.2, 100)
y_stem = np.linspace(2.0, 3.85, 100)
draw_pure_p8_icon(ax, x_stem, y_stem, premium_gold, lw=22)

# هندسة قوس حرف P الملتف بتداخل متزن ومباشر مع الرقم 8
t_arc = np.linspace(-np.pi / 2, np.pi / 2, 200)
x_arc = 0.42 * np.cos(t_arc) + 2.2
y_arc = 0.42 * np.sin(t_arc) + 3.43
draw_pure_p8_icon(ax, x_arc, y_arc, premium_gold, lw=22)

# 5. تنظيف لوحة الرسم وإلغاء المحاور والأطراف تماماً لتركيز الرمز كأيقونة مستقلة
ax.axis('off')
ax.set_xlim(1.3, 4.0)
ax.set_ylim(1.4, 4.3)

# 6. تصدير وحفظ الأيقونة بأعلى دقة متجهة بدون حواف ميتة للاستخدام المباشر
plt.savefig('P8_Pure_Gold_Icon.png', dpi=400, bbox_inches='tight', pad_inches=0.1, facecolor=fig.get_facecolor(), edgecolor='none')
plt.show()

print("تم بنجاح تصدير وحفظ أيقونة P8 الصافية بدقة فائقة باسم: P8_Pure_Gold_Icon.png")
