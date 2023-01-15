from setuptools import setup, find_packages

setup(
    name="iris-ml-app",
    version="0.0.2",
    description="An app about color of flowers",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=["streamlit", "pandas", "sklearn", "sklearn.ensemble"],
    entry_points={"console_scripts": ["iris-ml-app = src.main:main"]},
)