import os
import treepoem

def mm_to_inch(mm):
    # print(mm/25.4)
    return mm/25.4/2  # yeah, no idea...


def pixel_to_mm(px):
    return px*(25.4 / 72)


def mm_to_pixel(mm):  # 72 dpi resolution
    return mm*1/(25.4 / 72)


def write_label_tp(barcode_type='qrcode', data='barcode payload', outfile='out.png', width_mm=20, height_mm=20, include_text=False):
    width_mod = mm_to_inch(width_mm)
    height_mod = mm_to_inch(height_mm)
    if include_text:  # idk...
        opts = {'_': '(includetext)', 'width': width_mod, 'height': height_mod}
    else:
        opts = {'width': width_mod, 'height': height_mod}
    image = treepoem.generate_barcode(barcode_type=barcode_type, data=data, options=opts)
    image.convert('1').save(outfile)


def csvfun_tp(in_csv, column, fmt, outdir, width=20, height=20, include_text=False):
    import csv
    outfile_pref = os.path.join(outdir, "tmp_")
    with open(in_csv) as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='"')
        for i, row in enumerate(reader):
            text = row[column]
            write_label_tp(data=text,
                           outfile=outfile_pref+str(i)+".png",
                           barcode_type=fmt,
                           width_mm=width,
                           height_mm=height,
                           include_text=include_text)


def add_sidetext(bc_width):
    from PIL import Image, ImageDraw, ImageFont
    img = Image.new('RGB', (200, 100))
    d = ImageDraw.Draw(img)
    txt = 'hi'
    W, H = (200, 200) # image size
    background = (0, 164, 201)
    fontsize = 65
    font = ImageFont.truetype("dc_o.ttf", fontsize)
    image = Image.new('RGBA', (W, H), background)
    draw = ImageDraw.Draw(image)

    # w, h = draw.textsize(txt) # not that accurate in getting font size
    w, h = font.getsize(txt)

    draw.text((mm_to_pixel(bc_width), (H-h)/2), txt, fill='white', font=font)
    # draw.text((10, 0), txt, (0,0,0), font=font)
    # img_resized = image.resize((188,45), Image.ANTIALIAS)

    save_location = os.getcwd()

    # img_resized.save(save_location + '/sample.jpg')
    image.save(save_location + '/sample.png')