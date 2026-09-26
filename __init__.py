bl_info = {
    "name": "Tark to Blend",
    "author": "Soyuz Kerman",
    "version": (1,0,0),
    "blender": (5, 2, 0),
    "location": "3D Viewport > Sidebar > Tark to Blend",
    "description": "Scene cleanup and material setup for Escape from Tarkov levels imported with Assetstudio",
    "category": "Materials",
    "doc_url" : "https://github.com/SoyuzKerman/Tark-to-Blend"
}


import bpy
import time
import os

from . import assignmat, cleanup, nodes, tarkdata


class UI_Settings(bpy.types.PropertyGroup) :

    Clean_Scene : bpy.props.BoolProperty(
        name="Clean Scene",
        description="Removes parenting and delete empties",
        #icon = "EMPTY_DATA",
        default = False
        )

    Save_CSV : bpy.props.BoolProperty(
        name="Save CSV",
        description="Saves a CSV in the Textures folder, containing data about the materials",
        #icon = "CURRENT_FILE",
        default = False
        )

    Tex_Dir_Path : bpy.props.StringProperty(
        name = "",
        description="Choose the folder containing the textures",
        default="Path here",
        maxlen=1024,
        subtype='DIR_PATH' # FILE_PATH
        )

class UI_Panel(bpy.types.Panel) :
    bl_space_type = "VIEW_3D"   # 3D Viewport
    bl_region_type = "UI"       # Sidebar
    bl_label = "Tark to Blend"  # Panel name
    bl_category = "Tark to Blend" # Sidebar name
    
    def draw_header(self, context) :
        self.layout.label(text="", icon='MATERIAL_DATA')
    
    def draw(self, context) :
        """Define layout"""
        layout = self.layout
        scene = context.scene
        panel = scene.Custom_Panel

        
        
        box0 = self.layout.box()
        
        row0 = box0.row()
        row0.label(text="Optional parameters :")
        
        row1 = box0.row()
        row1.prop(panel, "Clean_Scene", text="Clean Scene", icon = "EMPTY_DATA")

        row2 = box0.row()
        row2.prop(panel, "Save_CSV", text="Save CSV", icon = "CURRENT_FILE")
        
        
        box1 = self.layout.box()
        
        row3 = box1.row()
        row3.label(text="Texture folder :")
        
        row4 = box1.row()
        row4.prop(panel, "Tex_Dir_Path")
        
        
        box2 = self.layout.box()
        
        row5 = box2.row()
        row5.operator("ttb.main", text="Start process", icon="PLAY")

        warningrow = box2.row()
        warningrow.alert = True
        warningrow.label(text="Blender may freeze. Do not touch", icon="FREEZE")
        # form
       
class OT_Main(bpy.types.Operator) :
    bl_idname = "ttb.main" # having "." in the name is mandatory
    bl_label = "Main Operator"
    
    def execute(self, context) :
        scene = context.scene
        panel = scene.Custom_Panel

        MAKE_CSV = panel.Save_CSV
        TEX_PATH = panel.Tex_Dir_Path

        if not os.path.exists(os.path.dirname(TEX_PATH)) :
            raise SyntaxError("Texture folder does not exist.")
        
        Time_0 = time.time()

        cleanup.start(panel.Clean_Scene)

        
        NODE_DELETE_LIST, DGN_TYPE_LIST, ATLAS_EXCEPTIONS, TRANSPARENT_NAMES, OBJ_TO_DELETE, EMISSIVE_TYPE_LIST = tarkdata.load()

        print("Creating Shader node groups")
        NG_EFT_Normal = nodes.NG_Normal(node_name = "EFT_Normal_Fix")
        NG_EFT_Opaque = nodes.NG_Shader(node_name = "EFT_Shader_DGN")
        NG_EFT_Emissive = nodes.NG_Shader_Em(node_name = "EFT_Shader_Emissive")
        NG_EFT_Transparent = nodes.NG_Shader_Hair(node_name = "EFT_Shader_Hair")
        NG_EFT_Puddle = nodes.NG_Shader_Puddle(node_name = "EFT_Puddle")
        print("Node groups created")

        assignmat.start(NODE_DELETE_LIST, DGN_TYPE_LIST, ATLAS_EXCEPTIONS, TRANSPARENT_NAMES, OBJ_TO_DELETE, EMISSIVE_TYPE_LIST,
                       NG_EFT_Normal, NG_EFT_Opaque, NG_EFT_Emissive, NG_EFT_Transparent, NG_EFT_Puddle,MAKE_CSV, TEX_PATH)

        Time_Final_s = round(time.time()-Time_0,6)
        print(f"Execution time : {Time_Final_s} s")

        return {'FINISHED'} 


Class_List = [OT_Main, UI_Settings, UI_Panel]


def register() :
    for cls in Class_List :
        bpy.utils.register_class(cls)
    bpy.types.Scene.Custom_Panel = bpy.props.PointerProperty(type = UI_Settings)


def unregister() :
    for cls in Class_List :
        bpy.utils.unregister_class(cls)
    del bpy.types.Scene.Custom_Panel


if __name__ == "__main__" :
    register()


