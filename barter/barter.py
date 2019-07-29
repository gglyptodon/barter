# -*- coding: utf-8 -*-
"""
barter.py
=========
barter.py generates barcode labels from csv files
"""

import sys
import os
import tempfile
import argparse
import barcode  # MIT License
import cairosvg  # LGPLv3
from PIL import Image, ImageDraw, ImageFont  # https://github.com/python-pillow/Pillow/blob/master/LICENSE
from barter.formats import SUPPORTED_BARCODES
from barter.stuff import svgtopng, pngstuff, csvfun


def main(args):
    csvinfile = args.infile
    column = args.column
    fmt = args.format
    outdir= args.outdir
    if not os.path.isdir(outdir):
        sys.exit(1)
    csvfun(in_csv=csvinfile, column=column, fmt=fmt,outdir=outdir)



if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--format", help="barcode format", choices=SUPPORTED_BARCODES,
                        default="code128")
    parser.add_argument("infile", help="input csv file")
    parser.add_argument("-c", "--column", help="column for which labels should be generated",
                        type=int, default=0)
    parser.add_argument("outdir", help="output directory name")
    args = parser.parse_args()
    main(args)
