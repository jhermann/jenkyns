# -*- coding: utf-8 -*-
""" jenkyns - (Python) Jenkins Tools.

    jenkyns is a command line tool that helps with the daily management
    of your Jenkins jobs.

    Copyright © 2013 Jürgen Hermann

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""
import os
import re
import sys

from paver.easy import *
from paver.setuputils import setup
from setuptools import find_packages


#
# Project Description
#
changelog = path("debian/changelog").text()
project = dict(
    # project data & layout
    name = changelog.split()[0],
    version = re.search(r"(?<=\()[^)]+(?=\))", changelog).group(),
    package_dir = {"": "src"},
    packages = find_packages("src", exclude=["tests"]),
    test_suite = "nose.collector",
    zip_safe = True,
    include_package_data = True,
    data_files = [
        ("EGG-INFO", [
            "README.md", "LICENSE", "debian/changelog",
        ]),
    ],
    entry_points = {
        "console_scripts": [
            "jenkyns = jenkyns.cli:run",
        ],
    },

    # dependency management
    install_requires = [
    ],
    setup_requires = [
        "docutils",
    ],
    extras_require = {
    },

    # PyPI
    url = "https://github.com/jhermann/jenkyns",
    license = "Apache License Version 2.0",
    keywords = "python tool cli jenkins continuous.integration",
    author = "Jürgen Hermann",
    author_email = "jh@web.de",
    description = __doc__.split('.')[0].strip(),
    long_description = __doc__.split('.', 1)[1].strip(),
    classifiers = [
        # values at http://pypi.python.org/pypi?:action=list_classifiers
        "Development Status :: 3 - Alpha",
        #"Development Status :: 4 - Beta",
        #"Development Status :: 5 - Production/Stable",
        "Operating System :: OS Independent",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 2.7",
        "Topic :: Software Development :: Build Tools",
        "Topic :: Software Development :: Quality Assurance",
        "Topic :: Utilities",
    ],
)


#
# Tasks
#
@task
@needs(["paver.misctasks.generate_setup", "paver.misctasks.minilib", "setuptools.command.develop"])
def init():
    """Initial project setup."""
    # Fix paver-minilib bug
    import zipfile
    pml = zipfile.ZipFile("paver-minilib.zip", 'a')
    try:
        pml.getinfo("paver/version.py")
    except KeyError:
        pml.writestr("paver/version.py", "VERSION='0.0.0'\n")
    pml.close()


#
# Call back to Paver
#
setup(**project)

