from setuptools import setup


def readfile(filename):
    with open(filename, 'r+') as f:
        return f.read()


setup(
    name="ascii",
    version="1",
    description="CLI to interact with the ASCII-table",
    long_description=readfile('README.md'),
    author="Tommaso Peduzzi @tommasopeduzzi",
    url="",
    py_modules=['main'],
    entry_points={
        'console_scripts': [
            'ascii = main:asciicli'
        ]
    },
)