# setup.py is used to build the application as a package itself.

from setuptools import find_packages,setup
from typing import List


HYPHEN_E_DOT="-e ."
def get_requirements(file_path:str)->List[str]:
    '''
    this function will return the list of requirements
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
setup(
    name="MLprojects",
    version='0.0.1',
    author='harsh',
    author_email='harsh.p.walia@gmail.com',
    package=find_packages(),
    install_requires=get_requirements('requirements.txt')
)