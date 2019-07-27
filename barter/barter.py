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


def helpfn():
    print("text format output")



if __name__ == "__main__":
    main(sys.argv)
