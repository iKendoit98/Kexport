import bpy
import os

from bpy.props import *

# Desired Backup destination folder
directory = r"C:\Users\Ian\Documents\PersonalProjects\Blender_Addons\BL_Kexport\test_directory"


bpy.ops.object.mode_set(mode='OBJECT')

view_layer = bpy.context.view_layer
obj_active = bpy.context.active_object



selection = bpy.context.selected_objects

#iterate over selected objects
for obj in selection:
    # Make sure its selected
    obj.select_set(True)
    
    # Save objs old location    
    loc = obj_active.location.copy()
    
    # Move objects to origin
    obj_active.location = (0,0,0)
    print("moved to origin")

    # Store objects Name
    name = bpy.path.clean_name(obj.name)
    # Store objects name and join to full filepath
    fn = os.path.join(directory, name)

    # Export objs with properties
    bpy.ops.export_scene.fbx(
        filepath=fn + ".fbx", 
        use_selection=True,
        mesh_smooth_type='EDGE',
        path_mode='ABSOLUTE')

    # Unselect Objects
    obj.select_set(False)
    print ('Exported:', fn)

    # Return objs location to previous location
    obj_active.location = loc
    print ('Moved back to original loc')



