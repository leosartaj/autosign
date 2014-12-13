Autosign
*********
Add your signature to your **python** files.

.. image:: https://travis-ci.org/leosartaj/autosign.svg
    :target: https://travis-ci.org/leosartaj/autosign

Installation
============
autosign can be installed using pip::

    pip install autosign

Uninstalling
============
autosign can be uninstalled using pip::

    pip uninstall autosign

Dependencies
============
autosign is based on Python 2.7.

Documentation
=============

Signing python files
--------------------
autosign can be used for signing python files::

    autosign signfile target [options]

autosign signs python files only.
Run the following command, for various options.::

    autosign --help 

Removing sign from python files
-------------------------------
autosign provides a utility, **remsign** for removing sign from signed python files::

    remsign target [options]

remsign checks python files only.
Run the following command, for various options.::

    remsign --help 

Checking a package
------------------
autosign provides a utility, **listsign** for collecting statistics::

    listsign target [options]

listsign checks python files only.
Run the following command, for various options.::

    listsign --help 

Signrc
------
Autosign utilizes signrc to sign, remove and list signed/un-signed files. The meaning of options is as follows.

* **ext** tells the utilities to look for files with only that extension
* **Start** defines the starting character sequence of a signature
* **line** defines the character sequence with whice every line(except start and end) should start of a valid signature
* **end** defines the ending character sequence of a signature
* **blank** (boolean) allows/forbids usage of blank line before start or after end of a signature
* **allow** defines a special regular expression. Matching to which a line can be allowed before the start of a signature.
  
Examples can be seen in examples directory. All the python files in this package have been signed using **examples/templates/template1.txt** using **examples/signrc/signrc_py**.

* --init option can be used for generating a very basic signrc
* All the utilities look for **.signrc** first in cwd, then in home directory by default.

Bugs
====
.. |issues| replace:: https://github.com/leosartaj/autosign/issues

For filing bugs raise an issue at |issues|
