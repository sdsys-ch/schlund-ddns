"""Update DNS settings using the Schlundtech XML-Gateway.
"""
from setuptools import setup, find_packages
import glob


setup(
    name='ws.ddns',
    version='1.3.0',

    install_requires=[
        'flask',
        'gocept.logging',
        'lxml',
        'requests',
        'setuptools',
    ],

    entry_points={
        'console_scripts': [
            'schlund-ddns = ws.ddns.update:main',
            'schlund-ddns-cgi = ws.ddns.web:main',
        ],
    },

    author='Wolfgang Schnerring <wosc@wosc.de>',
    author_email='wosc@wosc.de',
    license='ZPL 2.1',
    url='https://github.com/wosc/schlund-ddns',

    description=__doc__.strip(),
    long_description='\n\n'.join(open(name).read() for name in (
        'README.rst',
        'CHANGES.txt',
    )),

    classifiers="""\
License :: OSI Approved :: Zope Public License
Programming Language :: Python
Programming Language :: Python :: 3
"""[:-1].split('\n'),

    namespace_packages=['ws'],
    packages=find_packages('src'),
    package_dir={'': 'src'},
    include_package_data=True,
    data_files=[('', glob.glob('*.txt'))],
    zip_safe=False,
)
