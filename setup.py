# mypy: disallow_untyped_defs=False
# -*- coding: utf-8 -*-
import os

from setuptools import find_packages, setup


def get_readme():
    path = os.path.join(os.path.dirname(__file__), "README.rst")
    with open(path) as f:
        return f.read().strip()


def get_version():
    path = os.path.join(os.path.dirname(__file__), "extruct", "VERSION")
    with open(path) as f:
        return f.read().strip()


setup(
    name="extruct",
    version=get_version(),
    description="Extract embedded metadata from HTML markup",
    long_description=get_readme(),
    long_description_content_type="text/x-rst",
    author="Scrapinghub",
    author_email="info@scrapinghub.com",
    maintainer="Scrapinghub",
    maintainer_email="info@scrapinghub.com",
    url="https://github.com/scrapinghub/extruct",
    entry_points={
        "console_scripts": {
            "extruct = extruct.tool:main",
        }
    },
    packages=find_packages(
        exclude=[
            "tests",
        ]
    ),
    package_data={"extruct": ["VERSION"]},
    install_requires=[
        "lxml",
        'rdflib<6.0.0;python_version<"3.7"',
        'rdflib-jsonld<=0.5.0;python_version<"3.7"',
        # rdflib 6.x.y (only on 3.7 and up) contains jsonld
        'rdflib>=6.0.0;python_version>="3.7"',
        "pyrdfa3",
        "mf2py",
        "w3lib",
        "html-text>=0.5.1",
        "six",
        "jstyleson",
    ],
    extras_require={
        "cli": [
            "requests",
        ],
    },
    keywords="extruct",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
)
