import os
from config import VALID_EXTENSIONS
from util import pull_gps, bulk_convert_gps
import exifread
from pprint import pprint

TEST_PATH = "C:\\Users\\Conor\\Desktop\\Balkans Trip\\Raw\\Albania"


def scrape_dir(path):
    gps_data = {}
    if not os.path.isdir(path):
        raise IsADirectoryError(f"{path} is not a valid directory.")

    files = [
        os.path.join(path, f)
        for f in os.listdir(path)
        if os.path.isfile(os.path.join(path, f))
    ]
    if not files:
        raise FileNotFoundError(f"No files in {path}")

    for file in files:
        gps_data.update(scrape_file(file))

    return gps_data


def scrape_file(path):
    with open(path, "rb") as f:
        exif = exifread.process_file(f)
        gps = pull_gps(exif)
        # print(gps)
        return {path: gps}


d = scrape_dir(TEST_PATH)
d = bulk_convert_gps(d)
pprint(d.values())
