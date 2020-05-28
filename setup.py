from setuptools import setup

setup(
    name='snapshotalyzer-3000',
    version='0.1',
    author='alpha-r-zero',
    packages=['shotty'],
    install_requires=[
        'click',
        'boto3'
    ],
    entry_point='''
        [console_scripts]
        shotty=shotty.shotty:cli
    ''',
)
