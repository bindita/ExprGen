# ExprGen: Learning to Generate 3D Stylized Character Expressions from Humans
## [paper](https://homes.cs.washington.edu/~bindita/papers/2Dto3Dexpr_WACV.pdf) | [database](http://grail.cs.washington.edu/projects/deepexpr/ferg-3d-db.html)

This repository contains python code to generate facial expressions on 3D MAYA rigs. There are two files in this repository:

* savetomaya.py, which reads the rig parameters and their values from a CSV file and sets the parameter values of the 3D rig.

* extractfrommaya.py, which extracts rig parameters and their values from a 3D rig and saves them in a CSV file.

Prerequisites:

* Install [MAYA](https://www.autodesk.com/education/free-software/maya)

* Set up system environment for mayapy according to [these](https://help.autodesk.com/cloudhelp/2016/CHS/Maya-Tech-Docs/PyMel/install.html#install-system-env) instructions

Usage:

* mayapy savetomaya.py -icsv -irig

*

Fill the agreement form linked on the database webpage to get access to the full versions of the CSV files.