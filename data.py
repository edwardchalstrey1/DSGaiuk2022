import rfc6266
import requests

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
		resp = requests.get(url, stream=True)
		resp.raise_for_status()
		name = rfc6266.parse_requests_response(resp).filename_unsafe
		with open(name, 'wb') as f:
			for chunk in resp.iter_content(chunk_size=1024): 
				if chunk:
	            	f.write(chunk)