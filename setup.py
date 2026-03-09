from setuptools import setup, find_packages
from typing import List

def get_requirements(file_path)->List[str]:
    '''This function will return the list of requirements'''
    requirements = []

    with open(file_path, 'r') as file_obj:
        requirements = file_obj.read().splitlines()
        if '-e.' in requirements:
            requirements.remove('-e.')
    return requirements

setup(
    name='mlproject',
    version='0.0.1',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    author='Ravi Yadav',
    author_email='ravipratapyadav1109@gmail.com',
    install_requires=get_requirements('requirements.txt')
)