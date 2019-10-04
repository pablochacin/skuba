#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Copyright (c) 2019 SUSE LLC.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os

from setuptools import find_packages, setup


def version():
    """Return the version. Pass when VERSION file not found"""
    pwd = os.path.dirname(os.path.abspath(__file__))
    try:
        with open(os.path.join(pwd, '..', 'VERSION')) as version_file:
            return version_file.read().strip()
    except FileNotFoundError:
        return ''


setup(
    name="skuba-testrunner",
    version=version(),
    author="SUSE Containers Team",
    author_email="containers@suse.com",
    description="Utility to deploy and test SUSE CaaSP clusters",
    long_description="Wraps skuba and terraform to provision, setup, and tests CaaSP clusters.",
    license="Apache License 2.0",
    keywords="CaaSP",
    url="https://github.com/SUSE/skuba/ci/infra/testrunner",
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache License 2.0',
        'Operating System :: POSIX :: Linux',
    ], 
    packages=find_packages(),
    install_requires=[
        'timeout-decorator',
        'requests',
        'pyhcl',
        'pytest==5.1.0',
        'pyyaml',
        'pytest-ordering'
    ],
    data_files=[
    ],
    entry_points={
        'console_scripts': [
            'skuba-testrunner=testrunner.testrunner:main'
        ]
    }
)
