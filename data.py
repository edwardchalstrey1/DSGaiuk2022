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
		'16jnmnbKS1qStGmEashuUJOyg8GlLA1YV',
		'15wd2Tly-4Otxgp0idQ_UPpCkIwx5pw4Z',
		'1q2j3Xvm11MezBSHEEJHbK0fscuGamK3L',
		'1DUebY1kB1k0yq3kNTNd4Lx39z07YPtXc',
		'1APE37mx9V6Iyl454qKrIJ0DIALwvMJd7',
		'1IexMWC5wgqRbVKJ2Io2Xe08UUalahiBk',
		'1Qfe7uQ3zut8bjiCEW3I_QGft-SI5jCHk'
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
