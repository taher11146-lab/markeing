import matplotlib.pyplot as plt
import numpy as np
from matplotlib.collections import LineCollection
from matplotlib.colors import LinearSegmentedColormap

# 1. دالة ذكية ومتقدمة لتوزيع التدرج اللوني بزاوية ديناميكية لمحاكاة لمعان المعدن (Chrome Effect)
def draw_premium_chrome_line(ax, x, y, colors, lw=20):
    points = np.array([x, y]).T.reshape(-1, 1, 2)
    segments = np.concatenate([points[:-1], points[1:]], axis=1)

    # بناء تدرج مخصص يعتمد على المسار الهندسي ليعطي بريقاً حقيقياً
    cmap = LinearSegmentedColormap.from_list("chrome_gold", colors, N=512)
    norm = plt.Normalize(0, len(x))

    lc = LineCollection(segments, cmap=cmap, norm=norm, linewidth=lw, zorder=3)
    lc.set_capstyle('round')
    lc.set_array(np.arange(len(x)))
    ax.add_collection(lc)

# 2. تهيئة لوحة الرسم الاحترافية بأعلى معايير التباين البصري وخلفية كحلية ليلاً (#050C1A)
fig, ax = plt.subplots(figsize=(8, 9), facecolor='#050C1A')
ax.set_facecolor('#050C1A')

# 3. لوحات ألوان "الفخامة المطلقة" الرقمية المعدلة للانعكاس الضوئي
# تدرج أزرق ملكي سيبراني مشرق في الأطراف ونقي في المنتصف
cyber_blue = ['#0D2354', '#1E3A8A', '#3B82F6', '#1E3A8A', '#0D2354']
# تدرج الذهب الكرومي الفاخر المحاكي لسبائك الذهب النقي
chrome_gold = ['#735613', '#D4AF37', '#FFF3B3', '#D4AF37', '#9E781D', '#FFF3B3', '#543F0C']

# 4. الحسابات الرياضية المتقدمة للمسارات الهندسية المتصلة
t = np.linspace(0, 2 * np.pi, 500)

# الدائرة العلوية لرقم 8 (بأبعاد ذهبية متناسقة)
x_top = 0.44 * np.cos(t) + 3.0
y_top = 0.44 * np.sin(t) + 3.42
draw_premium_chrome_line(ax, x_top, y_top, chrome_gold, lw=22)

# الدائرة السفلية لرقم 8
x_bottom = 0.56 * np.cos(t) + 3.0
y_bottom = 0.56 * np.sin(t) + 2.48
draw_premium_chrome_line(ax, x_bottom, y_bottom, chrome_gold, lw=22)

# الساق العمودي الأساسي لحرف P
x_stem = np.linspace(2.15, 2.15, 150)
y_stem = np.linspace(1.95, 3.90, 150)
draw_premium_chrome_line(ax, x_stem, y_stem, cyber_blue, lw=22)

# القوس المطور لحرف P الذي يتداخل بانسيابية متناهية ويلتف ليعانق الرقم 8
t_p = np.linspace(-np.pi / 2, np.pi / 2, 250)
x_loop = 0.42 * np.cos(t_p) + 2.15
y_loop = 0.42 * np.sin(t_p) + 3.45
draw_premium_chrome_line(ax, x_loop, y_loop, cyber_blue, lw=22)

# 5. طباعة التايبوغرافي الفخم لاسم الوكالة (Typography Section)
# اسم العلامة الأساسي بخط مشع متناسق
ax.text(2.65, 0.95, 'P8 MARKETING', fontsize=45, fontweight='bold',
        color='#D4AF37', ha='center', va='center', fontname='sans-serif', zorder=5)

# التوصيف الوظيفي للوكالة بالتوزيع الرقمي المنفصل ليعطي طابع العالمية
subtitle = 'DIGITAL PERFORMANCE AGENCY'
spaced = ' '.join(list(subtitle))
ax.text(2.65, 0.60, spaced, fontsize=9.5, fontweight='medium',
        color='#A0AEC0', ha='center', va='center', fontname='sans-serif', zorder=5)

# 6. ضبط لوحة العرض وإلغاء المحاور والأطراف الميتة تماماً
ax.axis('off')
ax.set_xlim(1.2, 4.1)
ax.set_ylim(0.2, 4.5)

# 7. تصدير التحفة الفنية بأعلى دقة متجهة بدون أي بكسلة وخلفية مدمجة فاخرة
plt.savefig('P8_Marketing_Masterpiece_Logo.png', dpi=400, bbox_inches='tight', pad_inches=0.2,
            facecolor=fig.get_facecolor(), edgecolor='none')

print("تم بنجاح توليد النموذج الأكثر تميزاً وفخامة وحفظه باسم: P8_Marketing_Masterpiece_Logo.png")
