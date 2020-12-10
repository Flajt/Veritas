from setuptools import setup

setup(
    name="Veritass",
    version="0.0.5",
    author="Flajt",
    author_email="tjhannover@gmail.com",
    description="A python package for checking text for false statments via the Semantic Web",
    long_description=open("README.md", "r").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/Flajt/Veritas",
    keywords="FakeNews ML DeepLearning fairseq",
    license="GNU General Public License v3.0",
    data_files=[('data', ['Veritas/data/dicts/dict.en.txt', 'Veritas/data/dicts/dict.sparql.txt'])],
    packages=["Veritas"],
    package_dir = {"Veritas":"Veritas"},
    install_requires=[
        "torch >= 1.5.1",
        "fairseq >= 0.6.1",
        "spacy>=2.3.2",
        "tqdm>=4.49.0"
    ],
    python_requires = ">3.5.0",
    exclude_package_data={"": ["checkpoint_best.pt"]},
    include_package_data = True,
    classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Libraries',
    "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",   # Again, pick a license
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)
#Note: The cloned submodule of fairseq is of version 0.6.0, but the working package is version 0.7.2 not something earlier
# tweepy, six and wikipedia are for development only