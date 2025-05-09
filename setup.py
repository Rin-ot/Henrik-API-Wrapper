from setuptools import setup, find_packages

setup(
    name = "Henrik_API_Wrapper", 
    version = "0.1", 
    packages = find_packages(), 
    install_requires = ["requests"], 
    author = "Rin-ot", 
    description = "Python Wrapper for Henrik-Dev's Unofficial VALORANT API.", 
    long_description = open("README.md").read(), 
    long_description_content_type = "text/markdown", 
    url = f"https://github.com/Rin-ot/Henrik-API-Wrapper", 
    classifiers = [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License"
    ], 
    python_requires = ">=3.7", 
)
