import bpy
import os



class KEX_Export:

    def __init__(self, context):
        self.__context = context
        self.__assets_folder = context.scene.assets_folder
        self.__mesh_type = context.scene.mesh_type
        self.__apply_transform = context.scene.apply_transform


    # Export objs
    def export_asset(self):

        bpy.ops.object.mode_set(mode='OBJECT')
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
            objname = bpy.path.clean_name(obj.name)
            name = self.__mesh_type + objname
            # Store objects name and join to full filepath
            fn = os.path.join(self.__assets_folder, name)

            # Export objs with properties
            bpy.ops.export_scene.fbx(
                filepath=fn + ".fbx",
                filter_glob="*.fbx", 
                use_selection=True,
                use_armature_deform_only=True,
                bake_space_transform=self.__apply_transform,
                mesh_smooth_type=self.__context.scene.export_smoothing,
                add_leaf_bones=False,
                path_mode='ABSOLUTE')

            # Unselect Objects
            obj.select_set(False)
            print ('Exported:', fn)

            # Return objs location to previous location
            obj_active.location = loc
            obj.select_set(True)
            print ('Moved back to original loc')
 