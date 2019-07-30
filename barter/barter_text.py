# -*- coding: utf-8 -*-
"""
barter_text.py
=========
barter_text.py generates barcode labels
"""

import argparse
from barter.formats import SUPPORTED_BARCODES, get_supported_by_treepoem
from barter.stuff import write_label, write_label_tp


def main(args):
    text = args.text
    fmt = args.format
    outfile = args.outfile
    width = args.width
    height = args.height


    #write_label(text=text, fmt=fmt, outfile=outfile, width=200, height=100)
    write_label_tp(data=text, outfile=outfile, barcode_type=fmt, width_mm=width, height_mm=height)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("text", help="text for the barcode")
    parser.add_argument("-f", "--format", help="barcode format", choices=SUPPORTED_BARCODES,
                        default="azteccodecompact")
    parser.add_argument("outfile", help="output file name")
    parser.add_argument("-H", "--height", help="height in mm", type=int, default=20)
    parser.add_argument("-W", "--width", help="width in mm", type=int, default=20)
    main(args=parser.parse_args())
