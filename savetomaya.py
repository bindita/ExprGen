'''
-------------------------
Code to read rig parameters from CSV file and set the parameters in 3D MAYA rig
Run with default inputs:
mayapy savetomaya.py

If you want to rename your input file, say maya.mb to maya_new.mb, run:
mayapy savetomaya.py -rename

To set input csv file name and input rig file name, run:
mayapy savetomaya.py -icsv /path/to/input_csv_file -irig /path/to/input_rig_file
-------------------------
'''

### import functions to load and initialize mayapy
import maya.standalone
maya.standalone.initialize()
import maya.cmds as cmds

### import other functions
import csv, argparse, os

### Add input arguments
parser = argparse.ArgumentParser()
parser.add_argument('-icsv', '--inputcsv', default='input.csv', #'human_mery_anger copy', 'mery_test_seq
                    help='file name of input csv')
parser.add_argument('-irig', '--inputrig', default='Mery.mb',
                    help='file name of input MAYA rig')
parser.add_argument('-rename', action='store_true',
                    help='renames the modified file')

### Parse input arguments
args = parser.parse_args()

### Set the variables to appropriate values
MayaAttributesFilename = args.inputcsv

MayaRigFilename = args.inputrig

MayaRigFilename_new = MayaRigFilename.split('/')[-1]

if args.rename:
	MayaRigFilename_new = MayaRigFilename_new.replace('.m','_new.m')

### Read all parameters from CSV file
with open(MayaAttributesFilename, 'r') as csvfile:
	parameters = list(csv.reader(csvfile))

### Get number of parameters and number of examples
Nexamples, Nparameters = len(parameters)-1, len(parameters[0])

### Open the MAYA rig
cmds.file(MayaRigFilename, o=True, force=True)

### For each example
for e in range(Nexamples):
	### Update the current time frame to be edited
	cmds.currentTime(e+1, edit=True)
	### For each parameter (ignore 1st column containing name)
	for i in range(1,Nparameters):

		### Get the object name and attribute name of the parameter
		### For example, if parameter name is browLeft.translateX,
		### objname = browLeft, attrname = translateX
		objname, attrname = parameters[0][i].split('.')

		### If object name contains reference, get two separate variables
		if len(objname.split(':')) > 1:
			objname = objname.split(':')[-1]
			objnameNOreference = parameters[0][i].split(':')[-1]
		else:
			objnameNOreference = parameters[0][i]	

		### Update the parameter value
		cmds.setAttr(objnameNOreference, float(parameters[e+1][i]), keyable=True)
		### Key frame the updated parameter 
		cmds.setKeyframe(objname, at=attrname)

### Set the new file name and save the MAYA file in the same directory as the python file (current directory)
cmds.file(rename=os.getcwd()+'/'+MayaRigFilename_new)
cmds.file(save=True)