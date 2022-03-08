import requests
import re
from urllib.parse import unquote


def getFilename(s):
	fname = re.findall("filename\*=([^;]+)", s, flags=re.IGNORECASE)
	if not fname:
		fname = re.findall("filename=([^;]+)", s, flags=re.IGNORECASE)
	if "utf-8''" in fname[0].lower():
		fname = re.sub("utf-8''", '', fname[0], flags=re.IGNORECASE)
		fname = unquote(fname)
	else:
		fname = fname[0]
	# clean space and double quotes
	return fname.strip().strip('"')


def download_data():
	file_ids = [
		'13wUorzpQZ984UACpprU8o21BO6rizaFB',
		'1yFJ3FEKXlJWyUaSL8Z0PkfINw2lYMchE',
		'1fTo5KmOLGbxI3uNHhVOTZbQyTWnOgYD6',
		'11I2vakOkyFTO_EyP19CZz9uMy71JzdIk',
		'1cpcxUg-7_CmAM-5Vpwa72VxUqwuhY8KX',
	]
	
	for id in file_ids:
		url = f'https://drive.google.com/uc?id={id}&authuser=0&export=download'
		r = requests.get(url, stream=True)
		r.raise_for_status()
		name = getFilename(r.headers['content-disposition'])
		with open(name, 'wb') as f:
			for chunk in r.iter_content(chunk_size=1024): 
				if chunk:
					f.write(chunk)
