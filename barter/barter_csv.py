# -*- coding: utf-8 -*-
"""
barter_csv.py
=========
barter_csv.py generates barcode labels from csv files
"""

import sys
import os
import argparse
from barter.formats import SUPPORTED_BARCODES
from barter.stuff import csvfun_tp, csvfun_tp_sidetext


def main(args):
    csvinfile = args.infile
    column = args.column
    fmt = args.format
    outdir= args.outdir
    include_text = args.include_text
    width = args.width
    height = args.height
    side_text_column = args.side_text_column
    side_text_margin = args.side_text_margin

    if not os.path.isdir(outdir):
        sys.exit(1)
    if side_text_column is None:
        csvfun_tp(in_csv=csvinfile,
                column=column,
                fmt=fmt,
                outdir=outdir,
                include_text=include_text,
                height=height,
                width=width)
    else:
        csvfun_tp_sidetext(
            in_csv=csvinfile,
                column=column,
                fmt=fmt,
                outdir=outdir,
                include_text=include_text,
                height=height,
                width=width,
                side_text_column = side_text_column,
                side_text_margin = side_text_margin)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--format", help="barcode format", choices=SUPPORTED_BARCODES,
                        default="code128")
    parser.add_argument("infile", help="input csv file")
    parser.add_argument("-c", "--column", help="column for which labels should be generated",
                        type=int, default=0)
    parser.add_argument("outdir", help="output directory name")
    parser.add_argument("-H", "--height", help="height in mm", type=int, default=20)
    parser.add_argument("-W", "--width", help="width in mm", type=int, default=40)
    parser.add_argument("-I", "--include_text", help="add human-readable text", dest='include_text', default=False, action='store_true')

    parser.add_argument("-S", "--side_text_column", help="column for additional text", type=int, default=None)
    parser.add_argument("-M", "--side_text_margin", type=int,
                        help="spacing between barcode and text on the side (in px)",
                        default=5)
    args = parser.parse_args()
    main(args)
