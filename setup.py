import setuptools

with open("README.md", "r") as f:
    long_description = f.read()


setuptools.setup(
    name="rankingmaker"
    version="0.0.1",
    author="Brendan Horst",
    author_email="yoshistar2000@gmail.com",
    url="https://github.com/BrendanHorst/ranking-maker",
    description="Allows you to create a rankng by selecting items from random pairs",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    install_requires=[],
    extras_require=[],
    tests_require=['pytest'],
    python_requires='>=3.6',
)

