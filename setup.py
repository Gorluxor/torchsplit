from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
        name="torchsplit",
        version="0.1.0",
        packages=find_packages(),
        description="Save contacts from your terminal",
        long_description=long_description,
        long_description_content_type="text/markdown",
        url="https://github.com/Gorluxor/torchsplit",
        author="Aleksandar Cvejic",
        author_email="cvejicaca@gmail.com",
        license="MIT",
        classifiers=[
            "License :: OSI Approved :: BSD License",
            "Programming Language :: Python :: 3.7",
        ],
        keywords = ['split', 'dataset', 'into', 'test', 'validation'],
        install_requires=[
            "scikit-learn",
            "torch",
            "numpy",
            'torchvision',
            ],
        )