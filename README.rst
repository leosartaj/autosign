Autosign
*********
Add your signature to your **python** files.
Use under **caution**, work in progress.

Installation
============
autosign can be installed using pip
::
  pip install autosign

Uninstalling
============
autosign can be uninstalled using pip
::
  pip uninstall autosign

Dependencies
============
autosign is based on Python 2.7.

Documentation
============

Writing valid signature template
--------------------------------
A valid signature uses syntax very closely related to python comments. 

* A signature should start and end with **'##'**.
* Every line other than the start and end should start with **'#'**. 
* Blank lines are allowed before and after starting a signature. 
* Line starting with **'#!'** is allowed before starting a signature. 
  
Examples can be seen in examples directory. All the python files in this package have been signed using 'examples/template1.txt'.

Signing python files
--------------------
autosign can be used for signing python files
::
  autosign signfile target [options]

Run the following command, for various options.
::
  autosign --help 
