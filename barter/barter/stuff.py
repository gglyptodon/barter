import os
import treepoem


def mm_to_inch(mm):
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


def csvfun_tp_sidetext(in_csv, column, fmt, outdir, width=20, height=20,
                       include_text=False,
                       side_text_column=0,
                       side_text_margin=1, fontname='', fontsize=16):
    import csv
    import tempfile

    outfile_pref = os.path.join(outdir, "tmp_")
    with open(in_csv) as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='"')
        for i, row in enumerate(reader):
            f = tempfile.NamedTemporaryFile(delete=True)
            fpng = f.name+".png"
            text = row[column]
            sidetext = row[side_text_column]
            margin = side_text_margin
            write_label_tp(data=text,
                           outfile=fpng, # outfile_pref+str(i)+".png",
                           barcode_type=fmt,
                           width_mm=width,
                           height_mm=height,
                           include_text=include_text)
            add_sidetext(img_to_add=fpng,
                         outfile=outfile_pref+str(i)+".png",
                         sidetext=sidetext,
                         margin=margin,
                         fontname=fontname,
                         fontsize=fontsize
                         )


def add_sidetext(sidetext="test0123456789",
                 img_to_add=None,
                 fontsize=20,
                 outfile=None,
                 margin=10,
                 fontname='FreeMono.otf',
                 ):

    from PIL import Image, ImageDraw, ImageFont
    if not outfile:
        raise Exception("Need output file name")

    # get dimensions from old image
    old_img = Image.open(img_to_add)  # barcode
    old_box = old_img.getbbox()
    print(old_box)
    old_width, old_height = old_box[2], old_box[3]

    # get dimensions for text
    #fontname = "dc_o.ttf",
    #font = ImageFont.load_default()
    try:
        font = ImageFont.truetype(fontname, fontsize)
    except Exception: # todo
        print("font {} not found".format(fontname))
        font = ImageFont.load_default()

    font_w, font_h = font.getsize(sidetext)

    # create new image with dim old_image_width + textwidth (+margin) x old_image_height
    W, H = (old_width+font_w+margin, old_height)  # new image size
    bgcol = (255, 255, 255)
    image = Image.new('RGBA', (W, H), bgcol)
    draw = ImageDraw.Draw(image)
    # add text to right
    draw.text((old_width+margin, (H-font_h)/2), sidetext, fill='black', font=font)
    # paste old image
    image.paste(old_img, box=old_box)
    # save image
    image.save(outfile)
    #mimage.paste(simage, box)
    # todo
    # get dimensions from old image
    # get dimensions for text
    # create new image with dim old_image_width + textwidth (+margin) x old_image_height
    # cp old image to left, add text
    # save image


    # draw.text((10, 0), txt, (0,0,0), font=font)
    # img_resized = image.resize((188,45), Image.ANTIALIAS)

    #save_location = os.getcwd()

    # img_resized.save(save_location + '/sample.jpg')

