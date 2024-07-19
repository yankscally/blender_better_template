import bpy
# TODO better name

class ExamplePanel(bpy.types.Panel):
    bl_label = "Object Panel"
    bl_idname = "VIEW3D_PT_object_panel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Map'

    def draw(self, context):
            layout = self.layout

            # context.scene.example_props is loaded in __init.py__!! 
            props = context.scene.example_props
            obj = context.object
            
            row = layout.row()
            row.prop(props, "my_int")
            row = layout.row()
            row.prop(props, "my_float")
            row = layout.row()
            row.prop(props, "my_enum")
            row = layout.row()
            row.prop(props, "my_string")

class ExampleProperties(bpy.types.PropertyGroup):

    bpy.types.Scene.my_int = bpy.props.IntProperty(
        name="int",
        description="integer",
        default=1,
        min=0,
        max=1024,
        step=1) #type: ignore
   
    bpy.types.Scene.my_float = bpy.props.FloatProperty(
        name="float",
        description="float",
        default=1.0,
        min=0.0625,
        max=1024.0,
        step=0.25,
        precision=2) #type: ignore
    
    bpy.types.Scene.my_enum = bpy.props.EnumProperty(
        name="enum",
        description="enumerator",
        items=[
            ("1", "first_option", "description"),
            ("2", "second_option", "description"),
            ("3", "third_option", "description"),
               ],
        default="1") #type: ignore

    bpy.types.Scene.my_string = bpy.props.StringProperty(
        name="string",
        description="words and stuff",
        default="type here..") #type: ignore

