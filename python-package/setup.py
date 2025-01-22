from setuptools import setup, find_packages

setup(
    name="api-key-manager-client",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[],
    author="Iván San Martín",
    author_email="ivansanmartin987@gmail.com",
    description="A simple package for api-key-manager",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/ivansanmartin/api-key-manager-client",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries",
    ],
    python_requires='>=3.11.4',
)