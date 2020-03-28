from setuptools import find_packages, setup

setup(
    name="LdvelhGraph",
    version="0.1",
    url="https://github.com/mrcanard/ldvelh-graph",
    author="Yvan Aillet",
    author_email="yvanaillet@gmail.com",
    license="MIT",
    packages=find_packages(),
    install_requires=[
        "pdfminer.six",
    ],
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
