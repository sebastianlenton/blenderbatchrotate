#script to automate Blender to create a set of stills rotating (these are later to be converted into a .gif)
#by Sebastian Lenton

#IMPORTANT
#re processed .blend file:
#the input .blend must have been saved in Object mode

#there must be one camera only, or else the script will fail. This camera can be angled as you like
#(a previous version of the script deleted and re-added the camera, but I think you need flxibility re camera placement)

#there must only be one mesh (eg the imported obj)

#there must be zero or one lamps in the initial .blend file- a lamp is added automatically (so all renders can have uniform lighting)

import bpy
import mathutils
import sys
import ntpath

#params for anim
framesInAnim = 32.0

#params for resolution
xLength = 500
yLength = 500

#get any command line args (http://blender.stackexchange.com/questions/6817/how-to-pass-command-line-arguments-to-a-blender-python-script)
argv = sys.argv
argv = argv[argv.index("--") + 1:]  # get all args after "--"

#set input/output
inputPath = argv[0]
filename = ntpath.basename( inputPath )
outputPath = argv[1]

#open the file 
bpy.ops.wm.open_mainfile(filepath=argv[0])

#select lamp (if there's a lamp present)
for ob in bpy.context.scene.objects:
	ob.select = ob.type == 'LAMP'

#delete the lamp present
bpy.ops.object.delete(use_global=False)

#the opened .blend must be in object mode for this to work, but it keeps failing for some reason
#bpy.ops.object.mode_set(mode='OBJECT')

#add new lamp
bpy.ops.object.lamp_add(type='POINT', view_align=False, location=(0.0, -2.0, 1.1), rotation=(1.5708, 0.0, 0.0))

#brighten up the lamp
newLamp = bpy.data.objects['Point']
newLamp.data.energy = 5.0

bpy.ops.object.select_all(action='DESELECT')

#delete the camera
for ob in bpy.context.scene.objects:
	ob.select = ob.type == 'CAMERA'

bpy.ops.object.delete(use_global=False)

#select all meshes (ideally we'd only want there to be one mesh there)
for mesh in bpy.context.scene.objects:
	mesh.select = mesh.type == 'MESH'

#set initial Z rotation to 0
mesh.rotation_euler[2] = 0

#animation - create keyframes
bpy.context.scene.frame_end = framesInAnim
bpy.context.scene.frame_current = 0
mesh.keyframe_insert(data_path="rotation_euler", frame=0.0, index=2)
bpy.context.scene.frame_current = framesInAnim
mesh.rotation_euler[2] = 6.28319
mesh.keyframe_insert(data_path="rotation_euler", frame=framesInAnim, index=2)

#set interpolation of graph points to linear (to remove easing)
kf = mesh.animation_data.action.fcurves[0].keyframe_points[0]
kf.interpolation = 'LINEAR'

bpy.ops.object.select_all(action='DESELECT')

#add new camera
bpy.ops.object.camera_add(view_align=False, enter_editmode=False, location=(0.0, -6.50764, 0.0), rotation=(1.570797, 0.0, 0.0))

#make camera the active camera (what this is actually doing is grabbing any camera it can find I think? But fingers crossed there will only ever be one camera)
bpy.context.scene.camera = bpy.data.objects['Camera']
bpy.context.object.data.type = 'ORTHO'
bpy.context.object.data.ortho_scale = 7.31429

#set renderpath
#will save as ../filename/filename0001.png and so on
bpy.context.scene.render.filepath = outputPath + "/" + filename + "/" + filename

#render settings
bpy.context.scene.render.resolution_percentage = 100
bpy.context.scene.render.resolution_x = xLength
bpy.context.scene.render.resolution_y = yLength

#render
bpy.ops.render.render(animation=True)
