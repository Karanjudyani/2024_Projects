from setuptools import find_packages,setup
from typing import List

def get_requirements(file_path:str)->List[str]:
    '''
    this function will return the list of requirements
    '''
    requirements=[]
    with open('requirements.txt') as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]

setup(
    name='2024_Projects',
    version='0.0.1',
    author='Karan J'
    author_email='karanjudyani@gmail.com'
    packages=find_packages(),
    install_rquires=get_requirements('requirements.txt')
)