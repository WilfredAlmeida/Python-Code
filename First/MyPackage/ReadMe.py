# In Python packages can be created using folder just like java but for python to understand that a folder is a package
# we need to define a file named '__init__.py' in the package. This file specifies that the folder is a package.
# This file can be empty or can have some initialization code for the package. A python package can have subpackages.
# Every sub-package will have its own __init__.py file indicating the folder as a package. While importing packages,
# Python looks in the list of directories defined in 'sys.path'. So in our project if we make a package it will be
# available only for our project. If we want to make a package universal than we need to make in into 'site-packages'
# folder in the installation directory.
# C:\\Users\\Wilfred Almeida\\AppData\\Local\\Programs\\Python\\Python37\\lib\\site-packages in our case.
