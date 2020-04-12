import bpy
import os



class Kex_Export:

    def __init__(self, context):
        self.__context = context
        self.__assets_folder = context.scene.assets_folder
        self.__bakes_folder = context.scene.bakes_folder


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
            name = "SM_" + objname
            # Store objects name and join to full filepath
            fn = os.path.join(self.__assets_folder, name)

            # Export objs with properties
            bpy.ops.export_scene.fbx(
                filepath=fn + ".fbx", 
                use_selection=True,
                mesh_smooth_type=self.__context.scene.export_smoothing,
                path_mode='ABSOLUTE')

            # Unselect Objects
            obj.select_set(False)
            print ('Exported:', fn)

            # Return objs location to previous location
            obj_active.location = loc
            print ('Moved back to original loc')

    def export_lowpoly(self):


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
            basename = bpy.path.clean_name(obj.name)
            name = basename + "_low"
            # Store objects name and join to full filepath
            fn = os.path.join(self.__bakes_folder, name)

            # Export objs with properties
            bpy.ops.export_scene.fbx(
                filepath=fn + ".fbx", 
                use_selection=True,
                mesh_smooth_type=self.__context.scene.export_smoothing,
                path_mode='ABSOLUTE')

            # Unselect Objects
            obj.select_set(False)
            print ('Exported:', fn)

            # Return objs location to previous location
            obj_active.location = loc
            print ('Moved back to original loc')


       # Export objs
    
    
    
    
    def export_highpoly(self):

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
            basename = bpy.path.clean_name(obj.name)
            name = basename + "_high"
            # Store objects name and join to full filepath
            fn = os.path.join(self.__bakes_folder, name)

            # Export objs with properties
            bpy.ops.export_scene.fbx(
                filepath=fn + ".fbx", 
                use_selection=True,
                mesh_smooth_type=self.__context.scene.export_smoothing,
                path_mode='ABSOLUTE')

            # Unselect Objects
            obj.select_set(False)
            print ('Exported:', fn)

            # Return objs location to previous location
            obj_active.location = loc
            print ('Moved back to original loc')        