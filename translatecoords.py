import argparse
parser = argparse.ArgumentParser()
parser.add_argument("latitude", help="Latitude values in D,M,S")
parser.add_argument("longitude", help="Longitude values in D,M,S")
args = parser.parse_args()

if args.latitude and args.longitude:
    latitude = args.latitude.split(',')
    longitude = args.longitude.split(',')

    dlatitude = int(latitude[0]) + (int(latitude[1])/60.0) + (
        int(latitude[2]) / 3600.0)

    dlongitude = int(longitude[0]) + (int(longitude[1])/60.0) + (
        int(longitude[2]) / 3600.0)

    print('Latitude: {}, Longitude {}'.format(dlatitude, dlongitude))

else:
    print(parser.usage)
