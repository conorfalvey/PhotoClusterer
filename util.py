from config import GPS_KEYS


def dms_to_dec(coord: list):
    if len(coord) != 3:
        raise TypeError(
            f"Expected list with GPS Degree/Minute/Second for Latitude or Longitude"
        )

    dec_coord = coord[0] + coord[1] / 60 + coord[2] / 3600

    return dec_coord


def pull_gps(exif: dict):
    return {k.split(" ")[1]: v.values for k, v in exif.items() if k in GPS_KEYS}


def bulk_convert_gps(d: dict):
    for k, v in d.items():
        if "GPSLatitude" in v.keys() and "GPSLongitude" in v.keys():
            v["GPSLatitude"] = dms_to_dec(v["GPSLatitude"])
            v["GPSLongitude"] = dms_to_dec(v["GPSLongitude"])
    return d
