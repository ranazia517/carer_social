#!/usr/bin/env python3
# Regenerates assets/og-card.png (1200x630) for wellnetixltd.com.
# Needs Poppins (Bold/Medium). See DEPLOYMENT_RUNBOOK.md section 6 (font gotcha:
# the nimind Inter TTFs are Git-LFS HTML pointers -> use Poppins instead).
import os
import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter

S = 2
W, H = 1200 * S, 630 * S
BG = (11, 11, 20)
INDIGO = (109, 95, 246)
VIOLET = (155, 107, 242)
PINK = (232, 121, 199)
HEAD = (244, 242, 251)
BODY = (188, 183, 206)
MUTED = (140, 135, 162)

_FONT_DIRS = [
    "/usr/share/fonts/truetype/google-fonts/",          # Cowork sandbox
    "/usr/share/fonts/truetype/poppins/",
    os.path.expanduser("~/Library/Fonts/"),             # macOS user fonts
    "/Library/Fonts/", "/System/Library/Fonts/Supplemental/",
]
def _font_path(name):
    for d in _FONT_DIRS:
        p = os.path.join(d, name)
        if os.path.exists(p):
            return p
    return name  # let PIL try its default search
def F(name, size):
    return ImageFont.truetype(_font_path(name), int(size * S))

# ---------- ambient glow background ----------
base = np.zeros((H, W, 3), np.float32); base[:] = BG
yy, xx = np.mgrid[0:H, 0:W]
def glow(cx, cy, rad, color, strength):
    d = np.sqrt(((xx - cx) / rad) ** 2 + ((yy - cy) / rad) ** 2)
    a = np.clip(1 - d, 0, 1) ** 2 * strength
    for i in range(3):
        base[:, :, i] += color[i] * a
glow(W * 0.10, H * 0.12, W * 0.60, INDIGO, 0.55)
glow(W * 0.97, H * 0.96, W * 0.55, PINK, 0.42)
glow(W * 0.75, H * 0.12, W * 0.42, VIOLET, 0.30)
glow(W * 0.30, H * 1.04, W * 0.45, INDIGO, 0.20)
base = np.clip(base, 0, 255).astype(np.uint8)
img = Image.fromarray(base, "RGB")
draw = ImageDraw.Draw(img)
draw.rectangle([0, 0, W, 6 * S], fill=(26, 23, 44))

# ---------- helpers ----------
def hgrad(w, h, stops):
    xs = np.linspace(0, 1, max(1, w)); pos = [s[0] for s in stops]
    r = np.interp(xs, pos, [s[1][0] for s in stops])
    g = np.interp(xs, pos, [s[1][1] for s in stops])
    b = np.interp(xs, pos, [s[1][2] for s in stops])
    arr = np.zeros((h, w, 3), np.uint8)
    arr[:, :, 0] = r[None, :]; arr[:, :, 1] = g[None, :]; arr[:, :, 2] = b[None, :]
    return Image.fromarray(arr, "RGB")

def grad_text(xy, text, font, stops=((0, INDIGO), (0.5, VIOLET), (1, PINK))):
    bbox = draw.textbbox((0, 0), text, font=font)
    tw, th = bbox[2] - bbox[0], bbox[3] - bbox[1]
    mask = Image.new("L", (tw + 8, th + 8), 0)
    ImageDraw.Draw(mask).text((-bbox[0] + 4, -bbox[1] + 4), text, font=font, fill=255)
    img.paste(hgrad(tw + 8, th + 8, stops), (int(xy[0]), int(xy[1])), mask)

def solid_text(xy, text, font, color):
    draw.text(xy, text, font=font, fill=color)

PAD = 84 * S

# ---------- logo mark ----------
mk = 66 * S
mark = Image.new("RGBA", (mk, mk), (0, 0, 0, 0))
mgrad = hgrad(mk, mk, ((0, INDIGO), (0.5, VIOLET), (1, PINK))).convert("RGBA")
mmask = Image.new("L", (mk, mk), 0)
ImageDraw.Draw(mmask).rounded_rectangle([0, 0, mk - 1, mk - 1], radius=int(20 * S), fill=255)
mark.paste(mgrad, (0, 0), mmask)
dot = Image.new("L", (mk, mk), 0)
ImageDraw.Draw(dot).ellipse([mk * 0.24, mk * 0.20, mk * 0.60, mk * 0.56], fill=170)
dot = dot.filter(ImageFilter.GaussianBlur(4 * S))
mark.paste(Image.new("RGB", (mk, mk), (255, 255, 255)), (0, 0), dot)
img.paste(mark, (PAD, 72 * S), mark)
solid_text((PAD + mk + 22 * S, 72 * S + 12 * S), "Wellnetix", F("Poppins-Bold.ttf", 37), HEAD)

# ---------- headline ----------
hf = F("Poppins-Bold.ttf", 60)
y = 210 * S
grad_text((PAD, y), "Advancing Human", hf)
y += int(60 * S * 1.18)
solid_text((PAD, y), "Wellbeing", hf, HEAD)
y += int(60 * S * 1.18) + 12 * S
solid_text((PAD, y), "Through Intelligent Technologies", F("Poppins-Medium.ttf", 31), HEAD)

# ---------- sub line ----------
y += int(31 * S * 1.2) + 28 * S
solid_text((PAD, y), "Ethical, privacy-first AI for mental wellbeing.", F("Poppins-Medium.ttf", 24), BODY)

# ---------- bottom row ----------
py = H - 94 * S
pf = F("Poppins-Medium.ttf", 22)
def pill(x, label):
    tb = draw.textbbox((0, 0), label, font=pf); tw, th = tb[2] - tb[0], tb[3] - tb[1]
    w = tw + 46 * S; h = 52 * S
    border = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    bmask = Image.new("L", (w, h), 0)
    ImageDraw.Draw(bmask).rounded_rectangle([0, 0, w - 1, h - 1], radius=h // 2, fill=255)
    border.paste(hgrad(w, h, ((0, INDIGO), (1, PINK))).convert("RGBA"), (0, 0), bmask)
    inner = Image.new("L", (w, h), 0)
    ImageDraw.Draw(inner).rounded_rectangle([2 * S, 2 * S, w - 1 - 2 * S, h - 1 - 2 * S], radius=h // 2, fill=255)
    border.paste(Image.new("RGB", (w, h), BG), (0, 0), inner)
    img.paste(border, (x, py), border)
    draw.text((x + 23 * S, py + (h - th) // 2 - tb[1]), label, font=pf, fill=HEAD)
    return x + w + 16 * S
nx = pill(PAD, "NiMind"); pill(nx, "CARER")

uf = F("Poppins-Medium.ttf", 23)
ub = draw.textbbox((0, 0), "wellnetixltd.com", font=uf); uw = ub[2] - ub[0]
draw.text((W - PAD - uw, py + 13 * S), "wellnetixltd.com", font=uf, fill=MUTED)

out = img.resize((1200, 630), Image.LANCZOS)
p = "/sessions/tender-confident-mccarthy/mnt/outputs/og-card.png"
out.save(p, "PNG")
print("saved", p, out.size)
