#!/usr/bin/env python
import json
from os.path import exists

from setuptools import find_packages, setup
from setuptools.dist import Distribution

from ftoolz import __version__ as ftoolz_version


class BinaryDistribution(Distribution):
    """Distribution which always forces a binary package with platform name"""

    def has_ext_modules(self) -> bool:
        return True


with open('Pipfile.lock') as pipfile_lock:
    lock_data = json.load(pipfile_lock)

requirements = [
    package_name
    for package_name in lock_data['default'].keys()
]

test_requirements = [
    package_name
    for package_name in lock_data['develop'].keys()
]

setup(
    name='ftoolz',
    version=ftoolz_version,
    license='MIT',
    description='Collection of higher-order and utility functions',
    long_description=(open('README.md').read() if exists('README.md') else ''),
    long_description_content_type='text/markdown',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Operating System :: Unix',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    url='https://github.com/blindspot-ai/ftoolz',
    maintainer='Martin Matyasek',
    maintainer_email='martin.matyasek@blindspot.ai',
    keywords='functional utility cytoolz itertools functools',
    packages=find_packages(exclude=['tests']),
    include_package_data=True,
    distclass=BinaryDistribution,
    zip_safe=False,
    python_requires='>=3.6',
    install_requires=requirements,
    test_suite='tests',
    tests_require=test_requirements,
)
