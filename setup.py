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


setup(
    name='oceanex_py3',
    version='1.0.1',
    url='https://github.com/laalaguer/oceanex_py3',
    license='MIT',
    author='laalaguer',
    author_email='laalaguer@gmail.com',
    description='Query, trade and manage funds on Oceanex.',
    long_description=__doc__,
    packages=['oceanex_py3'],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=[
        'pytest',
        'requests',
        'pyjwt'
    ],
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
