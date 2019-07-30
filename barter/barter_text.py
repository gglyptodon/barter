# -*- coding: utf-8 -*-
"""
barter_text.py
==============
barter_text.py generates barcode labels
"""

import argparse
from barter.formats import SUPPORTED_BARCODES
from barter.stuff import write_label_tp


def main(args):
    text = args.text
    fmt = args.format
    outfile = args.outfile
    width = args.width
    height = args.height
    include_text = args.include_text

    write_label_tp(data=text, outfile=outfile, barcode_type=fmt, width_mm=width,
                   height_mm=height, include_text=include_text)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("text", help="text for the barcode")
    parser.add_argument("-f", "--format", help="barcode format", choices=SUPPORTED_BARCODES,
                        default="code128")
    parser.add_argument("outfile", help="output file name")
    parser.add_argument("-H", "--height", help="height in mm", type=int, default=20)
    parser.add_argument("-W", "--width", help="width in mm", type=int, default=40)
    parser.add_argument("-I", "--include_text", help="add human-readable text", dest='include_text', default=False, action='store_true')
    main(args=parser.parse_args())