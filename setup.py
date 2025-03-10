from setuptools import setup, find_packages

setup(
    name="records",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "requests",
        "pandas"
    ],
    author="Yuki Ogawa",
    author_email="yo2368@columbia.edu",
    description="A package to fetch and process GBIF records.",
    url="https://github.com/yvnvii/records",
    classifiers=[
        "Programming Language :: Python :: 3",
    ],
)

