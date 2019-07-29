import os
import tempfile
import barcode
from .formats import SUFFIX_PNG, SUFFIX_SVG

def write_label(text, fmt, outfile):
    barcode_class = barcode.get_barcode_class(fmt)
    gen_barcode = barcode_class(text)

    with tempfile.TemporaryDirectory() as tmpdirname:
        tmpout = os.path.join(tmpdirname, "tmp.out")
        print('created temporary directory', tmpdirname, tmpout)
        gen_barcode.save(tmpout)
        svgtopng(tmpout+SUFFIX_SVG, out=tmpout+SUFFIX_PNG)
        # todo: png/pdf with bcode next to human readable output for labels of size n*m )
        # todo: read in csv for multi outputs
        # todo: size

        pngstuff(bcd=tmpout+SUFFIX_PNG, message=text, out=outfile)
    pass


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



def helpfn():
    print("text format output")

