from setuptools import setup

with open('README.md', 'r') as fh:
    long_description = fh.read()

setup(
    name='bitstore',
    version='0.0.1',
    description='This library contains functions to create, interpret and manipulate sequences of bits stored in integers.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    py_modules=['bitstore'],
    package_dir={'': 'src'},
    extras_require= {
        "dev": [
            "pytest>=6.1.2",
        ],
    },
    # install_requires = []
)