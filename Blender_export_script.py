import bpy

#Finding current file name
RawFilename = bpy.path.basename(bpy.data.filepath)

#Cutting out an extension
Filename = RawFilename.replace('blend','')

#Setting path to export our stuff as fbx
ExportPath = 'D:\\fbx_output\\'+Filename+'fbx'

#Exporting (we assume that our library have only mesh objects)
bpy.ops.export_scene.fbx(filepath=ExportPath, use_selection=False, global_scale=.2, object_types={'MESH'})

#Closing blender
bpy.ops.wm.quit_blender()
