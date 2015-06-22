try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    "name": "Projectname"
    "description": "Project Description",
    "author": "Name of author",
    "author_email": "Email of author",
    "url":"Project's URL",
    "download_url":"Project's download_url",
    "version":"0.1",
    "install_requires":["nose"],
    "packages": ["NAME"],
    "scripts": []
}

setup(**config)