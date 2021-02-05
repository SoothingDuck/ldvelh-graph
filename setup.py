import os
from setuptools import setup, find_packages
here = os.path.abspath(os.path.dirname(__file__))

install_requires = ['EbookLib', 'beautifulsoup4', 'networkx', 'wheel']

setup(
    name="LdvelhGraph",
    version="0.1",
    url="https://github.com/mrcanard/ldvelh-graph",
    author="Yvan Aillet",
    author_email="yvanaillet@gmail.com",
    license="MIT",
    packages=find_packages(),
    install_requires=install_requires,
    package_data={'ldvelh': ['data/*.epub', 'data/*.pdf']},
)
