from PIL import Image, ImageDraw, ImageFont
# def tatouage(filename,outer_file="outer_file",prenom='prenom',nom='nom',x=10,y=10,ratio=1):

def getname_without_ext(filename):
    s = filename.split('.')
    s2 = s[:len(s) - 1]
    ext = ''.join(s[len(s) - 1:len(s)])
    r = '.'.join(s2)
    return [r, ext]


def tagimg(filename, prenom, nom, ratio):
    """

    :param filename: tagimg.py str
    :param prenom: djibril str
    :param nom: thiongane str
    :param ratio: float
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

def main():
    import sys
    nb=sys.argv
    tagimg(nb[1],nb[2],nb[3],nb[4])
    
if __name__=='__main__':
    main()

