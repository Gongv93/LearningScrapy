from setuptools import setup, find_packages

setup(
    name='example_1',
    version='1.0',
    packages=find_packages(),
    entry_points={'scrapy': ['settings = example_1.settings']},
)
