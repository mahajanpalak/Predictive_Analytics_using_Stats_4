from setuptools import setup, find_packages

setup(
    name="topsis-palak-102497010",   # Must match PyPI name
    version="1.0.1",                 # Increase version (VERY IMPORTANT)
    author="Palak",
    author_email="palak@example.com",
    description="Implementation of TOPSIS method for decision making",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    license="MIT",
    packages=find_packages(),
    install_requires=[
        "pandas",
        "numpy",
        "openpyxl"
    ],
    entry_points={
        "console_scripts": [
            "topsis=topsis_palak_102497010.topsis:main"
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License"
    ],
    python_requires=">=3.6",
)
