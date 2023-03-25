from PIL.ExifTags import TAGS, GPSTAGS
from PIL import Image
import os

def get_exif_metadata(image_path):
    exifData = {}
    image = Image.open(image_path)
    if hasattr(image, '_getexif'):
        exifinfo = image._getexif()
        if exifinfo is not None:
            for tag, value in exifinfo.items():
                decoded = TAGS.get(tag, tag)
                exifData[decoded] = value
    decode_gps_info(exifData)
    return exifData

def convert_to_degress(value):
    d = float(value[0])
    m = float(value[1])
    s = float(value[2])
    return d + (m / 60.0) + (s / 3600.0)
    
def decode_gps_info(exif):
    gpsinfo = {}
    if 'GPSInfo' in exif:
        for key in exif['GPSInfo'].keys():
            decode = GPSTAGS.get(key,key)
            gpsinfo[decode] = exif['GPSInfo'][key]
        exif['GPSInfo'] = gpsinfo

        latitude = exif['GPSInfo']['GPSLatitude']
        latitude_ref = exif['GPSInfo']['GPSLatitudeRef']
        longitude = exif['GPSInfo']['GPSLongitude']
        longitude_ref = exif['GPSInfo']['GPSLongitudeRef']
        if latitude:
            latitude_value = convert_to_degress(latitude)
            if latitude_ref != 'N':
                latitude_value = -latitude_value
        else:
            return {}
        if longitude:
            longitude_value = convert_to_degress(longitude)
            if longitude_ref != 'E':
                longitude_value = -longitude_value
                
        exif['GPSInfo'] = {"Latitude" : latitude_value, "Longitude" : longitude_value}
   
def printMetadata():
    for dirpath, dirnames, files in os.walk("images"):
        for name in files:
            print("[+] Metadata for file: %s " %(dirpath+os.path.sep+name))
            try:
                exifData = {}
                exif = get_exif_metadata(dirpath+os.path.sep+name)
                for metadata in exif:
                    print("Metadata: %s - Value: %s " %(metadata, exif[metadata]))
                print("\n")
            except:
                import sys, traceback
                traceback.print_exc(file=sys.stdout)

if __name__ == "__main__":
    printMetadata()


