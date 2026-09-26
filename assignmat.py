# Author : Soyuz Kerman
# https://soyuzkerman.net/
# Version : 2026-09-17
# Tested on Blender 5.2.0,
# with Factory and trader scenes

# HOW TO USE :
# 1. Import the scene file (fbx) in Blender
# 2. Select the root object, scale it from 0.010 to 1, move it if you need to
# 3. [OPTIONAL] Select all objects (A), clear parent and keep transformation (Alt + P), then delete the EMPTY objects
# 4. Load the script in the Blender text editor
# 5. Change the texture folder path TEX_PATH
#    and switch MAKE_CSV to True if you want the material log.
# 6. Execute the script.
# 7. Manually check for missing textures and missed transparent materials.
# 8. File > Clean Up > Purge unused data.

import bpy
import csv
import numpy as np
import time
import os

#%% FUNCTIONS

def Scene_Cleanup(OBJ_TO_DELETE) :
    # Deletes useless objects based on the OBJ_TO_DELETE list
    # OBJ_TO_DELETE : list of str, manually built

    Objects = bpy.data.objects

    for Obj in Objects :

        if any(x in Obj.name for x in OBJ_TO_DELETE) :
            Objects.remove(Obj)

    return None


def Instantiate_Group(Nodes, Custom_Group):
    # Adds a node group to the tree
    # Nodes : bpy.data.materials.node_tree.nodes
    # https://blender.stackexchange.com/questions/150874/python-add-existing-nodegroup-to-material
    Group = Nodes.new(type='ShaderNodeGroup')
    Group.node_tree = Custom_Group
    return Group


def Node_Tree_Mapping(Nodes) :
    # Identifies and returns the nodes used in the material setup
    # Nodes = Mat.node_tree.nodes

    Has_Normal = False
    Has_Diffuse = False
    D_Texture = None
    N_Texture = None

    BSDF_Node = Nodes["Principled BSDF"]

    Has_Diffuse = BSDF_Node.inputs["Base Color"].is_linked
    Has_Normal = BSDF_Node.inputs["Normal"].is_linked

    if Has_Diffuse and Has_Normal :
        # D texture is always the first, if N exists its node name ends with .001
        D_Texture = Nodes["Image Texture"]
        N_Texture = Nodes["Image Texture.001"]

    elif Has_Diffuse and not Has_Normal :
        D_Texture = Nodes["Image Texture"]

    elif not Has_Diffuse and Has_Normal :
        N_Texture = Nodes["Image Texture"]

    return D_Texture, N_Texture, Has_Diffuse, Has_Normal


def Is_Shader_Transparent(Mat, Nodes, Has_Diffuse, Has_Normal, D_Texture, Atlas_Exceptions, TRANSPARENT_NAMES) :
    # Detects if the material is transparent
    # WARNING : based on my observations about the material setup and texture names.
    # It is impossible to flawlessly detect if a material must be transparent
    # with this setup.
    # Mat = bpy.types.Material
    # Nodes = Mat.node_tree.nodes
    # Has_Normal : bool (use NodeTree_Contains_Normal function)
    # Atlas_Exceptions : list of str

    if Has_Diffuse :
        Img_Name = D_Texture.image.name
        Img_W = D_Texture.image.size[0]
        Img_H = D_Texture.image.size[1]
        Is_Terrain_Texture = Img_W == 2048 and Img_H == 2048

        if any(x in Img_Name for x in TRANSPARENT_NAMES) :
        # Check if the image texture name contains keywords for tranparent objects
            return True
        
        if any(x in Mat.name for x in TRANSPARENT_NAMES) :
        # Check if the material name contains keywords for tranparent objects
            return True

        if any(x in Img_Name for x in ["grass", "Grass"]) and not Is_Terrain_Texture :
            # If the texture name contains "grass" and is not a 2048x2048 texture,
            # it is assumed to be transparent
            return True

        if Has_Normal : 
            if any(x in Img_Name for x in ["atlas","Atlas"]) :
                if Img_Name in Atlas_Exceptions :
                    return False
                else :
                    return True

        return False

    else :
        # If the diffuse texture does not exist,
        # it does not really matter if it's transparent or not
        return False


def Get_Texture_Suffix(Texture_Name) :
    # Gets the "_diff.png" part of the texture name
    # Texture_Name : str, use with bpy.types.Node.image.name

    # Because of inconsistent naming,
    # I manually added these exceptions
    if "[Albedo]" in Texture_Name :
        return "[Albedo].png"
    if "[Glossy].png" in Texture_Name :
        return "[Glossy].png"
    if "[Normal]" in Texture_Name :
        return "[Normal].png"
 
    return "_" + Texture_Name.split("_")[-1]


def Get_G_Texture_Name(Texture_Name, Suffix) :
    # Texture_Name : str
    # Suffix : str, for example "_gloss.png" from DGN_TYPE_LIST
    
    Texture_Name_Split = Texture_Name.split("_")
    Texture_Name_Split[-1] = Suffix.split("_")[-1] # split is used to avoid using the "_" from DGN_TYPE_LIST elements
    Texture_Name_2 = "_".join(Texture_Name_Split)
    
    return Texture_Name_2


def Load_G_Texture(Texture_Name, TEX_PATH, DGN_Index, DGN_TYPE_LIST) :
    # Texture_Name : str
    # DGN_Index : int, location of the Texture_Name suffix in DGN_TYPE_LIST
    # DGN_TYPE_LIST : nparray of the naming conventions

    G_Texture_Name = Get_G_Texture_Name(Texture_Name, DGN_TYPE_LIST[DGN_Index,1])
    G_Texture_Path = rf"{TEX_PATH}\{G_Texture_Name}"
    G_Texture_Image = bpy.data.images.load(G_Texture_Path)

    return G_Texture_Image


def Add_G_Texture(Nodes, G_Texture_Image) :
    # Adds an "Image Texture" node to the material node tree
    # Nodes : Mat.node_tree.nodes
    # G_Texture_Image : bpy.types.Image
    G_Texture = Nodes.new(type="ShaderNodeTexImage")
    G_Texture.image = G_Texture_Image
    G_Texture.location = (-470, -300)
    return G_Texture

def Is_DGN_Type(Has_Diffuse, D_Texture, DGN_TYPE_LIST) :
    # Detects if the textures follow the "D-G-N" naming convention
    # Has_Diffuse : bool
    # D_Texture : bpy.types.Node
    # DGN_TYPE_LIST : nparray

    if Has_Diffuse :
        return any(x in D_Texture.image.name for x in DGN_TYPE_LIST[:,0])
    else : 
        return False

def Find_G_Texture(Nodes, Has_Diffuse, Has_Normal, D_Texture, N_Texture, Is_DGN, TEX_PATH, DGN_TYPE_LIST) :
    # Algorithm to find and return the "glossy" texture
    # It's slow and stupid, you have to go through all of the possibilies
    # because there are a lot of mistakes and inconsistencies in the file names.
    # Nodes : Mat.node_tree.nodes
    # Has_Diffuse, Has_Normal : bool
    # D_Texture, N_Texture : bpy.types.Node
    # TEX_PATH : str, path of the texture folder
    # DGN_TYPE_LIST : nparray

    if Is_DGN :
        DGN_Index = int(np.where(DGN_TYPE_LIST[:,0] == Get_Texture_Suffix(D_Texture.image.name))[0][0])
        # Finds the index of the suffix in DGN_TYPE_LIST

        try :
            # Search for the missing texture based on the normal texture first,
            # because several materials sharing the same normal/gloss
            # can have different diffuse textures

            if Has_Normal :
                G_Texture_Image = Load_G_Texture(N_Texture.image.name, TEX_PATH, DGN_Index, DGN_TYPE_LIST)
            else :
                G_Texture_Image = Load_G_Texture(D_Texture.image.name, TEX_PATH, DGN_Index, DGN_TYPE_LIST)
            G_Texture = Add_G_Texture(Nodes, G_Texture_Image)
            Has_Glossy = True
            # If successful, the function ends here
            return G_Texture, Has_Glossy

        except RuntimeError :
            # If the texture does not exist -> RuntimeError
            # Search based on the diffuse texture name instead
            try :
                
                G_Texture_Image = Load_G_Texture(D_Texture.image.name, TEX_PATH, DGN_Index, DGN_TYPE_LIST)
                G_Texture = Add_G_Texture(Nodes, G_Texture_Image)
                Has_Glossy = True
                # If successful, the function ends here
                return G_Texture, Has_Glossy

            except RuntimeError :
                # If the texture does not exist -> RuntimeError
                # We search all of the possible naming conventions
                for j in range(len(DGN_TYPE_LIST)) :
                    try :
                        G_Texture_Image = Load_G_Texture(D_Texture.image.name, TEX_PATH, j, DGN_TYPE_LIST)
                        G_Texture = Add_G_Texture(Nodes, G_Texture_Image)
                        # If successful, the function ends here
                        Has_Glossy = True
                        return G_Texture, Has_Glossy

                    except RuntimeError :
                        pass

                if Has_Normal :
                    for j in range(len(DGN_TYPE_LIST)) :
                        try :
                            G_Texture_Image = Load_G_Texture(N_Texture.image.name, TEX_PATH, j, DGN_TYPE_LIST)
                            G_Texture = Add_G_Texture(Nodes, G_Texture_Image)
                            # If successful, the function ends here
                            Has_Glossy = True
                            return G_Texture, Has_Glossy

                        except RuntimeError :
                            pass
                    
                Has_Glossy = False
                return None, Has_Glossy

    else :
        Has_Glossy = False
        return None, Has_Glossy


def Build_Material_Setup(Mat, Nodes, Links, Has_Diffuse, Has_Normal, Has_Glossy, Is_Transparent,
                        Has_Emissive, D_Texture, N_Texture, G_Texture, E_Texture,
                        NG_EFT_Opaque, NG_EFT_Transparent, NG_EFT_Emissive, NG_EFT_Normal,
                        NODE_DELETE_LIST) :
    # Adds nodes to the material node tree and connects them.
    # Nodes : Mat.node_tree.nodes
    # Links : Mat.node_tree.links
    # Has_Diffuse, Has_Normal, Is_Transparent : bool
    # D_Texture, G_Texture, N_Texture : bpy.data.images
    # NG_EFT_* : bpy.types.ShaderNodeCustomGroup, custom shade node group
    # NODE_DELETE_LIST: list of str

    Mat.surface_render_method = "BLENDED"

    if not Has_Diffuse :
        # The texture is broken/incomplete, use a bright red BSDF
        Nodes["Principled BSDF"].inputs["Base Color"].default_value = (1.0, 0.0, 0.0, 1)

    else :
        # Delete unused nodes
        for node_name in NODE_DELETE_LIST :
            try :
                node =  Nodes[node_name]
                Nodes.remove(node)
            except KeyError :
                # Exception if the node does not exist
                # for materials without normal map
                pass

        # Add custom shader node
        if Has_Emissive :
            Shader_Group = Instantiate_Group(Nodes, NG_EFT_Emissive)
            Links.new(E_Texture.outputs["Color"],Shader_Group.inputs["E"])
            Shader_Group.inputs["Emission Strength"].default_value = 1
        
        elif Is_Transparent :
            Shader_Group = Instantiate_Group(Nodes, NG_EFT_Transparent)
        
        else : 
            Shader_Group = Instantiate_Group(Nodes, NG_EFT_Opaque)
        Shader_Group.location.x = -50
        Shader_Group.location.y = 200

        # Connect the nodes
        if Has_Glossy :
            Links.new(G_Texture.outputs["Color"],Shader_Group.inputs["G"])

        if Has_Diffuse :
            Links.new(D_Texture.outputs["Color"],Shader_Group.inputs["D"])
            Links.new(D_Texture.outputs["Alpha"],Shader_Group.inputs["D alpha"])

        if Has_Normal :
            Normal_Group = Instantiate_Group(Nodes, NG_EFT_Normal)
            Links.new(N_Texture.outputs["Color"],Normal_Group.inputs[0])
            Links.new(N_Texture.outputs["Alpha"],Normal_Group.inputs[1])
            Links.new(Shader_Group.inputs["N Converted"],Normal_Group.outputs[0])
            Normal_Group.location = (-220,-10)
        else :
            #Shader_Group.inputs["N Strength"].default_value = 0
            pass

        Output_Node = Nodes["Material Output"]
        Links.new(Output_Node.inputs["Surface"],Shader_Group.outputs["BSDF"])

    return None


def Add_To_Log(Mat, Mat_Log_List, Texture_Log_List, Transparent_Log_List, Emissive_Log_List,
               Has_Diffuse, Has_Normal, Has_Glossy, Has_Emissive,
               Is_Transparent, D_Texture, N_Texture, G_Texture, E_Texture) :
    
    Mat_Log_List.append(Mat.name)
    Transparent_Log_List.append(str(Is_Transparent))

    Texture_Names = []
    if Has_Diffuse :
        Texture_Names.append(D_Texture.image.name)
    else : 
        Texture_Names.append("None")

    if Has_Glossy :
        Texture_Names.append(G_Texture.image.name)
    else : 
        Texture_Names.append("None")    

    if Has_Normal :
        Texture_Names.append(N_Texture.image.name)
    else : 
        Texture_Names.append("None")

    if Has_Emissive :
        Texture_Names.append(E_Texture.image.name)
    else : 
        Texture_Names.append("None")        

    Texture_Log_List.append(Texture_Names)

    return None


def Save_Log(TEX_PATH, Mat_Log_List, Transparent_Log_List,
            Texture_Log_List, Emissive_Log_List) :
    # Saves information about materials in a CSV file
    # TEX_PATH : str, output folder
    # Mat_Log_List : list of str, contains the material names
    # Transparent_Log_List : list of bool, contains info about if a material is transparent
    # Texture_Log_List : list of lists containing three str, contains the texture names
    # Emissive_Log_List : list of bool, contains info about if a material is emissive

    File_Name = "EFT_Material_Setup.csv"
    File_Path = rf"{TEX_PATH}\{File_Name}"

    Data = [["Material name", "is Transparent", "is Emissive", "Diffuse", "Glossy", "Normal", "Emissive"]]

    for m in range(len(Mat_Log_List)) :
        Data.append([Mat_Log_List[m], Transparent_Log_List[m],
                    Emissive_Log_List[m], Texture_Log_List[m][0],
                    Texture_Log_List[m][1], Texture_Log_List[m][2],
                    Texture_Log_List[m][3]])

    with open(File_Path, 'w', newline='') as Csvfile:
        Writer = csv.writer(Csvfile, delimiter = ";")
        # ";" allows the columns to be displayed correctly when opened in MS Excel.
        Writer.writerows(Data)

    return None


def Find_Emissive(TEX_PATH, EMISSIVE_TYPE_LIST) :
    # Scans the texture folder for Emissive textures
    # TEX_PATH : str, path of texture folder
    # EMISSIVE_TYPE_LIST : list of str, contains the possible types names for emissive textures
    
    Files = os.listdir(TEX_PATH)
    Emissive_Texture_Names = []

    for File_Name in Files :
        if any(x in File_Name for x in EMISSIVE_TYPE_LIST) :
            Emissive_Texture_Names.append(File_Name)

    return Emissive_Texture_Names


def Is_Shader_Emissive(Nodes, TEX_PATH, D_Texture, Is_DGN, Emissive_Texture_Names, Emissive_Log_List) :
    # Finds if a texture is emissive and adds the node to the node_tree
    # TEX_PATH : str, path of texture folder
    # D_Texture : bpy.types.Node, diffuse texture node
    # Emissive_Texture_Names : list of str, contains the file name of emissive textures
    # Emissive_Log_List : list of bool, for the log

    if Is_DGN :
        # If the shader is not of DGN Type :
        # - It will be incorrectly flagged as emissive
        # - It will not be emissive anyway

        if "[Albedo]" in D_Texture.image.name :
            # Specific case where split("_") will not work
            # None of these textures are emissive
            Has_Emissive = False
            return None, Has_Emissive

        # Get texture name without DGN suffix
        Texture_Name_Split = D_Texture.image.name.split("_")[:-1]
        D_Texture_Name = "_".join(Texture_Name_Split)

        # Compare with emissive list
        for E_Texture_Name in Emissive_Texture_Names :
            if E_Texture_Name.startswith(D_Texture_Name) :

                # Load texture
                E_Texture_Path = rf"{TEX_PATH}\{E_Texture_Name}"
                E_Texture_Image = bpy.data.images.load(E_Texture_Path)
                
                # Add node
                E_Texture = Nodes.new(type="ShaderNodeTexImage")
                E_Texture.image = E_Texture_Image
                E_Texture.location = (-470, -600)

                Has_Emissive = True
                Emissive_Log_List.append(str(Has_Emissive))
                return E_Texture, Has_Emissive

    Has_Emissive = False
    Emissive_Log_List.append(str(Has_Emissive))
    return None, Has_Emissive

#%% MAIN

def start(NODE_DELETE_LIST, DGN_TYPE_LIST, ATLAS_EXCEPTIONS, TRANSPARENT_NAMES, OBJ_TO_DELETE, EMISSIVE_TYPE_LIST,
          NG_EFT_Normal, NG_EFT_Opaque, NG_EFT_Emissive, NG_EFT_Transparent, MAKE_CSV, TEX_PATH) :

    print("------ EFT MATERIAL SETUP START ------")

    # Lists to print in the log
    Mat_Log_List = []
    Transparent_Log_List = []
    Emissive_Log_List = []
    Texture_Log_List = []

    print("Deleting useless objects")
    Scene_Cleanup(OBJ_TO_DELETE)
    print("Deletion complete")


    print("--- Starting material setup ---")

    Emissive_Texture_Names = Find_Emissive(TEX_PATH, EMISSIVE_TYPE_LIST)
    print(Emissive_Texture_Names)

    for Mat in bpy.data.materials :
    #for Mat in [bpy.data.materials["material name"]]: # for debug

        print(Mat.name)

        Links = Mat.node_tree.links
        Nodes = Mat.node_tree.nodes

        D_Texture, N_Texture, Has_Diffuse, Has_Normal = Node_Tree_Mapping(Nodes)
        Is_DGN = Is_DGN_Type(Has_Diffuse, D_Texture, DGN_TYPE_LIST)

        Is_Transparent = Is_Shader_Transparent(Mat, Nodes, Has_Diffuse, Has_Normal, D_Texture, ATLAS_EXCEPTIONS, TRANSPARENT_NAMES)

        E_Texture, Has_Emissive = Is_Shader_Emissive(Nodes, TEX_PATH, D_Texture, Is_DGN, Emissive_Texture_Names, Emissive_Log_List)

        G_Texture, Has_Glossy = Find_G_Texture(Nodes, Has_Diffuse, Has_Normal, D_Texture, N_Texture, Is_DGN, TEX_PATH, DGN_TYPE_LIST)

        Build_Material_Setup(Mat, Nodes, Links, Has_Diffuse, Has_Normal, Has_Glossy, Is_Transparent,
                            Has_Emissive, D_Texture, N_Texture, G_Texture, E_Texture,
                            NG_EFT_Opaque, NG_EFT_Transparent, NG_EFT_Emissive, NG_EFT_Normal,
                            NODE_DELETE_LIST)

        Add_To_Log(Mat, Mat_Log_List, Texture_Log_List, Transparent_Log_List,
                Emissive_Log_List, Has_Diffuse, Has_Normal, Has_Glossy,
                Has_Emissive, Is_Transparent, D_Texture, N_Texture, G_Texture, E_Texture)

    print("--- Material setup complete ---")
    print("Check the scene manually to fix missing textures and transparent objects if needed")

    if MAKE_CSV :
        Save_Log(TEX_PATH, Mat_Log_List, Transparent_Log_List,
                Texture_Log_List, Emissive_Log_List)
        print(f"Log saved at {TEX_PATH}")


    print("------ EFT MATERIAL SETUP DONE ------")

    return None