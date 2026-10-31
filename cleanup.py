import bpy

def start(Cleanup_Toggle) :

    Objects = bpy.data.objects

    if Cleanup_Toggle :

        print("Starting Cleanup")

        Empty_List = []

        # Find empties and scale the root
        for obj in Objects :

            if obj.parent == None :
            # The only object that does not have a parent
            # is the root object that must be scaled
                obj.scale = (1,1,1)
            # For some reason it's imported with 0.01 scale

            if obj.type == "EMPTY" :

                if obj.animation_data == None :
                    # Avoid deleting empties that contain animations
                    # (for characters)
                    Empty_List.append(obj.name)
                
                #print(obj.name)

        #print(Empty_List)

        # Clear parents
        bpy.ops.object.select_all(action = "SELECT")
        bpy.ops.object.parent_clear(type='CLEAR_KEEP_TRANSFORM')

        # Delete all empties
        bpy.ops.object.select_all(action='DESELECT')

        for empty in Empty_List :
            bpy.data.objects[empty].select_set(True)

        bpy.ops.object.delete(use_global=False)

        print("Cleanup done")

    else :
        for obj in Objects :
            if obj.parent == None :
                obj.scale = (1,1,1)
        print("Scene scaled, no cleanup")


def rig():
    for Obj in bpy.data.objects :
        if Obj.type != 'MESH': continue
        Mod = Obj.modifiers
        
        if len(Mod) > 0 :
            # Find the modifier (0 by default)
            Armature_Mod = Mod[0]
            
            if Armature_Mod.type != 'ARMATURE': continue
            
            # Get name of new rig
            Current_Rig_Name = Armature_Mod.object.name
            New_Rig_Name = "RIG-" + Current_Rig_Name
            
            # Assign new rig to all objects
            Armature_Mod.object = bpy.data.objects[New_Rig_Name]
        
            # From https://extensions.blender.org/add-ons/rigi-all/
            # Fix Vertex Group naming for Rigify.
            armature = Armature_Mod.object
            for group in Obj.vertex_groups:
                if not armature.data.bones.get('DEF-' + group.name): continue
                group.name = 'DEF-' + group.name
            
            # Parent all objects to the rig
            Obj.parent = bpy.data.objects[New_Rig_Name]