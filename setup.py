"""
Setup script untuk package Calculator
Digunakan untuk build dan distribusi package
"""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="calculator-cicd-demo",
    version="1.0.0",
    author="STQA Student",
    author_email="student@example.com",
    description="Simple calculator untuk demonstrasi CI/CD",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/username/calculator-cicd-demo",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Education",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    python_requires=">=3.8",
    install_requires=[],
    extras_require={
        "dev": [
            "pytest>=7.0.0",
            "pytest-cov>=4.0.0",
            "flake8>=5.0.0",
            "black>=22.0.0",
        ],
    },
)