import bpy
import os

from . kex_export import *
from bpy.types import Operator


class KEX_OT_ExportAsset(bpy.types.Operator):
    bl_idname = "object.kexport_ot_operator"
    bl_label = "Batch Export"
    bl_description = "Export Selected objects as fbx"
    bl_options = {"REGISTER"}



    def execute(self, context):
        
        k_export = KEX_Export(context)
        k_export.export_asset()        

        #self.report({'INFO'}, "Exported to " + context.scene.export_folder)
        return {"FINISHED"}



class KEX_OT_OpenFolder(bpy.types.Operator):
  
  bl_idname = "object.kexport_ot_openfolder"
  bl_label = "Open Export Folder"
  bl_description = "Open the export folder" 
  bl_options = {'REGISTER'}

  def execute(self, context):
    bpy.ops.wm.path_open(filepath=context.scene.assets_folder)
    return {'FINISHED'}