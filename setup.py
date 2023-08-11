import re

from setuptools import find_packages, setup

# get metadata from module using a regexp
with open('sensor_awi/__init__.py') as f:
    metadata = dict(re.findall(r'__(.*)__ = [\']([^\']*)[\']', f.read()))

setup(
    name=metadata['title'],
    version=metadata['version'],
    author=metadata['author'],
    author_email=metadata['email'],
    maintainer=metadata['author'],
    maintainer_email=metadata['email'],
    license=metadata['license'],
    url='https://github.com/hafu/rdmo-sensor-awi',
    description=u'The dynamic sensor AWI optionset will query the sensor.awi.de API for sensors.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    classifiers=[
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.8'
    ],
    packages=find_packages(),
    include_package_data=True
)
