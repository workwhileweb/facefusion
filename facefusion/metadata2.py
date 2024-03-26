METADATA =\
{
	'name': 'f*ck stripe',
	'description': 'f*ck stripe',
	'version': '0.0.1',
	'license': 'MIT',
	'author': 'Henry Ruhs',
	'url': 'https://casher.onrender.com/'
}


def get(key : str) -> str:
	return METADATA[key]
