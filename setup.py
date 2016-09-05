#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name='hstspreload',
    version='2016.9.5',
    url='https://github.com/kislyuk/hstspreload',
    license='Apache Software License',
    author='Andrey Kislyuk',
    author_email='kislyuk@gmail.com',
    description='HSTS and HPKP Preload List support for Python HTTP clients',
    long_description=open('README.rst').read(),
    install_requires=[
    ],
    extras_require={
        ':python_version == "2.7"': ['enum34 >= 1.0.4'],
        ':python_version == "3.3"': ['enum34 >= 1.0.4']
    },
    packages=find_packages(exclude=['test']),
    platforms=['MacOS X', 'Posix'],
    package_data={'pyhttpsec': ['*.gz']},
    include_package_data=True,
    test_suite='test',
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: POSIX',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
