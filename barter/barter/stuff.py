import os
import treepoem

def mm_to_inch(mm):
    # print(mm/25.4)
    return mm/25.4/2  # yeah, no idea...


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
