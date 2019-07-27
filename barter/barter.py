import sys
import barcode

version = "0.0.1"


def main(args):
    print("barter {}".format(version))
    print("available:{}".format(" \n".join(barcode.PROVIDED_BARCODES)))
    print(" ".join(args))
    text = args[1]
    fmt = args[2]
    outfile = args[3]
    if not text:
        text = "test"
    if not fmt:
        fmt = "code128"
    if not outfile:
        outfile = "out.svg"
    cls = barcode.get_barcode_class(fmt)
    bcode = cls(text)
    print(bcode)
    bcode.save(outfile)
    svgtopng(outfile+".svg")
    # todo: png/pdf with bcode next to human readable output for labels of size n*m )
    # todo: read in csv for multi outputs
    pngstuff(message=text)


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

def pngstuff(bcd="out.png", message="Happy Birthday!",name = 'bla' ):
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

    image.save('res.png')



def helpfn():
    print("text format output")



if __name__ == "__main__":
    main(sys.argv)
