import bpy
import os


from . Kexport_op import *

class Kex_Export:
    # Export objs

    
    def __init__(self, context):
        self.__context = context
        self.__export_folder = context.scene.export_folder
        self.__center_transform = context.scene.center_transform
        self.__apply_transform = context.scene.apply_transform
        self.__export_objects = context.selected_objects

    def export_obj(self):
        
        
        # Desired Backup destination folder
        directory = r"C:\Users\Ian\Documents\PersonalProjects\Blender_Addons\BL_Kexport\test_directory"
        
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

    def append_export_topbar(self, context):
        if context.region.alignment != 'RIGHT':
            layout = self.layout
            row = layout.row(align=True)

            # Place the export operator here
            self.layout.operator(
            Kexport_OT_Operator.bl_idname,
            text="UExport",
            icon='FILE_TICK') 