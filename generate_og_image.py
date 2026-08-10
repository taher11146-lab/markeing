from PIL import Image, ImageDraw, ImageFont

W, H = 1200, 630
NAVY = (11, 19, 43)
DEEP = (14, 26, 60)
GOLD = (212, 175, 55)
GOLD_LIGHT = (250, 228, 158)
GOLD_DARK = (140, 111, 35)
BLUE = (30, 58, 138)

img = Image.new("RGB", (W, H), NAVY)
d = ImageDraw.Draw(img)

for y in range(H):
    t = y / H
    row = tuple(int(NAVY[i] * (1 - t) + DEEP[i] * t) for i in range(3))
    d.line([(0, y), (W, y)], fill=row)

f_marks = [
    (0.035, 0.048, r"C:\Windows\Fonts\seguisb.ttf", 150),
    (0.085, 0.132, r"C:\Windows\Fonts\seguisb.ttf", 96),
    (0.232, 0.070, r"C:\Windows\Fonts\seguisb.ttf", 84),
    (0.232, 0.146, r"C:\Windows\Fonts\seguisb.ttf", 102),
]
try:
    mark = Image.open(r"C:\Users\Amira\OneDrive\Desktop\markeing\PER8\logo-mark_512.png")
except Exception:
    mark = None

if mark:
    mw = 260
    mh = int(mw * mark.height / mark.width)
    mark = mark.resize((mw, mh), Image.LANCZOS)
    img.paste(mark, (W - mw - 60, 50), mark)

f_font = ImageFont.truetype(r"C:\Windows\Fonts\seguisb.ttf", 96)

def gold_text(d, xy, txt, font, anchor="la"):
    d.text(xy, txt, font=font, fill=GOLD, anchor=anchor)

d.text((820, 140), "PER8", font=f_font, fill=(255, 255, 255))
gold_text(d, (820, 270), "هندسة التسويق", ImageFont.truetype(r"C:\Windows\Fonts\seguisb.ttf", 56))

f = ImageFont.truetype(r"C:\Windows\Fonts\seguisb.ttf", 44)
d.text((820, 380), "متجرك يبيع وأنت نائم", font=f, fill=GOLD_LIGHT)

f2 = ImageFont.truetype(r"C:\Windows\Fonts\seguisb.ttf", 30)
d.text((820, 470), "فحص مجاني للأبعاد الثمانية خلال 48 ساعة", font=f2, fill=(185, 196, 222))

img.save(r"C:\Users\Amira\OneDrive\Desktop\markeing\PER8\og-image.png", optimize=True)
print("og-image.png saved:", img.size)