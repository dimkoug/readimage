from PIL import Image
from PIL.ExifTags import TAGS
from GPSPhoto import gpsphoto

image_file = 'img.jpg'

img = Image.open(image_file)
info = img._getexif()
for tag, value in info.items():
    key = TAGS.get(tag, tag)
    print(key + " " + str(value))

data = gpsphoto.getGPSData('img.jpg')
print(data['Latitude'], data['Longitude'])
