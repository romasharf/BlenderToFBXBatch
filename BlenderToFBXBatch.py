#Before running this script you need Python 3.10(?) and Blendr 2.93 to be installed on your system
#Also you have to place all the Bledner files that you want to export to fbx to D:\fbx_input (if you don't have such a directory, you have to create it)
#And create D:\fbx_output directory
#Otherwise script won't work
#Of course you can replace "D" hard drive letter to any hard drive letter that you want ("G" letter for example)

import subprocess
import os
import fnmatch

MyDir = 'D:/fbx_input' #Directory to be processed by the script

StuffList = os.listdir(MyDir) #All items in the directory
BlendList = fnmatch.filter(StuffList, '*.blend') #Only Blender files in the directory

CMDPath = "c:\windows\system32\cmd.exe" #Path to Windows cmd.exe
BlenderPath = "C:/Program Files/Blender Foundation/Blender 2.93/blender.exe" #Path to Blender

#Main cycle. Here we're just getting each .blend file in our directory and running the "Blender_export_script.py" script
for MyFile in BlendList:
    P = subprocess.run([CMDPath, "/C", BlenderPath, "-b", MyDir+'/'+MyFile,'-P', 'D:\scipting_projects\Blender_export_script.py'])
