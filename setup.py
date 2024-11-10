from setuptools import setup, find_packages

setup(
    name="math-quiz",
    version="1.0",
    packages=find_packages(),
    install_requires=[],
    author="Saley-Sujan",
    author_email="saleysujan96@gmail.com",
    description="A simple math quiz game with random questions.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/Saley-Sujan/dsss_homework_2",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)