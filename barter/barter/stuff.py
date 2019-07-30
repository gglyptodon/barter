import os
import tempfile
import barcode
from .formats import SUFFIX_PNG, SUFFIX_SVG
import svglib


def mm_to_inch(mm):
    print(mm/25.4)
    return mm/25.4/2  # yeah, no idea...


def write_label_tp(barcode_type='qrcode', data='barcode payload', outfile='out.png', width_mm=20, height_mm=20, include_text=False):
    import treepoem
    #image = treepoem.generate_barcode(barcode_type=barcode_type, data=data, options={"width": mm_to_inch(width_mm), "height": mm_to_inch(height_mm)})
    #image.convert('1').save(outfile+"mm"+".pdf")

    width_mod = mm_to_inch(width_mm)
    height_mod = mm_to_inch(height_mm)
    if include_text:  # idk...
        opts = {'_': '(includetext)', 'width': width_mod, 'height': height_mod}
    else:
        opts = {'width': width_mod, 'height': height_mod}
    image = treepoem.generate_barcode(barcode_type=barcode_type, data=data, options=opts)
    image.convert('1').save(outfile)


def writelabel2(barcode, code, out, opts, text):
    writersvg = barcode.SVGWriter()
    writerimg = barcode.ImageWriter()
    name = barcode.generate(barcode, code, writersvg, out, opts, text)
    print('New barcode saved as {0}.'.format(name))
    name = barcode.generate(barcode, code, writerimg, out, opts, text)
    print('New barcode saved as {0}.'.format(name))


def write_label(text, fmt, outfile, width=200, height=100):
    barcode_class = barcode.get_barcode_class(fmt)
    gen_barcode = barcode_class(text)

    with tempfile.TemporaryDirectory() as tmpdirname:
        tmpout = os.path.join(tmpdirname, "tmp.out")
        gen_barcode.save(tmpout)
        svgtopng2(tmpout+SUFFIX_SVG, out=tmpout+SUFFIX_PNG)
        # todo: png/pdf with bcode next to human readable output for labels of size n*m )
        # todo: size

        pngstuff(bcd=tmpout+SUFFIX_PNG, message=text, out=outfile)


def svgtopng2(insvg, out="out.png", width=10, height=20):
    from svglib.svglib import svg2rlg
    from reportlab.graphics import renderPDF, renderPM
    drawing = svg2rlg(insvg)
    renderPM.drawToFile(drawing, out, fmt="PNG")


#todo height width not working
def svgtopng(insvg, out="out.png", width=10, height=20):
    from cairosvg.surface import PNGSurface
    with open(insvg, 'rb') as svg_file:
        PNGSurface.convert(
            bytestring=svg_file.read(),
            width=width,
            height=height,
            write_to=open(out, 'wb')
        )


def pngstuff(bcd="out.png", message="Happy Birthday!",name = 'bla', out='res.png'):
    from PIL import Image, ImageDraw, ImageFont
    #image = Image.open('background.png')
    image = Image.new('RGB', (200, 100),color=(255,255,255))
    bcdim=Image.open(bcd)
    image.paste(bcdim, (0,0))

    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype('Roboto-Bold.ttf', size=14)
    (x, y) = (120, 20)
    color = 'rgb(0, 0, 0)' #
    # draw the message on the background
    draw.text((x, y), message, fill=color, font=font)
    (x, y) = (150, 150)
    color = 'rgb(255, 255, 255)' # white color
    draw.text((x, y), name, fill=color, font=font)


    # save the edited image

    image.save(out)


def csvfun(in_csv, column, fmt, outdir):
    import csv
    outfile_pref = os.path.join(outdir,"tmp_")
    with open(in_csv) as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='"')
        for i, row in enumerate(reader):
            #print(', '.join(row))
            #print(row[column])
            text = row[column]
            write_label(text=text, fmt=fmt, outfile=outfile_pref+str(i)+".png")
