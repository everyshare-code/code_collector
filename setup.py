from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="code-collector",
    version="0.1.0",
    author="Park Junyoung",
    author_email="park20542040@gmail.com",
    description="A tool to collect user-written code from a project",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/everyshare-code/code_collector",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
    entry_points={
        "console_scripts": [
            "code-collector=code_collector.cli:main",
        ],
    },
)