import bpy

def start(Cleanup_Toggle) :

    Objects = bpy.data.objects

    if Cleanup_Toggle :

        print("Starting Cleanup")

        Empty_List = []

        # Find empties and scale the root
        for obj in Objects :
            
            if obj.type == "EMPTY" :
                Empty_List.append(obj.name)
                
                if obj.parent == None :
                # The only object that does not have a parent
                # is the root object that must be scaled
                    obj.scale = (1,1,1)
                # For some reason it's imported with 0.01 scale
                    
                print(obj.name)

        print(Empty_List)

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