import setuptools

fh = open("README.md", "r")
long_description = fh.read()
fh.close()

setuptools.setup(
    name="cleverfetch-pkg-dmarienburg",
    version="1.0",
    author="David Marienburg",
    author_email="david.marienburg@gmail.com",
    description="A simple script for automating your downloads of data from the Clever sftp site",
    long_description=long_description,
    url="https://github.com/dmarienburg/CleverFetch",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Langauge :: Python :: 3",
        "License :: MIT License",
        "Operating System :: OS Independent"
    ],
    python_requires=">=3.0"
)