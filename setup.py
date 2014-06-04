#!/usr/bin/env python
from setuptools import setup
import glob, os.path

console_scripts = ['i18n_tool = i18n.main:main']

setup(
    name='i18n_tools',
    version='0.1',
    description='edX i18n tools',
    packages=[
        'i18n',
    ],
    install_requires=["polib", "ddt", "path.py", "pyYaml", "pytz"],
    test_suite='nose.collector',
    entry_points={
        'console_scripts': console_scripts
    }
)