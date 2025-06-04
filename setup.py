from setuptools import setup, find_packages
from typing import List

HYPHEN_E_DOT = '-e .'

def get_req(file_path: str) -> List[str]:
    with open(file_path) as file:
        requirements = file.readlines()
        requirements = [r.strip() for r in requirements]  # Remove newline chars

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)

        return requirements

setup(
    name='ml',
    author='Rohith',
    version='1.0.0',
    packages=find_packages(),
    install_requires=get_req('requirements.txt')
)
