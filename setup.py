import pathlib
from setuptools import setup

HERE = pathlib.Path(__file__).parent
README = (HERE / "README.md").read_text()

setup(
    name="rfc1924",
    version="0.3.0",
    description="Implementation of RFC 1924",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/0xflotus/rfc1924",
    author="0xflotus",
    author_email="0xflotus+pypi@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
    ],
    packages=["rfc1924"],
    include_package_data=True,
    install_requires=[],
    tests_require=["pytest"],
)
