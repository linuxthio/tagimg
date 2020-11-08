from PIL import Image, ImageDraw, ImageFont


def getname_without_ext(filename):
    s = filename.split('.')
    s2 = s[:len(s) - 1]
    ext = ''.join(s[len(s) - 1:len(s)])
    r = '.'.join(s2)
    return [r, ext]


def tagimg(filename, prenom, nom, ratio):
    """

    :param filename: the filename of image : str
    :param prenom: the surname you want to display :str
    :param nom: the name you want to display  str
    :param ratio: the ratio (float) ex: 2 or 2.0 to divide the size per 2
    :return: void
    """
    base = Image.open(filename).convert("RGBA")
    txt = Image.new("RGBA", base.size, (255, 255, 255, 0))
    ecart = 40 * int(ratio)
    fnt = ImageFont.truetype("Pillow/Tests/fonts/FreeMono.ttf", ecart)
    d = ImageDraw.Draw(txt)

    xs = base.size[0] / 2
    ys = base.size[1] / 2

    d.text((xs, ys - ecart), prenom, font=fnt, fill=(0, 255, 0, 128))
    d.text((xs, ys), nom, font=fnt, fill=(0, 255, 0, 123))

    d.text((xs, ys + ecart), prenom, font=fnt, fill=(255, 255, 0, 128))
    d.text((xs, ys + 2 * ecart), nom, font=fnt, fill=(255, 255, 0, 123))

    d.text((xs, ys + 3 * ecart), prenom, font=fnt, fill=(255, 0, 0, 128))
    d.text((xs, ys + 4 * ecart), nom, font=fnt, fill=(255, 0, 0, 123))

    out = Image.alpha_composite(base, txt)

    x = base.size[0]
    y = base.size[1]


    size = x / ratio, y / ratio
    out.thumbnail(size, Image.ANTIALIAS)
    namefile=getname_without_ext(filename)[0]
    outer_file = namefile + "_out_."+"png"
    out.save(outer_file)
    print(outer_file, base.size[0])



"""w=getname_without_ext('fic-_121221kil.jeu.jpeg')
print(w)
"""



