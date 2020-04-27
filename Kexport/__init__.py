
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

from bpy.props import *
from bpy.types import Panel

from . kex_operators import *
from . kex_export import *
from . kex_panel import *





# Assets export folder destination property
bpy.types.Scene.assets_folder = StringProperty(name="assets folder", 
               subtype="DIR_PATH", 
               description="Directory to export the fbx files into")
# Bakes export folder destination property
bpy.types.Scene.bakes_folder = StringProperty(name="bakes folder", 
               subtype="DIR_PATH", 
               description="Directory to export the fbx files into")


bpy.types.Scene.mesh_type = EnumProperty(
    name="Mesh Type",
    description="Defines skeletal or static mesh type",
    items=(
        ('SM_','Static Mesh','Static Mesh', 0),
        ('SK_', 'Skeletal Mesh', 'Skeletal Mesh', 1),
        ),
    default='SM_'
    )
# smoothing type property
bpy.types.Scene.export_smoothing = EnumProperty(
    name="Smoothing",
    description="Defines the export smoothing information",
    items=(
        ('EDGE', 'Edge', 'Write edge smoothing',0),
        ('FACE', 'Face', 'Write face smoothing',1),
        ('OFF', 'Normals Only', 'Write normals only',2)
        ),
    default='OFF'
    )

def append_export_topbar(self, context):
    if context.region.alignment != 'RIGHT':
        layout = self.layout
        row = layout.row(align=True)

        # Place the export operator here
        self.layout.operator(
        KEX_OT_Operator.bl_idname,
        text="UExport",
        icon='FILE_TICK') 


def register():
    bpy.utils.register_class(KEX_OT_Operator)
    bpy.utils.register_class(KEX_BAKES_OT_Operator)
    bpy.utils.register_class(KEX_PT_Panel)

    bpy.types.TOPBAR_HT_upper_bar.append(append_export_topbar)

def unregister():
    bpy.utils.unregister_class(KEX_OT_Operator)
    bpy.utils.unregister_class(KEX_BAKES_OT_Operator)
    bpy.utils.unregister_class(KEX_PT_Panel)

    bpy.types.TOPBAR_HT_upper_bar.remove(append_export_topbar)


if __name__ == "__main__":
    register()