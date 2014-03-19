"""
Flask-BIBFRAME
--------------

This Flask extension provides  for `BIBFRAME <http://bibframe.org>`_ Linked
Data support in Flask applications.
"""
__author__ = "Jeremy Nelson"
__version_info__ = ('0', '0', '3')
__version__ = '.'.join(__version_info__)

from setuptools import find_packages, setup

setup(
    name='Flask-BIBFRAME',
    version=__version__,
    url='http://github.com/jermnelson/flask_bibframe',
    license='MIT License',
    author=__author__,
    author_email='jermnelson@gmail.com',
    description='Library for BIBFRAME Linked Data support in Flask apps',
    long_description=__doc__,
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=[
        'python-dateutil',
        'Flask',
        'poster',
        'rdflib'
    ],
    classifiers=[
        'Framework :: Flask',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'

    ]
)
