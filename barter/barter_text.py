# -*- coding: utf-8 -*-
"""
barter_text.py
==============
barter_text.py generates barcode labels
"""

import argparse
from barter.formats import SUPPORTED_BARCODES, SUPPORTED_IMG_FORMATS
from barter.stuff import write_label_tp, add_sidetext


def main(args):
    text = args.text
    fmt = args.format
    outfile = args.outfile
    width = args.width
    height = args.height
    include_text = args.include_text
    sidetext = args.side_text
    margin = args.side_text_margin

    if not outfile.split(".")[-1] in SUPPORTED_IMG_FORMATS:
        print("{} did not have a valid file extension, saving to {}".format(outfile, outfile+".png"))
        outfile += ".png"

    if not sidetext:
        write_label_tp(data=text, outfile=outfile, barcode_type=fmt, width_mm=width,
                   height_mm=height, include_text=include_text)
    else:
        import tempfile
        f = tempfile.NamedTemporaryFile(delete=True)
        fpng = f.name+".png"
        write_label_tp(data=text, outfile=fpng, barcode_type=fmt, width_mm=width,
                       height_mm=height, include_text=include_text)
        add_sidetext(img_to_add=fpng, outfile=outfile, sidetext=sidetext, margin=margin)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("text", help="text for the barcode")
    parser.add_argument("-f", "--format", help="barcode format", choices=SUPPORTED_BARCODES,
                        default="code128")
    parser.add_argument("outfile", help="output file name")
    parser.add_argument("-H", "--height", help="height in mm", type=int, default=20)
    parser.add_argument("-W", "--width", help="width in mm", type=int, default=40)
    parser.add_argument("-I", "--include_text", help="add human-readable text under barcode",
                        dest='include_text', default=False, action='store_true')
    parser.add_argument("-S", "--side_text", help="text to put next to barcode", default="")
    parser.add_argument("-M", "--side_text_margin", type=int,
                        help="spacing between barcode and text on the side (in px)",
                        default=5)
    main(args=parser.parse_args())
