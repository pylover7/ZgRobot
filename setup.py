#!/usr/bin/env python
# coding=utf-8

import io
import zgrobot

from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand


class PyTest(TestCommand):
    user_options = [("pytest-args=", "a", "Arguments to pass to pytest")]

    def initialize_options(self):
        TestCommand.initialize_options(self)
        self.pytest_args = ""

    def run_tests(self):
        import shlex
        import sys

        # import here, cause outside the eggs aren't loaded
        import pytest

        errno = pytest.main(shlex.split(self.pytest_args))
        sys.exit(errno)


with io.open("README.md", encoding="utf8") as f:
    readme = f.read()

install_requires = open("requirements.txt").readlines()
setup(
    name='zgrobot',
    version=zgrobot.__version__,
    author=zgrobot.__author__,
    author_email='shuoshuoyun@foxmail.com',
    url='https://github.com/pylover7/ZgRobot',
    packages=find_packages(),
    keywords="wechat weixin zgrobot",
    description='ZgRoBot: writing WeChat Offical Account Robots with fun',
    long_description=readme,
    long_description_content_type="text/markdown",
    install_requires=install_requires,
    include_package_data=True,
    license='MIT License',
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: MIT License',
        'Operating System :: MacOS',
        'Operating System :: POSIX',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: Implementation :: CPython',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Utilities',
    ],
    project_urls={
        'Documentation': 'https://zgrobot.readthedocs.io/zh/stable/',
        'Source': 'https://github.com/pylover7/ZgRobot',
        'Tracker': 'https://github.com/pylover7/ZgRobot/issues'
    },
    python_requires='>=3',
    tests_require=['pytest'],
    cmdclass={"pytest": PyTest},
    extras_require={'crypto': ["cryptography"]},
    package_data={'zgrobot': ['contrib/*.html']}
)
