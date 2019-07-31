import treepoem.data


def get_supported_by_treepoem():
    return sorted(treepoem.data.barcode_types.keys())


SUPPORTED_BARCODES = get_supported_by_treepoem()
SUPPORTED_IMG_FORMATS = ["png"]
