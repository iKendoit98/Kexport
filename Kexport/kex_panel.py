import bpy
from bpy.types import Panel

class KEX_PT_Panel(bpy.types.Panel):
    bl_label = "Game Exports"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Kexport"

    def draw(self, context):
        layout = self.layout
        scene = context.scene

        # Assets folder
        row = layout.row(align=True)
        row.label(text="Assets folder:")
        # # Asset folder selection
        row.prop(context.scene, 'assets_folder', text='')


        # label
        row_smooth = layout.row()
        col_smooth_lbl = row_smooth.column()
        col_smooth_lbl.label(text="Smoothing:")
        # property
        col_smooth = row_smooth.column()
        col_smooth.alignment = 'EXPAND'
        col_smooth.prop(context.scene, "export_smoothing", text="")


         # label
        row_smooth = layout.row()
        col_smooth_lbl = row_smooth.column()
        col_smooth_lbl.label(text="Mesh Type:")
         # property
        col_smooth = row_smooth.column()
        col_smooth.alignment = 'EXPAND'
        col_smooth.prop(context.scene, "mesh_type", text="")

        row = layout.row()
        row.prop(context.scene, "apply_transform", text="Apply transform")

        
        # Export Asset button
        row = layout.row(align=True)
        row.operator('object.kexport_ot_operator', text='Asset Export')
        row = layout.row()
        row.operator('object.kexport_ot_openfolder', text='Open export folder')
        