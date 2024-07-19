import bpy

# panel and operators load automagically from __init__ 

class OtherPanel(bpy.types.Panel):
    bl_label = "Map"
    bl_idname = "VIEW3D_PT_map_panel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Example'
   
    def draw(self, context):
        layout = self.layout
        obj = context.object
    
        scene = context.scene
        
        row = layout.row()
        row.label(text="another panel for other stuff")
        row = layout.row()


