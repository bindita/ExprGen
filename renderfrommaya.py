### import functions to load and initialize mayapy
import maya.standalone
maya.standalone.initialize()
import maya.cmds as cmds

### Add input arguments
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('-irig', '--inputrig', default='Mery.mb',
                    help='file name of input MAYA rig')
parser.add_argument('-dirname', '--directoryname', default = '',
					help='renames the modified file')

### Parse input arguments
args = parser.parse_args()

### open the maya file to render
cmds.file(args.inputrig, o=True, iv=True, force=True)

### set up directory to store the rendered image
cmds.workspace( directory = args.directoryname )
cmds.workspace( fileRule = ['images', args.directoryname] )

### Set the time frame number you want to render
### Here we render the 10th frame, so start and end numbers are same
cmds.setAttr('defaultRenderGlobals.startFrame',10)
cmds.setAttr('defaultRenderGlobals.endFrame',10)

### render using the built-in camera 'fergcam_mery'
### saved image will have 256 x 256 dimensions
name = cmds.render('fergcam_mery',x=256,y=256)

### playblast option
#cmds.renderSettings(cam='fergcam_mery')
#cmds.playblast(f='mymovie',format='image',st=1,et=30,wh=[256,256],v=False,fo=True,os=True)