## Importing the required libraries for setting up
from setuptools import find_packages, setup
from typing import List

def get_requirements(file_path:str)->List[str]:
    '''This function returs the list of requirements'''
    requirements = []
    with open(file_path) as file_obj:

        ## read everyline of requirements.txt
        requirements = file_obj.readlines()

        ## while reading a new line in  the requiremetnts.txt we also get to include '\n'
        ## to handle it we replace it
        requirements = [req.replace("\n","") for req in requirements]


## all the params required are written here
setup(
name = 'ML Project',
version = '0.0.1',
author = 'Nithish Yadav',
author_email = 'imyadavcodes@gmail.com',
packages = find_packages(),

## Method for reading and installling all required libraries for the project
install_requires = get_requirements('requirements.txt') 
)