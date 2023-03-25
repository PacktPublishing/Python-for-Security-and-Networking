from PIL import Image
from PIL.ExifTags import TAGS

def get_exif_tags():
	ret = {}
	i = Image.open('images/image.jpg')
	info = i._getexif()
	for tag, value in info.items():
		decoded = TAGS.get(tag, tag)
		ret[decoded] = value
	return ret

print(get_exif_tags())
