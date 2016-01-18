__author__ = '@capJavert'

from setuptools import setup

setup(
    name='renamer',
    version='0.2',
    summary='shell tool',
    homepage='https://github.com/capJavert/renamer',
    author='capJavert',
    author_email='/',
    license='MIT',
    description='Simple shell tool for file renaming written in python',
    platforms='windows, linux',

    py_modules=['renamer'],
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        renamer=renamer:main
    ''',
)
