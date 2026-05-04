from setuptools import setup, find_packages
setup(name="stealth-core", version="1.0.0", packages=find_packages(),
      install_requires=["psutil"], python_requires=">=3.10")
