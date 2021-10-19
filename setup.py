#! /usr/bin/env python3
"""Installations script."""

from setuptools import setup


setup(
    name='html5ds',
    use_scm_version=True,
    setup_requires=['setuptools_scm'],
    python_requires='>=3.8',
    author='HOMEINFO - Digitale Informationssysteme GmbH',
    author_email='<info@homeinfo.de>',
    maintainer='Richard Neumann',
    maintainer_email='<r.neumann@homeinfo.de>',
    packages=['html5ds'],
    entry_points={'console_scripts': ['html5ds = html5ds.main:main']},
    data_files=[('/usr/lib/systemd/system', ['html5ds.service'])],
    description=('Browser wrapper for HTML5 digital sigange applications.')
)
