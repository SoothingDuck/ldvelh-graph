import os
from setuptools import setup, find_packages
here = os.path.abspath(os.path.dirname(__file__))

install_requires = [
    'EbookLib',
    'beautifulsoup4',
    'networkx'
    ]

setup(
    name="LdvelhGraph",
    version="0.1",
    url="https://github.com/mrcanard/ldvelh-graph",
    author="Yvan Aillet",
    author_email="yvanaillet@gmail.com",
    license="MIT",
    packages=find_packages(),
    install_requires=install_requires,
    package_data={
        'ldvelh': ['data/*.epub', 'data/*.pdf']
    },
)

# setup(name='funniest',
#       version='0.1',
#       description='The funniest joke in the world',
#       url='http://github.com/storborg/funniest',
#       author='Flying Circus',
#       author_email='flyingcircus@example.com',
#       license='MIT',
#       packages=['funniest'],
#       install_requires=[
#           'markdown',
#       ],
#       zip_safe=False)
