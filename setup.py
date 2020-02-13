import os
import setuptools

with open(os.path.join(os.path.dirname(__file__), "README.md"), "rt") as fh:
    long_description = fh.read()

test_requires = [
    "pytest",
    "pylint>=1.6.5",
]

setuptools.setup(
    name="diraccfg",
    use_scm_version=True,
    author="Federico Stagni",
    description="DIRAC cfg files reader",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/DIRACGrid/cfg",
    packages=setuptools.find_packages(exclude=["tests"]),
    license="GPL-3.0-only",
    test_suite="tests",
    setup_requires=["setuptools_scm"],
    install_requires=[],
    extras_require={
        'testing': test_requires,
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GPLv3 License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=2.7",
)
