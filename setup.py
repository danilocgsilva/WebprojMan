from setuptools import setup

VERSION = "0.0.1"

def readme():
    with open("README.md") as f:
        return f.read()

setup(
    name="webprojman",
    version=VERSION,
    description="Manages web project",
    long_description_content_type="text/markdown",
    long_description=readme(),
    keywords="web project personal management",
    url="https://github.com/danilocgsilva/WebprojMan",
    author="Danilo Silva",
    author_email="contact@danilocgsilva.me",
    packages=["webprojman"],
    entry_points={"console_scripts": ["projman=webprojman.__main__:main"],},
    include_package_data=True
)

