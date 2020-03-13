from setuptools import setup

__version__ = "1.0.0"

with open('README.rst') as f:
    long_description = f.read()

setup(
    name = "django-spgateway",
    version = __version__,
    description = 'Django support for Spgateway',
    keywords = "django, spgateway",
    url = "https://github.com/superbil/django-spgateway",
    license = "MIT",
    packages = ["spgateway"],
    include_package_data = True,
    install_requires = ["django>=1.10", "pycrypto>=2.6.1"],
    classifiers = [
        "Development Status :: 4 - Beta",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.7",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Framework :: Django",
        "Framework :: Django :: 2.2",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Environment :: Web Environment",
    ],
    long_description = long_description,
    projects_urls = {
        'Bug Reports': 'https://github.com/Superbil/django-spgateway/issues',
        'Source': 'https://github.com/superbil/django-spgateway',
    }
)
