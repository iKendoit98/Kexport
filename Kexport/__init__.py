bl_info = {
    "name" : "Kexport",
    "author" : "Ikruz",
    "descrtion" : "Batch export as Fbx",
    "blender" : (2, 80, 0),
    "version" : (0, 3, 2, 3),
    "location" : "Kexport panel",
    "warning" : "",
    "category" : "Import-Export"
}

import bpy
from bpy.props import *

from . bex_panel import *
from . bex_op import *
from . bex_folder_op import *

bpy.types.Scene.export_folder = StringProperty(name="Export folder", 
               subtype="DIR_PATH", 
               description="Directory to export the fbx files into")

bpy.types.Scene.center_transform = BoolProperty(name="Center transform",
                default=True,
                description="Set the pivot point of the object to the center")

bpy.types.Scene.apply_transform = BoolProperty(name="Apply transform",
                default=True,
                description="Applies scale and transform (Experimental)")

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


# Create an extra export button
def add_export_button(self, context):
    if context.region.alignment != 'RIGHT':
        layout = self.layout
        row = layout.row(align=True)

        self.layout.operator(
        BatEx_OT_Operator.bl_idname,
        text="Export",
        icon='PLUGIN')

    

classes = ( BatEx_PT_Panel, BatEx_OT_Operator, BatEx_OT_OpenFolder )



def register():
    bpy.utils.register_class(BatEx_PT_Panel)
    bpy.utils.register_class(BatEx_OT_Operator)
    bpy.utils.register_class(BatEx_OT_OpenFolder)
    # append the extra button to the top bar
    bpy.types.TOPBAR_HT_upper_bar.append(add_export_button)

def unregister():
    # clean up
    bpy.types.TOPBAR_HT_upper_bar.remove(add_export_button)
    bpy.utils.unregister_class(BatEx_PT_Panel)
    bpy.utils.unregister_class(BatEx_OT_Operator)
    bpy.utils.unregister_class(BatEx_OT_OpenFolder)
    



if __name__ == "__main__":
    register()
