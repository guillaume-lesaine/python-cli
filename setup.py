from typing import Dict

from setuptools import find_packages, setup

version: Dict[str, str] = {}
with open("src/myclilibrary/version.py") as f:
    exec(f.read(), version)

with open("README.md") as f:
    long_description = f.read()

setup(
    name="myclilibrary",
    version=version["__version__"],
    description="Library CLI Test",
    author="Guillaume Lesaine",
    author_email="guillaume.lesaine@protonmail.com",
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=["click"],
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    entry_points={
        "console_scripts": ["myclilibrary=myclilibrary.__main__:cli"]
    },
    python_requires=">=3.7",
)
