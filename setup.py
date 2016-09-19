# coding: utf-8
import sys
from setuptools import setup, Command, find_packages

try:
    from pypandoc import convert
    read_md = lambda f: convert(f, 'rst')
except ImportError:
    read_md = lambda f: open(f, 'r').read()

requires_list = []

setup(
    name="genetic",
    version=".".join(map(str, __import__('genetic').__version__)),
    description="General purpose genetic algorithm library",
    long_description=read_md('README.md'),
    author="Sig-ML IIITMK",
    author_email="arjoonn.msccsc5@iiitmk.ac.in",
    url='https://github.com/sig-ml/genetic',
    keywords="Genetic Algorithms Multiprocessing",
    packages=['genetic.py'],
    entry_points="""
        [console_scripts]
        genetic=genetic:main
    """,
    license='MIT',
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        ],
)
