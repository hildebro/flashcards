import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="flashcards",
    version="0.0.1",
    author="Alexander Hildebrandt",
    author_email="alex@hillburn.net",
    description="Create flashcards on PDFs to print and cut out",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/hildebro/flashcards",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
)
