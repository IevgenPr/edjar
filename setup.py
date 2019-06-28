# start tests from this directory:
# python3 -m pytest tests --disable-pytest-warnings
from setuptools import find_packages, setup

setup(
    name = "edjar",
    version = "0.0.1",
    url = "http://example.com",
    license="NONE",
    description = "Application to keep track of personal courses from various providers",
    packages = find_packages(),
    include_package_data=True,
    install_requires=[
            'flask',
    ],
    extras_require={
        'test': [
            'pytest',
            'coverage',
        ],
    },
        
)
