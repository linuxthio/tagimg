# -*- coding: utf-8 -*-
from PIL import Image, ImageDraw, ImageFont
import os
from pathlib import Path
import datetime

def getname_without_ext(filename):
    s = filename.split('.')
    s2 = s[:len(s) - 1]
    ext = ''.join(s[len(s) - 1:len(s)])
    r = '.'.join(s2)
    return [r, ext]

def get_date_hour():
    x = datetime.datetime.now().__str__().split()
    _date=x[0]
    _hour=x[1].split('.')[0]
    return [_date,_hour]

def tagimg(filename, prenom='thiongane', nom=get_date_hour()[0], ratio=1):
    """

    :param filename: the filename of image : str
    :param prenom: the surname you want to display :str
    :param nom: the name you want to display  str
    :param ratio: the ratio (float) ex: 2 or 2.0 to divide the size per 2
    :return: void
    """
    prenom=prenom.title()
    nom=nom.title()
    base = Image.open(filename).convert("RGBA")
    txt = Image.new("RGBA", base.size, (255, 255, 255, 0))
    
    if float(ratio)<1:
        ecart=60
    else:
        ecart = 20 * int(ratio)
    fnt = ImageFont.truetype("Pillow/Tests/fonts/FreeMono.ttf", ecart)
    d = ImageDraw.Draw(txt)

    xs = base.size[0] / 2
    ys = base.size[1] / 2
    
    a=40 #alpha
    d.text((xs, ys - 5*ecart), prenom, font=fnt, fill=(255, 255, 255, 255))
    d.text((xs, ys-4*ecart), nom, font=fnt, fill=(255, 255, 255, 255))

    d.text((xs, ys - 3*ecart), prenom, font=fnt, fill=(0, 0, 0, 255))
    d.text((xs, ys-2*ecart), nom, font=fnt, fill=(0, 0, 0, 255))

    d.text((xs, ys - ecart), prenom, font=fnt, fill=(0, 255, 0, a))
    d.text((xs, ys), nom, font=fnt, fill=(0, 255, 0, a))

    d.text((xs, ys + ecart), prenom, font=fnt, fill=(255, 255, 0, a))
    d.text((xs, ys + 2 * ecart), nom, font=fnt, fill=(255, 255, 0, a))

    d.text((xs, ys + 3 * ecart), prenom, font=fnt, fill=(255, 0, 0, a))
    d.text((xs, ys + 4 * ecart), nom, font=fnt, fill=(255, 0, 0, a))

    out = Image.alpha_composite(base, txt)

    x = base.size[0]
    y = base.size[1]

    fratio=float(ratio)
    size = x / fratio, y / fratio
    out.thumbnail(size, Image.ANTIALIAS)
    namefile=getname_without_ext(filename)[0]
    outer_file = namefile + "_out_."+"png"
    DOSSIER_DEST='tagimg_out'
    home = str(Path.home())
    path_dest="{}/{}".format(home,DOSSIER_DEST)
    try:
        os.mkdir(path_dest)
    except:
        pass
    
    out.save(path_dest+'/'+outer_file)
    print(path_dest)
    print(outer_file, base.size[0])



"""w=getname_without_ext('fic-_121221kil.jeu.jpeg')
print(w)
"""

def main():
    import sys
    nb=sys.argv
    print(len(nb))
    if len(nb)==1:
        print('you are forget the image filename')
    elif len(nb)==2:
        tagimg(nb[1])
    elif len(nb)==3:
        tagimg(nb[1],nb[2])
    elif len(nb)==4:
        tagimg(nb[1],nb[2],nb[3])
    elif len(nb)==5:
        tagimg(nb[1],nb[2],nb[3],nb[4])
    else:
        print("Error:: missing parametre")
    
if __name__=='__main__':
    main()

