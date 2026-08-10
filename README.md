# PER8 — هندسة التسويق العالمي بأبعادها الثمانية

منظومة تسويق رقمية متكاملة: `PER8` (المنصة الرئيسية) و `P8_MARKETING` (وكالة الأداء الرقمي) — مبنية كموقعين ثابتين (Static) على GitHub Pages.

**على الهواء مباشرة:** https://taher11146-lab.github.io/markeing/

## البنية
```
index.html            بوابة الربط بين الموقعين (+ OG/social tags + sitemap)
PER8/                 المنصة الرئيسية: 8Ps، سلم العروض (فحص/ركيزة/منظومة)، واتساب
P8_MARKETING/         وكالة الأداء: مصفوفة 8Ps + محرك ROI تفاعلي + فحص مجاني
docs/                 الأدلة التشغيلية والتدريبية (انظر الأسفل)
PER8/logo-mark.svg    الشعار الرسمي (سهم P + 8 ذهبي) ومجموعة أيقونات 16-512
```

## النشر
الصفحات تُبنى تلقائياً من الفرع `main` — أي `git push` ينشر خلال ~2 دقيقة.

## الأدلة (اقرأها قبل أي تغيير نصي)
- `docs/arabic_copy_guide.md` — قواعد النص العربي القوي (لا إنجليزية داخل الجملة)
- `docs/marketing-mastery.md` — العقلية والاستراتيجية + مهمة الأسبوع
- `docs/sales-playbook.md` — نصوص البيع على واتساب + اعتراضات السعر
- `docs/evidence-log.md` — سجل الأرقام الحقيقية (تغذية قسم النتائج مستقبلاً)
- `docs/service-agreement.md` — اتفاقية الخدمة

## توليد الأصول
```bash
python generate_logo.py          # شعارات PER8 التاريخية (مصفوفة)
python generate_marketing_logo.py
python generate_masterpiece_logo.py
python generate_monogram_icon.py
python generate_og_image.py      # صورة مشاركة 1200x630 (مسارات: PER8/og-image.png)
```

## الملاحظات
- العملة الموحدة: الريال السعودي `ر.س` (السوق المستهدف: السعودية — واتساب +966).
- أيقونات التطبيق: `PER8/logo-mark_*.png` (16-512) مولّدة من `logo-mark.svg`، ويمكن إعادة توليدها بقلم `Pillow` من أي مصدر مربع.
- لا تُنشر أرقام نتائج إلا من `docs/evidence-log.md` — الإثبات بالحقيقة فقط.