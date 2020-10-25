import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
        name="example-pkg-IndiePotato",
        version="0.0.1",
        author="Oliver Nock",
        author_email="OliverRobertNock@Gmail.com",
        description="A small example package.",
        long_description=long_description,
        long_description_content_type="text/markdown",
        url="https://github.com/IndiePotato/sampleproject",
        packages=setuptools.find_packages(),
        classifiers=[
            "Programming Language :: Python :: 3",
            "License :: OSI Approved :: MIT License",
            "Operating System :: OS Independent",
        ],
        python_requires='>=3.6',
)
