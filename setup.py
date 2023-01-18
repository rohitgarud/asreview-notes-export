# based on https://github.com/pypa/sampleproject
# MIT License

from io import open
from os import path

# Always prefer setuptools over distutils
from setuptools import find_namespace_packages
from setuptools import setup

import versioneer

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='asreview-notes-export',
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    description='ASReview notes export extension',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/rohitgarud/asreview-notes-export',
    author='Rohit Garud',
    author_email='rohit.garuda1992@gmail.com',
    classifiers=[
        'Development Status :: 1 - Planning',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ],
    keywords='asreview notes export',
    packages=find_namespace_packages(include=['asreviewcontrib.*']),
    install_requires=[
        "asreview>=1,<2",
    ],
    extras_require={},
    entry_points={
        "asreview.entry_points": [
            "notes_export = asreviewcontrib.insights.entrypoint:ExportEntryPoint",
        ]
    },
    project_urls={
        'Bug Reports': "https://github.com/rohitgarud/asreview-notes-export/issues",
        'Source': "https://github.com/rohitgarud/asreview-notes-export",
    },
)