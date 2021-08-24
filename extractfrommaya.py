'''
-------------------------
Code to extract rig parameters values from a MAYA rig and save them in a CSV file

Run with default inputs:
mayapy extractfrommaya.py

If you want to specify the character (one of Mery, Bonnie, Ray and Malcolm), say Bonnie, run:
mayapy extractfrommaya.py -char Bonnie

To set input rig file name, run:
mayapy extractfrommaya.py -irig /path/to/input/rig/file
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
parser.add_argument('-char', '--character', default='Mery',
                    help='name of input character: Mery, Bonnie, Ray or Malcolm')
parser.add_argument('-irig', '--inputrig', default='Mery.mb',
                    help='file name of input MAYA rig')

### Parse input arguments
args = parser.parse_args()

### Set the variables to appropriate values
MayaRigFilename = args.inputrig
CSVfilename = MayaRigFilename.split('/')[-1].split('.')[0] + '.csv'

if args.character is 'Mery':
	Facial_Group_Name, Group_Name_Start = 'Mery_grp_cn_facials_controls', 'Mery_ac_'
elif args.character is 'Bonnie':
	Facial_Group_Name, Group_Name_Start = 'BONNIE:BONNIE_ANIM_FACE', 'BONNIE:BONNIE_ANIM_FACE_'
elif args.character is 'Ray':
	Facial_Group_Name, Group_Name_Start = 'CGTarian_Ray_2015_09_08:ray_face_controls', 'CGTarian_Ray_2015_09_08:ray_'
	# also use the Facial_Group_Name = 'CGTarian_Ray_2015_09_08:ray_sk_cn_head_offset'
elif args.character is 'Malcolm':
	Facial_Group_Name, Group_Name_Start = 'malcolm_v200:headControls', 'malcolm_v200:ctl'
else:
	print('Character name must be one of Mery, Bonnie, Ray and Malcolm')
	quit()


### Helper function to extract attributes from the opened rig
def extractAttributes():
	attrAndValues = {}	

	### list all descendent nodes of type transform
	allNodes = cmds.listRelatives(Facial_Group_Name, allDescendents=True, type='transform')
	
	for node in allNodes: 
		attrList = None
		if '_parentConstraint' in node:
			continue 

		### UNCOMMENT for BONNIE and RAY
		# all relevant transform nodes have associated shapes; if not, they are group names
		#if not cmds.listRelatives(node,shapes=True):
		#	continue

		### for each valid node, extract the names of the keyable attributes
		if str(node).startswith(Group_Name_Start):
			attrList = cmds.listAttr(node, keyable=True)		
		
		### get the full attribute name and its corresponding value for each attribute
		if attrList:
			for attr in attrList:				
				name = node + "." + attr # attribute name in the form "NODE_NAME.ATTR_NAME"
				value = cmds.getAttr(name) # attribute value
				attrAndValues[name] = value
	
	return attrAndValues

### Main function
if __name__ == '__main__':	
	orderedAttr = None
	with open(CSVfilename, 'w') as output:
		writer = csv.writer(output)

		### uncomment if you want to read multiple files in folders and subfolders
		#for path, subdirs, rigFiles in os.walk(folder):
		#	for rig in rigFiles:
		
		### uncomment if your folder has some non-maya files
		#base, ext = os.path.splitext(MayaRigFilename)
		#if ext != '.mb' and ext != '.ma': # skip if file isn't a rig (there could be some hidden files)
		#	continue

		### open the maya file
		print 'Opening file: ', MayaRigFilename, '...'
		fullpath = MayaRigFilename #os.path.join(path, rig)
		cmds.file(fullpath, o=True, iv=True, force=True)		
		
		### set the time frames to be extracted; default: all
		startFrame = int(cmds.getAttr('defaultRenderGlobals.startFrame'))
		endFrame = int(cmds.getAttr('defaultRenderGlobals.endFrame'))

		### loop over each time frame
		for i in range(startFrame, endFrame + 1): 
			cmds.currentTime(i)
			print 'Extracting for frame', i

			### call helper function for extracting attributes
			attrAndValues = extractAttributes()

			### write the attribute names in the first row of the csv file 
			if not orderedAttr:
				orderedAttr = list(attrAndValues.keys())
				orderedAttr.sort()
				orderedAttr.insert(0, 'file_name')
				# some file has an extra attribute: "Mery_ac_rg_iris1.translateY"; ignore this attribute
				ignore = 'Mery_ac_rg_iris1.translateY'
				if ignore in orderedAttr:
					orderedAttr.remove(ignore)
				writer.writerow(orderedAttr)

			### write the attribute values in the remaining rows of the csv file 
			attrAndValues['file_name'] = fullpath + "_" + str(i).zfill(4)
			row = []
			for attr in orderedAttr:
				row.append(attrAndValues[attr])
			writer.writerow(row)