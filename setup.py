from setuptools import find_packages, setup
import os

def get_requirements(path:str):
    '''
    This function returns the a list of all the required packages
    '''
    requirements = []
    with open("requirements.txt", "r") as file:
        requirements = file.readlines()
        requirements = [package.replace("\n", "") for package in requirements]
    
    if "-e ." in requirements:
        requirements.remove("-e .")
    
    return requirements



setup(
    name="ml_project",
    version="0.0.1",
    author="Alex Maggioni",
    author_email="veralex1000@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt")
)