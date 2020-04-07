# ExprGen: Learning to Generate 3D Stylized Character Expressions from Humans
## [paper](https://homes.cs.washington.edu/~bindita/papers/2Dto3Dexpr_WACV.pdf) | [database](http://grail.cs.washington.edu/projects/deepexpr/ferg-3d-db.html)

<p align="center"> 
<img src="https://homes.cs.washington.edu/~bindita/images/wacv2018.gif" width="500px">
</p>

This repository contains python code to generate facial expressions on 3D MAYA rigs. There are two files in this repository:

* `savetomaya.py`, which reads the rig parameters and their values from a CSV file and sets the parameter values of the 3D rig.

* `extractfrommaya.py`, which extracts rig parameters and their values from a 3D rig and saves them in a CSV file. (*coming soon!*)

An example CSV file, `input.csv`, is provided in this repository. The format of the CSV files is as follows:
- The first row contains the names of the facial parameters of the 3D rig.
- Each of the remaining rows contains the values of those parameters for a particular expression.
- The first column contains the name of the expression. The expression category is mentioned within the name.

Fill the agreement form linked on the database webpage to get access to the full versions of all the CSV files.

## Prerequisites:

* Install [MAYA](https://www.autodesk.com/education/free-software/maya). Optionally, you can learn more about MAYA controls [here](https://area.autodesk.com/tutorials/series/intro-to-maya/).

* Set up system environment for mayapy according to [these](https://help.autodesk.com/cloudhelp/2016/CHS/Maya-Tech-Docs/PyMel/install.html#install-system-env) instructions.

## Basic usage:

* Download the RAR file from [here](https://www.meryproject.com/download), extract the `.mb` (MAYA) file, and save it as `Mery.mb` in the current folder.

* Run the following command from the terminal:
```
$ mayapy savetomaya.py
```
This will overwrite the original `Mery.mb` file (not recommended!). To avoid this, you can rename the file to be saved to `Mery_new.mb` using:
```
$ mayapy savetomaya.py -rename
```

In case the terminal cannot run mayapy directly, you can specify the entire path to `mayapy.exe` to run it. On MacOS with MAYA version 2018, you can do:
```
$ /Applications/Autodesk/maya2018/Maya.app/Contents/bin/mayapy savetomaya.py -rename
```

## Full usage:

By default, the python file reads `input.csv` (input csv file) and `Mery.mb` (input rig file) from the current directory. Once you have the MAYA files and CSV files for all the four characters in our dataset, you can change the paths to the input files using:
```
$ mayapy savetomaya.py -icsv /path/to/csv/file -irig /path/to/rig/file -rename
```
You can then open the newly generated MAYA file in MAYA and see the results. You can also [render](https://knowledge.autodesk.com/support/maya/learn-explore/caas/CloudHelp/cloudhelp/2019/ENU/Maya-Rendering/files/GUID-1F2C09E9-FBE1-4F18-9151-D7FF25D5CA12-htm.html) the current view to get the results in 2D.

In case you animate the rig within MAYA (manipulate the rig parameter values), you can extract the new parameter values using:
```
$ mayapy extractfrommaya.py -char <character name> -irig /path/to/rig/file
```
For example, to extract parameter values for character `Mery` from `Meryfile.mb`, use:
```
$ mayapy extractfrommaya.py -char Mery -irig Meryfile.mb
```
and this will generate a CSV file named `Meryfile.csv` in the current directory.

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
