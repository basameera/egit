from setuptools import setup

def readme():
    with open('README.md') as f:
        README = f.read()
    return README


setup(
    name="egit",
    version="0.0.1",
    description="Python Easy Git",
    long_description=readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/basameera/egit",
    author="Sameera Sandaruwan",
    author_email="basameera@protonmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
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