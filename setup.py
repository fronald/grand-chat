try:
    from setuptools import setup
except:
    from distutils.core import setup

config = {
    'description': 'A simple chat application for geeks',
    'author': 'Felipe Costa',
    'url': 'github.com/felipeanchieta/grandchat',
    'download_url': 'github.com/felipeanchieta/grandchat/download',
    'author_email': 'felipeanchieta2@gmail.com',
    'version': '0.1',
    'install_requires': [],
    'scripts': [],
    'name': 'GrandChat'
}

setup(**config)
