# setup.py
from setuptools import setup, find_packages

setup(
    name='poly_igdb',
    version='0.1.8',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    package_data={'poly_igdb': ['*.py']},
    install_requires=[
        # Add your dependencies here
    ],
    test_suite='tests',
    tests_require=[
        # Add your test dependencies here
    ],
)