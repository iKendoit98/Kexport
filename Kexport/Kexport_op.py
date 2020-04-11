import bpy
import os

from . kex_export import *




class Kexport_OT_Operator(bpy.types.Operator):
    bl_idname = "object.kexport_ot_operator"
    bl_label = "Batch Export"
    bl_description = "Export Selected objects as fbx"
    bl_options = {"REGISTER"}

    @classmethod
    def poll(cls, context):
        return True

    def execute(self, context):
        
        k_export = Kex_Export(context)
        k_export.export_obj()
        k_export.append_export_topbar(context)
        
        #self.report({'INFO'}, "Exported to " + context.scene.export_folder)
        return {"FINISHED"}




