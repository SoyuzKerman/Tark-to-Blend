import bpy

# Function to merge duplicate data
# https://gist.github.com/MichaelGatesDev/0d3f075c5512bec9faa9be9ed033ff39

# remove duplicate materials
def Remove_Duped_Materials():
    print("Removing duplicate materials")
    mats = bpy.data.materials
    for mat in mats:
        (original, _, ext) = mat.name.rpartition(".")
        
        if ext.isnumeric() and mats.find(original) != -1:
            print("%s -> %s" %(mat.name, original))
            
            mat.user_remap(mats[original])
            mats.remove(mat)
    print("Done")

    return None


# remove duplicate textures
def Remove_Duped_Textures():
    print("Removing duplicate textures")
    mats = bpy.data.materials
    for mat in mats:
        if mat.node_tree:
            for n in mat.node_tree.nodes:
                if n.type == 'TEX_IMAGE':
                    if n.image is None:
                        print(mat.name,'has an image node with no image')
                    elif n.image.name[-3:].isdigit():
                        name = n.image.name[:-4]
                        exists = False
                        for img in bpy.data.images:
                            if img.name in name:
                                exists = True
                        if exists:
                            old_name = n.image.name
                            n.image = bpy.data.images[name]
                            print("%s -> %s" %(old_name, n.image.name))
                        else:
                            n.image.name = name
    print("Done")

    return None

# Modified from https://github.com/asoftbird/NodeDeduper/tree/main
def Remove_Duped_NG():
    print("Removing duplicate node groups")
    node_groups = bpy.data.node_groups
    for group in node_groups:
        unduped_name, *_ = group.name.rpartition(".")
        if unduped_name in node_groups and unduped_name != group.name:
            original_size = len(group.nodes)
            dupe_size = len(node_groups[unduped_name].nodes)
    
            if original_size != dupe_size:
                print(f"Length of {group.name} does not match {node_groups[unduped_name].name}! Skipping remap")
            else:
                group.user_remap(node_groups[unduped_name])
                print(f"Remapped {group.name} to {node_groups[unduped_name].name}!")

    else:
        group.name = unduped_name
    
    for group in node_groups:
        if group.use_fake_user == False and group.users == 0:
            print(f"Removed group {group.name}")
            node_groups.remove(group)
    
    print("Done")

    return None


def start() :
    Remove_Duped_Materials()
    Remove_Duped_Textures()
    Remove_Duped_NG()
    bpy.ops.outliner.orphans_purge()
    return None