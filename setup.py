from setuptools import setup, find_packages
setup(name="stealth-core", version="1.2.0", packages=find_packages(),
    install_requires=["psutil>=5.9.0", "pyobjc-framework-Quartz>=10.0", "prometheus-client>=0.18.0", "pyyaml>=6.0"],
    extras_require={"dev": ["pytest>=8.0", "mypy>=1.8", "black>=24.0", "ruff>=0.3", "pre-commit>=3.6"]},
    python_requires=">=3.11")
