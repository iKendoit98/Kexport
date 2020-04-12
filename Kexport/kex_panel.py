import bpy
from bpy.types import Panel

class Kexport_Panel(bpy.types.Panel):
    bl_label = "FBX Export"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Kexport"

    def draw(self, context):
        layout = self.layout
        scene = context.scene

        row = layout.row()
        row.label(text="Assets folder:")


        row = layout.row()
        row.prop(context.scene, 'assets_folder', text='')

        row = layout.row()
        row.label(text="Bakes folder:")

        row = layout.row()
        row.prop(context.scene, 'bakes_folder', text='')



        row_smooth = layout.row()
        col_smooth_lbl = row_smooth.column()
        col_smooth_lbl.label(text="Smoothing:")

        col_smooth = row_smooth.column()
        col_smooth.alignment = 'EXPAND'
        col_smooth.prop(context.scene, "export_smoothing", text="")
        
        row = layout.row()
        row.operator('object.kexport_ot_operator', text='Export Game Asset')

        # Low poly export button
        row = layout.row()
        colA = row.column()
        colA.operator('object.kexport_low_ot_operator', text='Export Low Poly')
        
        # High poly export button
        colB = row.column()
        colB.operator('object.kexport_high_ot_operator', text='Export High Poly')