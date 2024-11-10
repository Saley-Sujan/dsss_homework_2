# setup.py

from setuptools import setup, find_packages

setup(
    name='math_quiz',  # Replace with your package name
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    license='MIT',
    description='A simple math quiz application.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Saley-Sujan',
    author_email='saleysujan96@gmail.com',
    url='https://github.com/Saley-Sujan/dsss_homework_2.git',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
    ],
    scripts=['scripts/math_quiz'],
    install_requires=[
        # List dependencies here if needed
    ],
)
