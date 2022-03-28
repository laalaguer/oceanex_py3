"""
oceanex_py3
-------------

oceanex_py3 is a Python SDK to query, trade and manage funds on Oceanex.

Installation: pip3 install oceanex_py3

Source: 

https://github.com/laalaguer/oceanex_py3

Documentation

https://laalaguer.github.io/oceanex_py3/

"""
from setuptools import setup
from os import path
this_directory = path.abspath(path.dirname(__file__))
long_description = ''
with open(path.join(this_directory, 'README.rst')) as f:
    long_description = f.read()
assert long_description


setup(
    name='oceanex_py3',
    version='1.2.0',
    url='https://github.com/laalaguer/oceanex_py3',
    license='MIT',
    author='laalaguer',
    author_email='laalaguer@gmail.com',
    description='Query, trade and manage funds on Oceanex.',
    long_description=long_description,
    packages=['oceanex_py3'],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=[x.strip() for x in open("requirements.txt")],
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
