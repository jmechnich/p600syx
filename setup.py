#!/usr/bin/env python3

from setuptools import setup  # type: ignore

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="p600syx",
    author="Joerg Mechnich",
    author_email="joerg.mechnich@gmail.com",
    license="GNU GPLv3",
    description="Python module for handling MIDI SysEx dumps from the Sequential Circuits Prophet-600 analog synthesizer.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jmechnich/p600syx",
    use_scm_version={"local_scheme": "no-local-version"},
    setup_requires=["setuptools_scm"],
    install_requires=["PyGithub"],
    scripts=["p600_syxdump"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: POSIX :: Linux",
    ],
    python_requires=">=3.8",
)
