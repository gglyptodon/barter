# -*- coding: utf-8 -*-
"""
barter_text.py
=========
barter_text.py generates barcode labels
"""

import argparse
from barter.formats import SUPPORTED_BARCODES
from barter.stuff import write_label


def main(args):
    text = args.text
    fmt = args.format
    outfile = args.outfile

    write_label(text=text, fmt=fmt, outfile=outfile)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("text", help="use this text instead of input csv file")
    parser.add_argument("-f", "--format", help="barcode format", choices=SUPPORTED_BARCODES,
                        default="code128")
    parser.add_argument("outfile", help="output file name")
    main(args=parser.parse_args())
