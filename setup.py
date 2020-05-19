from setuptools import setup
from egit import __version__, __author__, __author_email__

def readme():
    with open('README.md') as f:
        README = f.read()
    return README


setup(
    name="egit",
    version=__version__,
    description="Python Easy Git",
    long_description=readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/basameera/egit",
    author=__author__,
    author_email=__author_email__,
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    packages=["egit"],
    include_package_data=True,
    # install_requires=["requests"],
    entry_points={
        "console_scripts": [
            "egit=egit.cli:main",
            "eg=egit.cli:main",
        ]
    },
)