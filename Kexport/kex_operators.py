import bpy
import os

from . kex_export import *



class KEX_OT_Operator(bpy.types.Operator):
    bl_idname = "object.kexport_ot_operator"
    bl_label = "Batch Export"
    bl_description = "Export Selected objects as fbx"
    bl_options = {"REGISTER"}



    def execute(self, context):
        
        k_export = KEX_Export(context)
        k_export.export_asset(0)        

        #self.report({'INFO'}, "Exported to " + context.scene.export_folder)
        return {"FINISHED"}

class KEX_BAKES_OT_Operator(bpy.types.Operator):
    bl_idname = "object.kexport_bakes_ot_operator"
    bl_label = "Export to selected bakes folder"
    bl_description = "Export Selected objects to bakes folder"
    bl_options = {"REGISTER"}



    def execute(self, context):
        
        k_export = KEX_Export(context)
        k_export.export_asset(1)
        print("Exported to:    Bakes Folder")
        #self.report({'INFO'}, "Exported to " + context.scene.export_folder)
        return {"FINISHED"}