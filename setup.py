from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="odd_even_classifier",
    version="0.1.0",
    packages=["odd_even_classifier"],
    install_requires=[
        "tensorflow>=2.0.0",
        "numpy",
    ]
)

