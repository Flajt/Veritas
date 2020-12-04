from setuptools import setup

setup(
    name="Veritas",
    version="0.0.1",
    author_email="tjhannover@gmail.com",
    description="A python package for checking text for false statments via the Semantic Web",
    long_description=open("README.md", "r").read(),
    install_requires=[
        "torch >= 1.5.1",
        "fairseq==0.7.2",
        "tweepy==3.9.0",
        " six==1.15.0",
        "wikipedia==1.4.0"
    ],
)
#Note: The cloned submodule of fairseq is of version 0.6.0, but the working package is version 0.7.2 not something earlier
# tweepy, six and wikipedia are for development only