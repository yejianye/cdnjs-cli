import setuptools, sys

setuptools.setup(
    name="fetchr",
    version='0.1.0',
    license="MIT",

    author="Ryan Ye",
    author_email="yejianye@gmail.com",
    url="https://github.com/yejianye/fetchr",

    description="A tool for downloading frequently-used Javascript/CSS libraries.",
    long_description=open("README.md").read(),
    keywords=[],
    classifiers=[
        "Environment :: Console",
        "Development Status :: 3 - Alpha",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Environment :: Other Environment",
        "Topic :: Utilities",
        ],
    entry_points={
        'console_scripts': [
            'fetchr = fetchr.cli:main',
        ]
    },
    install_requires=['sh', 'slimit', 'cssmin', 'requests', 'argh'],
    packages=['fetchr', 'fetchr.packages'],
)
