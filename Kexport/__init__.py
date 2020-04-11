
bl_info = {
    "name" : "Kexporter",
    "author" : "iKendoit",
    "description" : "Batch Exporter focused on game exports",
    "blender" : (2, 80, 2),
    "version" : (0, 0, 1),
    "location" : "Kexport panel",
    "category" : "Import-Export"
}
     



import bpy

from bpy.types import Panel

from . Kexport_op import *
from . kex_export import *


class Kexport_Panel(bpy.types.Panel):
    bl_label = "FBX Export"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Kexport"

    def draw(self, context):
        layout = self.layout
        scene = context.scene

        row = layout.row()
        row.label(text="Export folder:")
        




classes = (Kex_Export, Kexport_OT_Operator, Kexport_Panel)

register, unregister = bpy.utils.register_classes_factory(classes)

if __name__ == "__main__":
    register()