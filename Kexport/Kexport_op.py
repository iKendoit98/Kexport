import bpy
import os

from . kex_export import *



class Kexport_OT_Operator(bpy.types.Operator):
    bl_idname = "object.kexport_ot_operator"
    bl_label = "Batch Export"
    bl_description = "Export Selected objects as fbx"
    bl_options = {"REGISTER"}



    def execute(self, context):
        
        k_export = Kex_Export(context)
        k_export.export_asset()        

        self.report({'INFO'}, "Exported to " + context.scene.export_folder)
        return {"FINISHED"}


class Kexport_LOW_OT_Operator(bpy.types.Operator):
    bl_idname = "object.kexport_low_ot_operator"
    bl_label = "Low Poly Export"
    bl_description = "Export Selected objects as low Poly fbx"
    bl_options = {"REGISTER"}



    def execute(self, context):
        
        k_export = Kex_Export(context)
        k_export.export_lowpoly()
        self.report({'INFO'}, "Exported to " + context.scene.export_folder)
        return {"FINISHED"}



class Kexport_HIGH_OT_Operator(bpy.types.Operator):
    bl_idname = "object.kexport_high_ot_operator"
    bl_label = "High Poly Export"
    bl_description = "Export Selected objects as high Poly fbx"
    bl_options = {"REGISTER"}




    def execute(self, context):
        
        k_export = Kex_Export(context)
        k_export.export_highpoly()
        self.report({'INFO'}, "Exported to " + context.scene.export_folder)
        return {"FINISHED"}