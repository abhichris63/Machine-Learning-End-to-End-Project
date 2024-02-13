from setuptools import setup,find_packages
from typing import List


# Declaring variables for setup function.
Project_Name = "house-predictor"
Version = "0.0.1"
Author = "Abhishek B"
Description = "This is the House Price Prediction End to End Machine Learning Project"
Packages = ["Housing"]
REQUIREMENTS_FILE_NAME = "requirements.txt"



def get_requirements_list()->List[str]:
    """
    Description: This function is going to return list of requirement
    mentioned in requirements.txt file

    return This function is going to return a list which contain name
    of libraries mentioned in requirements.txt file.
    """
    with open(REQUIREMENTS_FILE_NAME) as requirement_file:
        return requirement_file.readlines().remove("-e .")

setup(
    name=Project_Name,
    version=Version,
    author=Author,
    description=Description,
    packages=find_packages(), 
    install_requires = get_requirements_list()

)

if __name__ == "__main__":
    print(get_requirements_list())
