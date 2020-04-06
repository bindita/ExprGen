# ExprGen: Learning to Generate 3D Stylized Character Expressions from Humans
## [paper](https://homes.cs.washington.edu/~bindita/papers/2Dto3Dexpr_WACV.pdf) | [database](http://grail.cs.washington.edu/projects/deepexpr/ferg-3d-db.html)

<p align="center"> 
<img src="https://homes.cs.washington.edu/~bindita/images/wacv2018.gif" width="500px">
</p>

This repository contains python code to generate facial expressions on 3D MAYA rigs. There are two files in this repository:

* `savetomaya.py`, which reads the rig parameters and their values from a CSV file and sets the parameter values of the 3D rig.

* `extractfrommaya.py`, which extracts rig parameters and their values from a 3D rig and saves them in a CSV file. (*coming soon!*)

An example CSV file, `input.csv`, is provided in this repository. The format of the CSV files is as follows:
- The first row contains the names of the parameters of the 3D rig.
- Each of the remaining rows contains the values of those parameters for a particular expression.
- The first column contains the name of the expression. The expression category is mentioned within the name.

Fill the agreement form linked on the database webpage to get access to the full versions of all the CSV files.

## Prerequisites:

* Install [MAYA](https://www.autodesk.com/education/free-software/maya). Optionally, you can learn more about MAYA controls [here](https://area.autodesk.com/tutorials/series/intro-to-maya/).

* Set up system environment for mayapy according to [these](https://help.autodesk.com/cloudhelp/2016/CHS/Maya-Tech-Docs/PyMel/install.html#install-system-env) instructions.

## Basic usage:

* Download the RAR file from [here](https://www.meryproject.com/download), extract the `.mb` (MAYA) file, and save it as `Mery.mb` in the current folder.

* Run the following command from the terminal:

`
$ mayapy savetomaya.py
`

This will overwrite the original `Mery.mb` file (not recommended!). To avoid this, you can rename the file to be saved to `Mery_new.mb` using:

`
$ mayapy savetomaya.py -rename
`

By default, the python file reads `input.csv` (input csv file) and `Mery.mb` (input rig file) from the current directory. In order to change their paths, you can use:

`
$ mayapy savetomaya.py -icsv /path/to/csv/file -irig /path/to/rig/file
`

## Full usage:

Coming soon!

## Citation:

If you use this dataset, please cite our paper:

```
@inproceedings{learningstylizedcharacters, 
  author={D. {Aneja} and B. {Chaudhuri} and A. {Colburn} and G. {Faigin} and L. {Shapiro} and B. {Mones}}, 
  booktitle={2018 IEEE Winter Conference on Applications of Computer Vision (WACV)}, 
  title={Learning to Generate 3D Stylized Character Expressions from Humans}, 
  pages={160-169}, 
  year={2018}, 
  month={March}
}
```
