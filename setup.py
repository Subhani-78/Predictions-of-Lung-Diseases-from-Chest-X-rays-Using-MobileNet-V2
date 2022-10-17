from setuptools import setup, find_packages
from typing import List

# Declaring setup function variables
PROJECT_NAME = "MOBILENETV2-LUNG-DISEASE-CLASSIFIER"
VERSION = "0.0.1"
AUTHOR = "Mujeeb Subhani"
DESCRIPTION = "Developed a classification and prediction model for lung pathologies of frontal thoracic X-rays using a modified model MobileNet V2." 

REQUIREMENT_FILE_NAME = "requirements.txt"
HYPHEN_E_DOT = "-e ."

def get_requirements_list() -> List[str]:

    with open(REQUIREMENT_FILE_NAME) as requirement_file:
        requirement_list = requirement_file.readlines()
        requirement_list = [requirement_name.replace("\n", "") for requirement_name in requirement_list]
        if HYPHEN_E_DOT in requirement_list:
            requirement_list.remove(HYPHEN_E_DOT)
        return requirement_list

setup(
    name=PROJECT_NAME,
    version=VERSION,
    description=DESCRIPTION,
    author=AUTHOR,
    packages=find_packages(),
    install_requires=get_requirements_list() 
)
