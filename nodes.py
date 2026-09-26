import bpy

# Node group to convert AssetStudio normal maps
def NG_Normal(node_name = "AS_Normal_Fix"):

    """Initialize AS_Normal_Fix node group"""
    as_normal_fix_1 = bpy.data.node_groups.new(type = 'ShaderNodeTree', name = node_name)

    as_normal_fix_1.color_tag = 'NONE'
    as_normal_fix_1.description = ""
    as_normal_fix_1.default_group_node_width = 140
    # as_normal_fix_1 interface

    # Socket Color
    color_socket = as_normal_fix_1.interface.new_socket(name="Fixed Normal", in_out='OUTPUT', socket_type='NodeSocketColor')
    color_socket.default_value = (0.0, 0.0, 0.0, 0.0)
    color_socket.attribute_domain = 'POINT'
    color_socket.default_input = 'VALUE'
    color_socket.structure_type = 'AUTO'

    # Socket Color
    color_socket_1 = as_normal_fix_1.interface.new_socket(name="N Color", in_out='INPUT', socket_type='NodeSocketColor')
    color_socket_1.default_value = (1.0, 0.5, 0.5, 1.0)
    color_socket_1.attribute_domain = 'POINT'
    color_socket_1.default_input = 'VALUE'
    color_socket_1.structure_type = 'AUTO'

    # Socket Alpha
    alpha_socket = as_normal_fix_1.interface.new_socket(name="N Alpha", in_out='INPUT', socket_type='NodeSocketFloat')
    alpha_socket.default_value = 0.5
    alpha_socket.min_value = -10000.0
    alpha_socket.max_value = 10000.0
    alpha_socket.subtype = 'NONE'
    alpha_socket.attribute_domain = 'POINT'
    alpha_socket.default_input = 'VALUE'
    alpha_socket.structure_type = 'AUTO'

    # Initialize as_normal_fix_1 nodes

    # Node Group Input
    group_input = as_normal_fix_1.nodes.new("NodeGroupInput")
    group_input.name = "Group Input"
    group_input.show_options = True

    # Node Separate XYZ
    separate_xyz = as_normal_fix_1.nodes.new("ShaderNodeSeparateXYZ")
    separate_xyz.name = "Separate XYZ"
    separate_xyz.show_options = True

    # Node Group Output
    group_output = as_normal_fix_1.nodes.new("NodeGroupOutput")
    group_output.name = "Group Output"
    group_output.show_options = True
    group_output.is_active_output = True

    # Node Reroute.001
    reroute_001 = as_normal_fix_1.nodes.new("NodeReroute")
    reroute_001.name = "Reroute.001"
    reroute_001.show_options = True
    reroute_001.socket_idname = "NodeSocketFloat"
    # Node Reroute.002
    reroute_002 = as_normal_fix_1.nodes.new("NodeReroute")
    reroute_002.name = "Reroute.002"
    reroute_002.show_options = True
    reroute_002.socket_idname = "NodeSocketFloat"
    # Node Reroute
    reroute = as_normal_fix_1.nodes.new("NodeReroute")
    reroute.name = "Reroute"
    reroute.show_options = True
    reroute.socket_idname = "NodeSocketFloat"
    # Node Combine Color.001
    combine_color_001 = as_normal_fix_1.nodes.new("ShaderNodeCombineColor")
    combine_color_001.name = "Combine Color.001"
    combine_color_001.show_options = True
    combine_color_001.mode = 'RGB'

    # Node Math.005
    math_005 = as_normal_fix_1.nodes.new("ShaderNodeMath")
    math_005.name = "Math.005"
    math_005.show_options = True
    math_005.operation = 'MULTIPLY'
    math_005.use_clamp = False
    # Value_001
    math_005.inputs[1].default_value = 2.0

    # Node Math.006
    math_006 = as_normal_fix_1.nodes.new("ShaderNodeMath")
    math_006.name = "Math.006"
    math_006.show_options = True
    math_006.operation = 'MULTIPLY'
    math_006.use_clamp = False
    # Value_001
    math_006.inputs[1].default_value = 2.0

    # Node Math.003
    math_003 = as_normal_fix_1.nodes.new("ShaderNodeMath")
    math_003.name = "Math.003"
    math_003.show_options = True
    math_003.operation = 'SUBTRACT'
    math_003.use_clamp = False
    # Value_001
    math_003.inputs[1].default_value = 1.0

    # Node Math.007
    math_007 = as_normal_fix_1.nodes.new("ShaderNodeMath")
    math_007.name = "Math.007"
    math_007.show_options = True
    math_007.operation = 'SUBTRACT'
    math_007.use_clamp = False
    # Value_001
    math_007.inputs[1].default_value = 1.0

    # Node Math
    math = as_normal_fix_1.nodes.new("ShaderNodeMath")
    math.name = "Math"
    math.show_options = True
    math.operation = 'MULTIPLY'
    math.use_clamp = False

    # Node Math.001
    math_001 = as_normal_fix_1.nodes.new("ShaderNodeMath")
    math_001.name = "Math.001"
    math_001.show_options = True
    math_001.operation = 'MULTIPLY'
    math_001.use_clamp = False

    # Node Math.002
    math_002 = as_normal_fix_1.nodes.new("ShaderNodeMath")
    math_002.name = "Math.002"
    math_002.show_options = True
    math_002.operation = 'ADD'
    math_002.use_clamp = False

    # Node Math.008
    math_008 = as_normal_fix_1.nodes.new("ShaderNodeMath")
    math_008.name = "Math.008"
    math_008.show_options = True
    math_008.operation = 'SUBTRACT'
    math_008.use_clamp = False
    # Value
    math_008.inputs[0].default_value = 1.0

    # Node Math.004
    math_004 = as_normal_fix_1.nodes.new("ShaderNodeMath")
    math_004.name = "Math.004"
    math_004.show_options = True
    math_004.operation = 'SQRT'
    math_004.use_clamp = False

    # Node Math.009
    math_009 = as_normal_fix_1.nodes.new("ShaderNodeMath")
    math_009.name = "Math.009"
    math_009.show_options = True
    math_009.operation = 'MULTIPLY'
    math_009.use_clamp = False
    # Value_001
    math_009.inputs[1].default_value = 0.5

    # Node Math.010
    math_010 = as_normal_fix_1.nodes.new("ShaderNodeMath")
    math_010.name = "Math.010"
    math_010.show_options = True
    math_010.operation = 'ADD'
    math_010.use_clamp = False
    # Value_001
    math_010.inputs[1].default_value = 0.5

    # Set locations
    as_normal_fix_1.nodes["Group Input"].location = (-1675.9642333984375, 0.0)
    as_normal_fix_1.nodes["Separate XYZ"].location = (-1394.9678955078125, 33.669395446777344)
    as_normal_fix_1.nodes["Group Output"].location = (176.73095703125, 152.7402801513672)
    as_normal_fix_1.nodes["Reroute.001"].location = (-1228.66552734375, 45.286739349365234)
    as_normal_fix_1.nodes["Reroute.002"].location = (-1394.755859375, 61.8431282043457)
    as_normal_fix_1.nodes["Reroute"].location = (-1228.66552734375, 61.8431282043457)
    as_normal_fix_1.nodes["Combine Color.001"].location = (19.791641235351562, 152.7402801513672)
    as_normal_fix_1.nodes["Math.005"].location = (-1226.7369384765625, 37.841278076171875)
    as_normal_fix_1.nodes["Math.006"].location = (-1226.7369384765625, -122.1976318359375)
    as_normal_fix_1.nodes["Math.003"].location = (-1072.4964599609375, 37.841278076171875)
    as_normal_fix_1.nodes["Math.007"].location = (-1072.4964599609375, -122.1976318359375)
    as_normal_fix_1.nodes["Math"].location = (-914.3770751953125, 37.841278076171875)
    as_normal_fix_1.nodes["Math.001"].location = (-914.3770751953125, -122.1976318359375)
    as_normal_fix_1.nodes["Math.002"].location = (-744.45703125, 34.59152603149414)
    as_normal_fix_1.nodes["Math.008"].location = (-586.5128173828125, 34.59152603149414)
    as_normal_fix_1.nodes["Math.004"].location = (-433.9521484375, 34.59152603149414)
    as_normal_fix_1.nodes["Math.009"].location = (-285.23828125, 34.59152603149414)
    as_normal_fix_1.nodes["Math.010"].location = (-139.0560302734375, 34.59152603149414)

    # Set dimensions
    as_normal_fix_1.nodes["Group Input"].width  = 140.0
    as_normal_fix_1.nodes["Group Input"].height = 100.0

    as_normal_fix_1.nodes["Separate XYZ"].width  = 140.0
    as_normal_fix_1.nodes["Separate XYZ"].height = 100.0

    as_normal_fix_1.nodes["Group Output"].width  = 140.0
    as_normal_fix_1.nodes["Group Output"].height = 100.0

    as_normal_fix_1.nodes["Reroute.001"].width  = 16.0
    as_normal_fix_1.nodes["Reroute.001"].height = 100.0

    as_normal_fix_1.nodes["Reroute.002"].width  = 16.0
    as_normal_fix_1.nodes["Reroute.002"].height = 100.0

    as_normal_fix_1.nodes["Reroute"].width  = 16.0
    as_normal_fix_1.nodes["Reroute"].height = 100.0

    as_normal_fix_1.nodes["Combine Color.001"].width  = 140.0
    as_normal_fix_1.nodes["Combine Color.001"].height = 100.0

    as_normal_fix_1.nodes["Math.005"].width  = 140.0
    as_normal_fix_1.nodes["Math.005"].height = 100.0

    as_normal_fix_1.nodes["Math.006"].width  = 140.0
    as_normal_fix_1.nodes["Math.006"].height = 100.0

    as_normal_fix_1.nodes["Math.003"].width  = 140.0
    as_normal_fix_1.nodes["Math.003"].height = 100.0

    as_normal_fix_1.nodes["Math.007"].width  = 140.0
    as_normal_fix_1.nodes["Math.007"].height = 100.0

    as_normal_fix_1.nodes["Math"].width  = 140.0
    as_normal_fix_1.nodes["Math"].height = 100.0

    as_normal_fix_1.nodes["Math.001"].width  = 140.0
    as_normal_fix_1.nodes["Math.001"].height = 100.0

    as_normal_fix_1.nodes["Math.002"].width  = 140.0
    as_normal_fix_1.nodes["Math.002"].height = 100.0

    as_normal_fix_1.nodes["Math.008"].width  = 140.0
    as_normal_fix_1.nodes["Math.008"].height = 100.0

    as_normal_fix_1.nodes["Math.004"].width  = 140.0
    as_normal_fix_1.nodes["Math.004"].height = 100.0

    as_normal_fix_1.nodes["Math.009"].width  = 140.0
    as_normal_fix_1.nodes["Math.009"].height = 100.0

    as_normal_fix_1.nodes["Math.010"].width  = 140.0
    as_normal_fix_1.nodes["Math.010"].height = 100.0


    # Initialize as_normal_fix_1 links

    # math.Value -> math_002.Value
    as_normal_fix_1.links.new(
        as_normal_fix_1.nodes["Math"].outputs[0],
        as_normal_fix_1.nodes["Math.002"].inputs[0]
    )
    # math_001.Value -> math_002.Value
    as_normal_fix_1.links.new(
        as_normal_fix_1.nodes["Math.001"].outputs[0],
        as_normal_fix_1.nodes["Math.002"].inputs[1]
    )
    # separate_xyz.Y -> math_005.Value
    as_normal_fix_1.links.new(
        as_normal_fix_1.nodes["Separate XYZ"].outputs[1],
        as_normal_fix_1.nodes["Math.005"].inputs[0]
    )
    # math_005.Value -> math_003.Value
    as_normal_fix_1.links.new(
        as_normal_fix_1.nodes["Math.005"].outputs[0],
        as_normal_fix_1.nodes["Math.003"].inputs[0]
    )
    # math_006.Value -> math_007.Value
    as_normal_fix_1.links.new(
        as_normal_fix_1.nodes["Math.006"].outputs[0],
        as_normal_fix_1.nodes["Math.007"].inputs[0]
    )
    # math_002.Value -> math_008.Value
    as_normal_fix_1.links.new(
        as_normal_fix_1.nodes["Math.002"].outputs[0],
        as_normal_fix_1.nodes["Math.008"].inputs[1]
    )
    # math_008.Value -> math_004.Value
    as_normal_fix_1.links.new(
        as_normal_fix_1.nodes["Math.008"].outputs[0],
        as_normal_fix_1.nodes["Math.004"].inputs[0]
    )
    # math_003.Value -> math.Value
    as_normal_fix_1.links.new(
        as_normal_fix_1.nodes["Math.003"].outputs[0],
        as_normal_fix_1.nodes["Math"].inputs[0]
    )
    # math_003.Value -> math.Value
    as_normal_fix_1.links.new(
        as_normal_fix_1.nodes["Math.003"].outputs[0],
        as_normal_fix_1.nodes["Math"].inputs[1]
    )
    # math_007.Value -> math_001.Value
    as_normal_fix_1.links.new(
        as_normal_fix_1.nodes["Math.007"].outputs[0],
        as_normal_fix_1.nodes["Math.001"].inputs[0]
    )
    # math_007.Value -> math_001.Value
    as_normal_fix_1.links.new(
        as_normal_fix_1.nodes["Math.007"].outputs[0],
        as_normal_fix_1.nodes["Math.001"].inputs[1]
    )
    # math_004.Value -> math_009.Value
    as_normal_fix_1.links.new(
        as_normal_fix_1.nodes["Math.004"].outputs[0],
        as_normal_fix_1.nodes["Math.009"].inputs[0]
    )
    # math_009.Value -> math_010.Value
    as_normal_fix_1.links.new(
        as_normal_fix_1.nodes["Math.009"].outputs[0],
        as_normal_fix_1.nodes["Math.010"].inputs[0]
    )
    # math_010.Value -> combine_color_001.Blue
    as_normal_fix_1.links.new(
        as_normal_fix_1.nodes["Math.010"].outputs[0],
        as_normal_fix_1.nodes["Combine Color.001"].inputs[2]
    )
    # group_input.Color -> separate_xyz.Vector
    as_normal_fix_1.links.new(
        as_normal_fix_1.nodes["Group Input"].outputs[0],
        as_normal_fix_1.nodes["Separate XYZ"].inputs[0]
    )
    # combine_color_001.Color -> group_output.Color
    as_normal_fix_1.links.new(
        as_normal_fix_1.nodes["Combine Color.001"].outputs[0],
        as_normal_fix_1.nodes["Group Output"].inputs[0]
    )
    # group_input.Alpha -> math_006.Value
    as_normal_fix_1.links.new(
        as_normal_fix_1.nodes["Group Input"].outputs[1],
        as_normal_fix_1.nodes["Math.006"].inputs[0]
    )
    # reroute.Output -> combine_color_001.Red
    as_normal_fix_1.links.new(
        as_normal_fix_1.nodes["Reroute"].outputs[0],
        as_normal_fix_1.nodes["Combine Color.001"].inputs[0]
    )
    # reroute_002.Output -> reroute.Input
    as_normal_fix_1.links.new(
        as_normal_fix_1.nodes["Reroute.002"].outputs[0],
        as_normal_fix_1.nodes["Reroute"].inputs[0]
    )
    # reroute_001.Output -> combine_color_001.Green
    as_normal_fix_1.links.new(
        as_normal_fix_1.nodes["Reroute.001"].outputs[0],
        as_normal_fix_1.nodes["Combine Color.001"].inputs[1]
    )
    # separate_xyz.Y -> reroute_001.Input
    as_normal_fix_1.links.new(
        as_normal_fix_1.nodes["Separate XYZ"].outputs[1],
        as_normal_fix_1.nodes["Reroute.001"].inputs[0]
    )
    # group_input.Alpha -> reroute_002.Input
    as_normal_fix_1.links.new(
        as_normal_fix_1.nodes["Group Input"].outputs[1],
        as_normal_fix_1.nodes["Reroute.002"].inputs[0]
    )

    return as_normal_fix_1

# Standard (opaque and non-emissive) shader group
def NG_Shader(node_name = "EFT_Shader_DGN"):
    """Initialize EFT_Shader_DGN node group"""
    eft_shader_dgn_1 = bpy.data.node_groups.new(type = 'ShaderNodeTree', name = node_name)

    eft_shader_dgn_1.color_tag = 'NONE'
    eft_shader_dgn_1.description = ""
    eft_shader_dgn_1.default_group_node_width = 140
    # eft_shader_dgn_1 interface

    # Socket BSDF
    bsdf_socket = eft_shader_dgn_1.interface.new_socket(name="BSDF", in_out='OUTPUT', socket_type='NodeSocketShader')
    bsdf_socket.attribute_domain = 'POINT'
    bsdf_socket.description = "EFT Shader"
    bsdf_socket.default_input = 'VALUE'
    bsdf_socket.structure_type = 'AUTO'

    # Socket D
    d_socket = eft_shader_dgn_1.interface.new_socket(name="D", in_out='INPUT', socket_type='NodeSocketColor')
    d_socket.default_value = (0.800000011920929, 0.800000011920929, 0.800000011920929, 1.0)
    d_socket.attribute_domain = 'POINT'
    d_socket.description = "Diffuse"
    d_socket.default_input = 'VALUE'
    d_socket.structure_type = 'AUTO'

    # Socket D alpha
    d_alpha_socket = eft_shader_dgn_1.interface.new_socket(name="D alpha", in_out='INPUT', socket_type='NodeSocketFloat')
    d_alpha_socket.default_value = 0.0
    d_alpha_socket.min_value = 0.0
    d_alpha_socket.max_value = 1.0
    d_alpha_socket.subtype = 'FACTOR'
    d_alpha_socket.attribute_domain = 'POINT'
    d_alpha_socket.description = "Metallic or Alpha"
    d_alpha_socket.default_input = 'VALUE'
    d_alpha_socket.structure_type = 'AUTO'

    # Socket G
    g_socket = eft_shader_dgn_1.interface.new_socket(name="G", in_out='INPUT', socket_type='NodeSocketColor')
    g_socket.default_value = (0.0, 0.0, 0.0, 1.0)
    g_socket.attribute_domain = 'POINT'
    g_socket.description = "Glossiness"
    g_socket.default_input = 'VALUE'
    g_socket.structure_type = 'AUTO'

    # Socket N Converted
    n_converted_socket = eft_shader_dgn_1.interface.new_socket(name="N Converted", in_out='INPUT', socket_type='NodeSocketColor')
    n_converted_socket.default_value = (0.5, 0.5, 1.0, 1.0)
    n_converted_socket.attribute_domain = 'POINT'
    n_converted_socket.description = "Converted Normal map input"
    n_converted_socket.default_input = 'VALUE'
    n_converted_socket.structure_type = 'AUTO'

    # Initialize eft_shader_dgn_1 nodes

    # Node Principled BSDF.001
    principled_bsdf_001 = eft_shader_dgn_1.nodes.new("ShaderNodeBsdfPrincipled")
    principled_bsdf_001.name = "Principled BSDF.001"
    principled_bsdf_001.show_options = True
    principled_bsdf_001.distribution = 'MULTI_GGX'
    principled_bsdf_001.subsurface_method = 'RANDOM_WALK_LEGACY'
    principled_bsdf_001.panel_states[0].is_collapsed = True
    principled_bsdf_001.panel_states[1].is_collapsed = True
    principled_bsdf_001.panel_states[2].is_collapsed = True
    principled_bsdf_001.panel_states[3].is_collapsed = True
    principled_bsdf_001.panel_states[4].is_collapsed = True
    principled_bsdf_001.panel_states[5].is_collapsed = True
    principled_bsdf_001.panel_states[6].is_collapsed = True
    principled_bsdf_001.panel_states[7].is_collapsed = True
    # IOR
    principled_bsdf_001.inputs[3].default_value = 1.0
    # Alpha
    principled_bsdf_001.inputs[4].default_value = 1.0
    # Thin Wall
    principled_bsdf_001.inputs[5].default_value = False
    # Diffuse Roughness
    principled_bsdf_001.inputs[8].default_value = 0.0
    # Subsurface Weight
    principled_bsdf_001.inputs[9].default_value = 0.0
    # Subsurface Radius
    principled_bsdf_001.inputs[10].default_value = (1.0, 0.20000000298023224, 0.10000000149011612)
    # Subsurface Scale
    principled_bsdf_001.inputs[11].default_value = 0.05000000074505806
    # Subsurface Anisotropy
    principled_bsdf_001.inputs[13].default_value = 0.0
    # Specular IOR Level
    principled_bsdf_001.inputs[14].default_value = 0.5
    # Specular Tint
    principled_bsdf_001.inputs[15].default_value = (1.0, 1.0, 1.0, 1.0)
    # Anisotropic
    principled_bsdf_001.inputs[16].default_value = 0.0
    # Anisotropic Rotation
    principled_bsdf_001.inputs[17].default_value = 0.0
    # Tangent
    principled_bsdf_001.inputs[18].default_value = (0.0, 0.0, 0.0)
    # Transmission Weight
    principled_bsdf_001.inputs[19].default_value = 0.0
    # Coat Weight
    principled_bsdf_001.inputs[20].default_value = 0.0
    # Coat Roughness
    principled_bsdf_001.inputs[21].default_value = 0.029999999329447746
    # Coat IOR
    principled_bsdf_001.inputs[22].default_value = 1.5
    # Coat Tint
    principled_bsdf_001.inputs[23].default_value = (1.0, 1.0, 1.0, 1.0)
    # Coat Normal
    principled_bsdf_001.inputs[24].default_value = (0.0, 0.0, 0.0)
    # Sheen Weight
    principled_bsdf_001.inputs[25].default_value = 0.0
    # Sheen Roughness
    principled_bsdf_001.inputs[26].default_value = 0.5
    # Sheen Tint
    principled_bsdf_001.inputs[27].default_value = (1.0, 1.0, 1.0, 1.0)
    # Emission Color
    principled_bsdf_001.inputs[28].default_value = (1.0, 1.0, 1.0, 1.0)
    # Emission Strength
    principled_bsdf_001.inputs[29].default_value = 0.0
    # Thin Film Thickness
    principled_bsdf_001.inputs[30].default_value = 0.0
    # Thin Film IOR
    principled_bsdf_001.inputs[31].default_value = 1.3300000429153442

    # Node Invert Color
    invert_color = eft_shader_dgn_1.nodes.new("ShaderNodeInvert")
    invert_color.name = "Invert Color"
    invert_color.show_options = True
    # Fac
    invert_color.inputs[0].default_value = 1.0

    # Node Group Output
    group_output = eft_shader_dgn_1.nodes.new("NodeGroupOutput")
    group_output.name = "Group Output"
    group_output.show_options = True
    group_output.is_active_output = True

    # Node Group Input
    group_input = eft_shader_dgn_1.nodes.new("NodeGroupInput")
    group_input.name = "Group Input"
    group_input.show_options = True

    # Node Normal Map
    normal_map = eft_shader_dgn_1.nodes.new("ShaderNodeNormalMap")
    normal_map.name = "Normal Map"
    normal_map.show_options = True
    normal_map.base = 'DISPLACED'
    normal_map.convention = 'OPENGL'
    normal_map.space = 'TANGENT'
    normal_map.uv_map = ""
    # Strength
    normal_map.inputs[0].default_value = 1.0

    # Node Reroute
    reroute = eft_shader_dgn_1.nodes.new("NodeReroute")
    reroute.name = "Reroute"
    reroute.show_options = True
    reroute.socket_idname = "NodeSocketColor"
    # Node Reroute.001
    reroute_001 = eft_shader_dgn_1.nodes.new("NodeReroute")
    reroute_001.name = "Reroute.001"
    reroute_001.show_options = True
    reroute_001.socket_idname = "NodeSocketColor"
    # Node Reroute.002
    reroute_002 = eft_shader_dgn_1.nodes.new("NodeReroute")
    reroute_002.name = "Reroute.002"
    reroute_002.show_options = True
    reroute_002.socket_idname = "NodeSocketFloatFactor"
    # Node Reroute.003
    reroute_003 = eft_shader_dgn_1.nodes.new("NodeReroute")
    reroute_003.name = "Reroute.003"
    reroute_003.show_options = True
    reroute_003.socket_idname = "NodeSocketFloatFactor"
    # Set locations
    eft_shader_dgn_1.nodes["Principled BSDF.001"].location = (-92.92974853515625, 60.93362045288086)
    eft_shader_dgn_1.nodes["Invert Color"].location = (-292.92974853515625, -36.31060028076172)
    eft_shader_dgn_1.nodes["Group Output"].location = (197.07025146484375, 60.93362045288086)
    eft_shader_dgn_1.nodes["Group Input"].location = (-505.42974853515625, 13.52299690246582)
    eft_shader_dgn_1.nodes["Normal Map"].location = (-302.92974853515625, -178.97726440429688)
    eft_shader_dgn_1.nodes["Reroute"].location = (-302.92974853515625, 79.68939971923828)
    eft_shader_dgn_1.nodes["Reroute.001"].location = (-142.92974853515625, 79.68939971923828)
    eft_shader_dgn_1.nodes["Reroute.002"].location = (-302.92974853515625, 21.689401626586914)
    eft_shader_dgn_1.nodes["Reroute.003"].location = (-142.92974853515625, 21.689401626586914)

    # Set dimensions
    eft_shader_dgn_1.nodes["Principled BSDF.001"].width  = 240.0
    eft_shader_dgn_1.nodes["Principled BSDF.001"].height = 100.0

    eft_shader_dgn_1.nodes["Invert Color"].width  = 140.0
    eft_shader_dgn_1.nodes["Invert Color"].height = 100.0

    eft_shader_dgn_1.nodes["Group Output"].width  = 140.0
    eft_shader_dgn_1.nodes["Group Output"].height = 100.0

    eft_shader_dgn_1.nodes["Group Input"].width  = 140.0
    eft_shader_dgn_1.nodes["Group Input"].height = 100.0

    eft_shader_dgn_1.nodes["Normal Map"].width  = 160.0
    eft_shader_dgn_1.nodes["Normal Map"].height = 100.0

    eft_shader_dgn_1.nodes["Reroute"].width  = 14.5
    eft_shader_dgn_1.nodes["Reroute"].height = 100.0

    eft_shader_dgn_1.nodes["Reroute.001"].width  = 14.5
    eft_shader_dgn_1.nodes["Reroute.001"].height = 100.0

    eft_shader_dgn_1.nodes["Reroute.002"].width  = 14.5
    eft_shader_dgn_1.nodes["Reroute.002"].height = 100.0

    eft_shader_dgn_1.nodes["Reroute.003"].width  = 14.5
    eft_shader_dgn_1.nodes["Reroute.003"].height = 100.0


    # Initialize eft_shader_dgn_1 links

    # invert_color.Color -> principled_bsdf_001.Roughness
    eft_shader_dgn_1.links.new(
        eft_shader_dgn_1.nodes["Invert Color"].outputs[0],
        eft_shader_dgn_1.nodes["Principled BSDF.001"].inputs[2]
    )
    # principled_bsdf_001.BSDF -> group_output.BSDF
    eft_shader_dgn_1.links.new(
        eft_shader_dgn_1.nodes["Principled BSDF.001"].outputs[0],
        eft_shader_dgn_1.nodes["Group Output"].inputs[0]
    )
    # group_input.N Converted -> normal_map.Color
    eft_shader_dgn_1.links.new(
        eft_shader_dgn_1.nodes["Group Input"].outputs[3],
        eft_shader_dgn_1.nodes["Normal Map"].inputs[1]
    )
    # normal_map.Normal -> principled_bsdf_001.Normal
    eft_shader_dgn_1.links.new(
        eft_shader_dgn_1.nodes["Normal Map"].outputs[0],
        eft_shader_dgn_1.nodes["Principled BSDF.001"].inputs[6]
    )
    # group_input.G -> invert_color.Color
    eft_shader_dgn_1.links.new(
        eft_shader_dgn_1.nodes["Group Input"].outputs[2],
        eft_shader_dgn_1.nodes["Invert Color"].inputs[1]
    )
    # group_input.D -> reroute.Input
    eft_shader_dgn_1.links.new(
        eft_shader_dgn_1.nodes["Group Input"].outputs[0],
        eft_shader_dgn_1.nodes["Reroute"].inputs[0]
    )
    # group_input.D alpha -> reroute_002.Input
    eft_shader_dgn_1.links.new(
        eft_shader_dgn_1.nodes["Group Input"].outputs[1],
        eft_shader_dgn_1.nodes["Reroute.002"].inputs[0]
    )
    # reroute.Output -> reroute_001.Input
    eft_shader_dgn_1.links.new(
        eft_shader_dgn_1.nodes["Reroute"].outputs[0],
        eft_shader_dgn_1.nodes["Reroute.001"].inputs[0]
    )
    # reroute_002.Output -> reroute_003.Input
    eft_shader_dgn_1.links.new(
        eft_shader_dgn_1.nodes["Reroute.002"].outputs[0],
        eft_shader_dgn_1.nodes["Reroute.003"].inputs[0]
    )
    # reroute_001.Output -> principled_bsdf_001.Base Color
    eft_shader_dgn_1.links.new(
        eft_shader_dgn_1.nodes["Reroute.001"].outputs[0],
        eft_shader_dgn_1.nodes["Principled BSDF.001"].inputs[0]
    )
    # reroute_003.Output -> principled_bsdf_001.Metallic
    eft_shader_dgn_1.links.new(
        eft_shader_dgn_1.nodes["Reroute.003"].outputs[0],
        eft_shader_dgn_1.nodes["Principled BSDF.001"].inputs[1]
    )

    return eft_shader_dgn_1

# Emissive shader
def NG_Shader_Em(node_name = "EFT_Shader_Emissive"):
    """Initialize EFT_Shader_Emissive node group"""
    eft_shader_emissive_1 = bpy.data.node_groups.new(type = 'ShaderNodeTree', name = node_name)

    eft_shader_emissive_1.color_tag = 'NONE'
    eft_shader_emissive_1.description = ""
    eft_shader_emissive_1.default_group_node_width = 140
    # eft_shader_emissive_1 interface

    # Socket BSDF
    bsdf_socket = eft_shader_emissive_1.interface.new_socket(name="BSDF", in_out='OUTPUT', socket_type='NodeSocketShader')
    bsdf_socket.attribute_domain = 'POINT'
    bsdf_socket.description = "EFT Emissive Shader"
    bsdf_socket.default_input = 'VALUE'
    bsdf_socket.structure_type = 'AUTO'

    # Socket D
    d_socket = eft_shader_emissive_1.interface.new_socket(name="D", in_out='INPUT', socket_type='NodeSocketColor')
    d_socket.default_value = (0.800000011920929, 0.800000011920929, 0.800000011920929, 1.0)
    d_socket.attribute_domain = 'POINT'
    d_socket.description = "Diffuse"
    d_socket.default_input = 'VALUE'
    d_socket.structure_type = 'AUTO'

    # Socket D alpha
    d_alpha_socket = eft_shader_emissive_1.interface.new_socket(name="D alpha", in_out='INPUT', socket_type='NodeSocketFloat')
    d_alpha_socket.default_value = 0.0
    d_alpha_socket.min_value = 0.0
    d_alpha_socket.max_value = 1.0
    d_alpha_socket.subtype = 'FACTOR'
    d_alpha_socket.attribute_domain = 'POINT'
    d_alpha_socket.description = "Metallic or Alpha"
    d_alpha_socket.default_input = 'VALUE'
    d_alpha_socket.structure_type = 'AUTO'

    # Socket G
    g_socket = eft_shader_emissive_1.interface.new_socket(name="G", in_out='INPUT', socket_type='NodeSocketColor')
    g_socket.default_value = (0.0, 0.0, 0.0, 1.0)
    g_socket.attribute_domain = 'POINT'
    g_socket.description = "Glossiness"
    g_socket.default_input = 'VALUE'
    g_socket.structure_type = 'AUTO'

    # Socket N Converted
    n_converted_socket = eft_shader_emissive_1.interface.new_socket(name="N Converted", in_out='INPUT', socket_type='NodeSocketColor')
    n_converted_socket.default_value = (0.5, 0.5, 1.0, 1.0)
    n_converted_socket.attribute_domain = 'POINT'
    n_converted_socket.description = "Converted Normal map"
    n_converted_socket.default_input = 'VALUE'
    n_converted_socket.structure_type = 'AUTO'

    # Socket E
    e_socket = eft_shader_emissive_1.interface.new_socket(name="E", in_out='INPUT', socket_type='NodeSocketColor')
    e_socket.default_value = (1.0, 1.0, 1.0, 1.0)
    e_socket.attribute_domain = 'POINT'
    e_socket.default_input = 'VALUE'
    e_socket.structure_type = 'AUTO'

    # Socket Emission Strength
    emission_strength_socket = eft_shader_emissive_1.interface.new_socket(name="Emission Strength", in_out='INPUT', socket_type='NodeSocketFloat')
    emission_strength_socket.default_value = 0.0
    emission_strength_socket.min_value = 0.0
    emission_strength_socket.max_value = 1000000.0
    emission_strength_socket.subtype = 'NONE'
    emission_strength_socket.attribute_domain = 'POINT'
    emission_strength_socket.description = "Emission texture"
    emission_strength_socket.default_input = 'VALUE'
    emission_strength_socket.structure_type = 'AUTO'

    # Initialize eft_shader_emissive_1 nodes

    # Node Normal Map
    normal_map = eft_shader_emissive_1.nodes.new("ShaderNodeNormalMap")
    normal_map.name = "Normal Map"
    normal_map.show_options = True
    normal_map.base = 'DISPLACED'
    normal_map.convention = 'OPENGL'
    normal_map.space = 'TANGENT'
    normal_map.uv_map = ""
    # Strength
    normal_map.inputs[0].default_value = 1.0

    # Node Principled BSDF.001
    principled_bsdf_001 = eft_shader_emissive_1.nodes.new("ShaderNodeBsdfPrincipled")
    principled_bsdf_001.name = "Principled BSDF.001"
    principled_bsdf_001.show_options = True
    principled_bsdf_001.distribution = 'MULTI_GGX'
    principled_bsdf_001.subsurface_method = 'RANDOM_WALK_LEGACY'
    principled_bsdf_001.panel_states[0].is_collapsed = True
    principled_bsdf_001.panel_states[1].is_collapsed = True
    principled_bsdf_001.panel_states[2].is_collapsed = True
    principled_bsdf_001.panel_states[3].is_collapsed = True
    principled_bsdf_001.panel_states[4].is_collapsed = True
    principled_bsdf_001.panel_states[5].is_collapsed = True
    principled_bsdf_001.panel_states[6].is_collapsed = False
    principled_bsdf_001.panel_states[7].is_collapsed = True
    # IOR
    principled_bsdf_001.inputs[3].default_value = 1.0
    # Alpha
    principled_bsdf_001.inputs[4].default_value = 1.0
    # Thin Wall
    principled_bsdf_001.inputs[5].default_value = False
    # Diffuse Roughness
    principled_bsdf_001.inputs[8].default_value = 0.0
    # Subsurface Weight
    principled_bsdf_001.inputs[9].default_value = 0.0
    # Subsurface Radius
    principled_bsdf_001.inputs[10].default_value = (1.0, 0.20000000298023224, 0.10000000149011612)
    # Subsurface Scale
    principled_bsdf_001.inputs[11].default_value = 0.05000000074505806
    # Subsurface Anisotropy
    principled_bsdf_001.inputs[13].default_value = 0.0
    # Specular IOR Level
    principled_bsdf_001.inputs[14].default_value = 0.5
    # Specular Tint
    principled_bsdf_001.inputs[15].default_value = (1.0, 1.0, 1.0, 1.0)
    # Anisotropic
    principled_bsdf_001.inputs[16].default_value = 0.0
    # Anisotropic Rotation
    principled_bsdf_001.inputs[17].default_value = 0.0
    # Tangent
    principled_bsdf_001.inputs[18].default_value = (0.0, 0.0, 0.0)
    # Transmission Weight
    principled_bsdf_001.inputs[19].default_value = 0.0
    # Coat Weight
    principled_bsdf_001.inputs[20].default_value = 0.0
    # Coat Roughness
    principled_bsdf_001.inputs[21].default_value = 0.029999999329447746
    # Coat IOR
    principled_bsdf_001.inputs[22].default_value = 1.5
    # Coat Tint
    principled_bsdf_001.inputs[23].default_value = (1.0, 1.0, 1.0, 1.0)
    # Coat Normal
    principled_bsdf_001.inputs[24].default_value = (0.0, 0.0, 0.0)
    # Sheen Weight
    principled_bsdf_001.inputs[25].default_value = 0.0
    # Sheen Roughness
    principled_bsdf_001.inputs[26].default_value = 0.5
    # Sheen Tint
    principled_bsdf_001.inputs[27].default_value = (1.0, 1.0, 1.0, 1.0)
    # Thin Film Thickness
    principled_bsdf_001.inputs[30].default_value = 0.0
    # Thin Film IOR
    principled_bsdf_001.inputs[31].default_value = 1.3300000429153442

    # Node Invert Color
    invert_color = eft_shader_emissive_1.nodes.new("ShaderNodeInvert")
    invert_color.name = "Invert Color"
    invert_color.show_options = True
    # Fac
    invert_color.inputs[0].default_value = 1.0

    # Node Group Output
    group_output = eft_shader_emissive_1.nodes.new("NodeGroupOutput")
    group_output.name = "Group Output"
    group_output.show_options = True
    group_output.is_active_output = True

    # Node Group Input
    group_input = eft_shader_emissive_1.nodes.new("NodeGroupInput")
    group_input.name = "Group Input"
    group_input.show_options = True

    # Node Reroute
    reroute = eft_shader_emissive_1.nodes.new("NodeReroute")
    reroute.name = "Reroute"
    reroute.show_options = True
    reroute.socket_idname = "NodeSocketColor"
    # Node Reroute.001
    reroute_001 = eft_shader_emissive_1.nodes.new("NodeReroute")
    reroute_001.name = "Reroute.001"
    reroute_001.show_options = True
    reroute_001.socket_idname = "NodeSocketColor"
    # Node Reroute.002
    reroute_002 = eft_shader_emissive_1.nodes.new("NodeReroute")
    reroute_002.name = "Reroute.002"
    reroute_002.show_options = True
    reroute_002.socket_idname = "NodeSocketFloat"
    # Node Reroute.003
    reroute_003 = eft_shader_emissive_1.nodes.new("NodeReroute")
    reroute_003.name = "Reroute.003"
    reroute_003.show_options = True
    reroute_003.socket_idname = "NodeSocketFloat"
    # Node Reroute.004
    reroute_004 = eft_shader_emissive_1.nodes.new("NodeReroute")
    reroute_004.name = "Reroute.004"
    reroute_004.show_options = True
    reroute_004.socket_idname = "NodeSocketColor"
    # Node Reroute.005
    reroute_005 = eft_shader_emissive_1.nodes.new("NodeReroute")
    reroute_005.name = "Reroute.005"
    reroute_005.show_options = True
    reroute_005.socket_idname = "NodeSocketColor"
    # Node Reroute.006
    reroute_006 = eft_shader_emissive_1.nodes.new("NodeReroute")
    reroute_006.name = "Reroute.006"
    reroute_006.show_options = True
    reroute_006.socket_idname = "NodeSocketFloatFactor"
    # Node Reroute.007
    reroute_007 = eft_shader_emissive_1.nodes.new("NodeReroute")
    reroute_007.name = "Reroute.007"
    reroute_007.show_options = True
    reroute_007.socket_idname = "NodeSocketFloatFactor"
    # Set locations
    eft_shader_emissive_1.nodes["Normal Map"].location = (-272.2073974609375, -20.57086181640625)
    eft_shader_emissive_1.nodes["Principled BSDF.001"].location = (-72.2073974609375, 154.807373046875)
    eft_shader_emissive_1.nodes["Invert Color"].location = (-267.2073974609375, 122.09580993652344)
    eft_shader_emissive_1.nodes["Group Output"].location = (217.7926025390625, 154.807373046875)
    eft_shader_emissive_1.nodes["Group Input"].location = (-512.2073974609375, 40.380462646484375)
    eft_shader_emissive_1.nodes["Reroute"].location = (-272.2073974609375, -258.57086181640625)
    eft_shader_emissive_1.nodes["Reroute.001"].location = (-122.2073974609375, -258.57086181640625)
    eft_shader_emissive_1.nodes["Reroute.002"].location = (-272.2073974609375, -316.57086181640625)
    eft_shader_emissive_1.nodes["Reroute.003"].location = (-122.2073974609375, -316.57086181640625)
    eft_shader_emissive_1.nodes["Reroute.004"].location = (-272.2073974609375, 238.09580993652344)
    eft_shader_emissive_1.nodes["Reroute.005"].location = (-122.2073974609375, 238.09580993652344)
    eft_shader_emissive_1.nodes["Reroute.006"].location = (-272.2073974609375, 180.09580993652344)
    eft_shader_emissive_1.nodes["Reroute.007"].location = (-122.2073974609375, 180.09580993652344)

    # Set dimensions
    eft_shader_emissive_1.nodes["Normal Map"].width  = 150.0
    eft_shader_emissive_1.nodes["Normal Map"].height = 100.0

    eft_shader_emissive_1.nodes["Principled BSDF.001"].width  = 240.0
    eft_shader_emissive_1.nodes["Principled BSDF.001"].height = 100.0

    eft_shader_emissive_1.nodes["Invert Color"].width  = 140.0
    eft_shader_emissive_1.nodes["Invert Color"].height = 100.0

    eft_shader_emissive_1.nodes["Group Output"].width  = 140.0
    eft_shader_emissive_1.nodes["Group Output"].height = 100.0

    eft_shader_emissive_1.nodes["Group Input"].width  = 140.0
    eft_shader_emissive_1.nodes["Group Input"].height = 100.0

    eft_shader_emissive_1.nodes["Reroute"].width  = 14.5
    eft_shader_emissive_1.nodes["Reroute"].height = 100.0

    eft_shader_emissive_1.nodes["Reroute.001"].width  = 14.5
    eft_shader_emissive_1.nodes["Reroute.001"].height = 100.0

    eft_shader_emissive_1.nodes["Reroute.002"].width  = 14.5
    eft_shader_emissive_1.nodes["Reroute.002"].height = 100.0

    eft_shader_emissive_1.nodes["Reroute.003"].width  = 14.5
    eft_shader_emissive_1.nodes["Reroute.003"].height = 100.0

    eft_shader_emissive_1.nodes["Reroute.004"].width  = 14.5
    eft_shader_emissive_1.nodes["Reroute.004"].height = 100.0

    eft_shader_emissive_1.nodes["Reroute.005"].width  = 14.5
    eft_shader_emissive_1.nodes["Reroute.005"].height = 100.0

    eft_shader_emissive_1.nodes["Reroute.006"].width  = 14.5
    eft_shader_emissive_1.nodes["Reroute.006"].height = 100.0

    eft_shader_emissive_1.nodes["Reroute.007"].width  = 14.5
    eft_shader_emissive_1.nodes["Reroute.007"].height = 100.0


    # Initialize eft_shader_emissive_1 links

    # normal_map.Normal -> principled_bsdf_001.Normal
    eft_shader_emissive_1.links.new(
        eft_shader_emissive_1.nodes["Normal Map"].outputs[0],
        eft_shader_emissive_1.nodes["Principled BSDF.001"].inputs[6]
    )
    # invert_color.Color -> principled_bsdf_001.Roughness
    eft_shader_emissive_1.links.new(
        eft_shader_emissive_1.nodes["Invert Color"].outputs[0],
        eft_shader_emissive_1.nodes["Principled BSDF.001"].inputs[2]
    )
    # principled_bsdf_001.BSDF -> group_output.BSDF
    eft_shader_emissive_1.links.new(
        eft_shader_emissive_1.nodes["Principled BSDF.001"].outputs[0],
        eft_shader_emissive_1.nodes["Group Output"].inputs[0]
    )
    # group_input.N Converted -> normal_map.Color
    eft_shader_emissive_1.links.new(
        eft_shader_emissive_1.nodes["Group Input"].outputs[3],
        eft_shader_emissive_1.nodes["Normal Map"].inputs[1]
    )
    # group_input.G -> invert_color.Color
    eft_shader_emissive_1.links.new(
        eft_shader_emissive_1.nodes["Group Input"].outputs[2],
        eft_shader_emissive_1.nodes["Invert Color"].inputs[1]
    )
    # group_input.E -> reroute.Input
    eft_shader_emissive_1.links.new(
        eft_shader_emissive_1.nodes["Group Input"].outputs[4],
        eft_shader_emissive_1.nodes["Reroute"].inputs[0]
    )
    # group_input.Emission Strength -> reroute_002.Input
    eft_shader_emissive_1.links.new(
        eft_shader_emissive_1.nodes["Group Input"].outputs[5],
        eft_shader_emissive_1.nodes["Reroute.002"].inputs[0]
    )
    # group_input.D -> reroute_004.Input
    eft_shader_emissive_1.links.new(
        eft_shader_emissive_1.nodes["Group Input"].outputs[0],
        eft_shader_emissive_1.nodes["Reroute.004"].inputs[0]
    )
    # group_input.D alpha -> reroute_006.Input
    eft_shader_emissive_1.links.new(
        eft_shader_emissive_1.nodes["Group Input"].outputs[1],
        eft_shader_emissive_1.nodes["Reroute.006"].inputs[0]
    )
    # reroute.Output -> reroute_001.Input
    eft_shader_emissive_1.links.new(
        eft_shader_emissive_1.nodes["Reroute"].outputs[0],
        eft_shader_emissive_1.nodes["Reroute.001"].inputs[0]
    )
    # reroute_002.Output -> reroute_003.Input
    eft_shader_emissive_1.links.new(
        eft_shader_emissive_1.nodes["Reroute.002"].outputs[0],
        eft_shader_emissive_1.nodes["Reroute.003"].inputs[0]
    )
    # reroute_004.Output -> reroute_005.Input
    eft_shader_emissive_1.links.new(
        eft_shader_emissive_1.nodes["Reroute.004"].outputs[0],
        eft_shader_emissive_1.nodes["Reroute.005"].inputs[0]
    )
    # reroute_006.Output -> reroute_007.Input
    eft_shader_emissive_1.links.new(
        eft_shader_emissive_1.nodes["Reroute.006"].outputs[0],
        eft_shader_emissive_1.nodes["Reroute.007"].inputs[0]
    )
    # reroute_005.Output -> principled_bsdf_001.Base Color
    eft_shader_emissive_1.links.new(
        eft_shader_emissive_1.nodes["Reroute.005"].outputs[0],
        eft_shader_emissive_1.nodes["Principled BSDF.001"].inputs[0]
    )
    # reroute_007.Output -> principled_bsdf_001.Metallic
    eft_shader_emissive_1.links.new(
        eft_shader_emissive_1.nodes["Reroute.007"].outputs[0],
        eft_shader_emissive_1.nodes["Principled BSDF.001"].inputs[1]
    )
    # reroute_001.Output -> principled_bsdf_001.Emission Color
    eft_shader_emissive_1.links.new(
        eft_shader_emissive_1.nodes["Reroute.001"].outputs[0],
        eft_shader_emissive_1.nodes["Principled BSDF.001"].inputs[28]
    )
    # reroute_003.Output -> principled_bsdf_001.Emission Strength
    eft_shader_emissive_1.links.new(
        eft_shader_emissive_1.nodes["Reroute.003"].outputs[0],
        eft_shader_emissive_1.nodes["Principled BSDF.001"].inputs[29]
    )

    return eft_shader_emissive_1

# Transparent shader
def NG_Shader_Hair(node_name = "EFT_Shader_Hair"):

    """Initialize EFT_Shader_Hair node group"""
    eft_shader_hair_1 = bpy.data.node_groups.new(type = 'ShaderNodeTree', name = node_name)

    eft_shader_hair_1.color_tag = 'NONE'
    eft_shader_hair_1.description = ""
    eft_shader_hair_1.default_group_node_width = 140
    # eft_shader_hair_1 interface

    # Socket BSDF
    bsdf_socket = eft_shader_hair_1.interface.new_socket(name="BSDF", in_out='OUTPUT', socket_type='NodeSocketShader')
    bsdf_socket.attribute_domain = 'POINT'
    bsdf_socket.description = "EFT Transparent Shader"
    bsdf_socket.default_input = 'VALUE'
    bsdf_socket.structure_type = 'AUTO'

    # Socket D
    d_socket = eft_shader_hair_1.interface.new_socket(name="D", in_out='INPUT', socket_type='NodeSocketColor')
    d_socket.default_value = (0.800000011920929, 0.800000011920929, 0.800000011920929, 1.0)
    d_socket.attribute_domain = 'POINT'
    d_socket.description = "Diffuse"
    d_socket.default_input = 'VALUE'
    d_socket.structure_type = 'AUTO'

    # Socket D alpha
    d_alpha_socket = eft_shader_hair_1.interface.new_socket(name="D alpha", in_out='INPUT', socket_type='NodeSocketFloat')
    d_alpha_socket.default_value = 0.0
    d_alpha_socket.min_value = 0.0
    d_alpha_socket.max_value = 1.0
    d_alpha_socket.subtype = 'FACTOR'
    d_alpha_socket.attribute_domain = 'POINT'
    d_alpha_socket.description = "Alpha"
    d_alpha_socket.default_input = 'VALUE'
    d_alpha_socket.structure_type = 'AUTO'

    # Socket G
    g_socket = eft_shader_hair_1.interface.new_socket(name="G", in_out='INPUT', socket_type='NodeSocketColor')
    g_socket.default_value = (0.0, 0.0, 0.0, 1.0)
    g_socket.attribute_domain = 'POINT'
    g_socket.description = "Glossiness"
    g_socket.default_input = 'VALUE'
    g_socket.structure_type = 'AUTO'

    # Socket N Converted
    n_converted_socket = eft_shader_hair_1.interface.new_socket(name="N Converted", in_out='INPUT', socket_type='NodeSocketColor')
    n_converted_socket.default_value = (0.5, 0.5, 1.0, 1.0)
    n_converted_socket.attribute_domain = 'POINT'
    n_converted_socket.description = "Converted Normal map"
    n_converted_socket.default_input = 'VALUE'
    n_converted_socket.structure_type = 'AUTO'

    # Initialize eft_shader_hair_1 nodes

    # Node Normal Map
    normal_map = eft_shader_hair_1.nodes.new("ShaderNodeNormalMap")
    normal_map.name = "Normal Map"
    normal_map.show_options = True
    normal_map.base = 'DISPLACED'
    normal_map.convention = 'OPENGL'
    normal_map.space = 'TANGENT'
    normal_map.uv_map = ""
    # Strength
    normal_map.inputs[0].default_value = 1.0

    # Node Principled BSDF.001
    principled_bsdf_001 = eft_shader_hair_1.nodes.new("ShaderNodeBsdfPrincipled")
    principled_bsdf_001.name = "Principled BSDF.001"
    principled_bsdf_001.show_options = True
    principled_bsdf_001.distribution = 'MULTI_GGX'
    principled_bsdf_001.subsurface_method = 'RANDOM_WALK_LEGACY'
    principled_bsdf_001.panel_states[0].is_collapsed = True
    principled_bsdf_001.panel_states[1].is_collapsed = True
    principled_bsdf_001.panel_states[2].is_collapsed = True
    principled_bsdf_001.panel_states[3].is_collapsed = True
    principled_bsdf_001.panel_states[4].is_collapsed = True
    principled_bsdf_001.panel_states[5].is_collapsed = True
    principled_bsdf_001.panel_states[6].is_collapsed = True
    principled_bsdf_001.panel_states[7].is_collapsed = True
    # Metallic
    principled_bsdf_001.inputs[1].default_value = 0.0
    # IOR
    principled_bsdf_001.inputs[3].default_value = 1.0
    # Thin Wall
    principled_bsdf_001.inputs[5].default_value = False
    # Diffuse Roughness
    principled_bsdf_001.inputs[8].default_value = 0.0
    # Subsurface Weight
    principled_bsdf_001.inputs[9].default_value = 0.0
    # Subsurface Radius
    principled_bsdf_001.inputs[10].default_value = (1.0, 0.20000000298023224, 0.10000000149011612)
    # Subsurface Scale
    principled_bsdf_001.inputs[11].default_value = 0.05000000074505806
    # Subsurface Anisotropy
    principled_bsdf_001.inputs[13].default_value = 0.0
    # Specular IOR Level
    principled_bsdf_001.inputs[14].default_value = 0.5
    # Specular Tint
    principled_bsdf_001.inputs[15].default_value = (1.0, 1.0, 1.0, 1.0)
    # Anisotropic
    principled_bsdf_001.inputs[16].default_value = 0.0
    # Anisotropic Rotation
    principled_bsdf_001.inputs[17].default_value = 0.0
    # Tangent
    principled_bsdf_001.inputs[18].default_value = (0.0, 0.0, 0.0)
    # Transmission Weight
    principled_bsdf_001.inputs[19].default_value = 0.0
    # Coat Weight
    principled_bsdf_001.inputs[20].default_value = 0.0
    # Coat Roughness
    principled_bsdf_001.inputs[21].default_value = 0.029999999329447746
    # Coat IOR
    principled_bsdf_001.inputs[22].default_value = 1.5
    # Coat Tint
    principled_bsdf_001.inputs[23].default_value = (1.0, 1.0, 1.0, 1.0)
    # Coat Normal
    principled_bsdf_001.inputs[24].default_value = (0.0, 0.0, 0.0)
    # Sheen Weight
    principled_bsdf_001.inputs[25].default_value = 0.0
    # Sheen Roughness
    principled_bsdf_001.inputs[26].default_value = 0.5
    # Sheen Tint
    principled_bsdf_001.inputs[27].default_value = (1.0, 1.0, 1.0, 1.0)
    # Emission Color
    principled_bsdf_001.inputs[28].default_value = (1.0, 1.0, 1.0, 1.0)
    # Emission Strength
    principled_bsdf_001.inputs[29].default_value = 0.0
    # Thin Film Thickness
    principled_bsdf_001.inputs[30].default_value = 0.0
    # Thin Film IOR
    principled_bsdf_001.inputs[31].default_value = 1.3300000429153442

    # Node Invert Color
    invert_color = eft_shader_hair_1.nodes.new("ShaderNodeInvert")
    invert_color.name = "Invert Color"
    invert_color.show_options = True
    # Fac
    invert_color.inputs[0].default_value = 1.0

    # Node Group Output
    group_output = eft_shader_hair_1.nodes.new("NodeGroupOutput")
    group_output.name = "Group Output"
    group_output.show_options = True
    group_output.is_active_output = True

    # Node Group Input
    group_input = eft_shader_hair_1.nodes.new("NodeGroupInput")
    group_input.name = "Group Input"
    group_input.show_options = True

    # Node Reroute
    reroute = eft_shader_hair_1.nodes.new("NodeReroute")
    reroute.name = "Reroute"
    reroute.show_options = True
    reroute.socket_idname = "NodeSocketColor"
    # Node Reroute.001
    reroute_001 = eft_shader_hair_1.nodes.new("NodeReroute")
    reroute_001.name = "Reroute.001"
    reroute_001.show_options = True
    reroute_001.socket_idname = "NodeSocketColor"
    # Node Reroute.002
    reroute_002 = eft_shader_hair_1.nodes.new("NodeReroute")
    reroute_002.name = "Reroute.002"
    reroute_002.show_options = True
    reroute_002.socket_idname = "NodeSocketFloatFactor"
    # Node Reroute.003
    reroute_003 = eft_shader_hair_1.nodes.new("NodeReroute")
    reroute_003.name = "Reroute.003"
    reroute_003.show_options = True
    reroute_003.socket_idname = "NodeSocketFloatFactor"
    # Set locations
    eft_shader_hair_1.nodes["Normal Map"].location = (-279.109130859375, -187.37216186523438)
    eft_shader_hair_1.nodes["Principled BSDF.001"].location = (-79.109130859375, 71.51774597167969)
    eft_shader_hair_1.nodes["Invert Color"].location = (-274.109130859375, -44.70549011230469)
    eft_shader_hair_1.nodes["Group Output"].location = (210.890869140625, 71.51774597167969)
    eft_shader_hair_1.nodes["Group Input"].location = (-481.609130859375, 15.13951301574707)
    eft_shader_hair_1.nodes["Reroute"].location = (-279.109130859375, 71.29450988769531)
    eft_shader_hair_1.nodes["Reroute.001"].location = (-129.109130859375, 71.29450988769531)
    eft_shader_hair_1.nodes["Reroute.002"].location = (-279.109130859375, 13.294512748718262)
    eft_shader_hair_1.nodes["Reroute.003"].location = (-129.109130859375, 13.294512748718262)

    # Set dimensions
    eft_shader_hair_1.nodes["Normal Map"].width  = 150.0
    eft_shader_hair_1.nodes["Normal Map"].height = 100.0

    eft_shader_hair_1.nodes["Principled BSDF.001"].width  = 240.0
    eft_shader_hair_1.nodes["Principled BSDF.001"].height = 100.0

    eft_shader_hair_1.nodes["Invert Color"].width  = 140.0
    eft_shader_hair_1.nodes["Invert Color"].height = 100.0

    eft_shader_hair_1.nodes["Group Output"].width  = 140.0
    eft_shader_hair_1.nodes["Group Output"].height = 100.0

    eft_shader_hair_1.nodes["Group Input"].width  = 140.0
    eft_shader_hair_1.nodes["Group Input"].height = 100.0

    eft_shader_hair_1.nodes["Reroute"].width  = 14.5
    eft_shader_hair_1.nodes["Reroute"].height = 100.0

    eft_shader_hair_1.nodes["Reroute.001"].width  = 14.5
    eft_shader_hair_1.nodes["Reroute.001"].height = 100.0

    eft_shader_hair_1.nodes["Reroute.002"].width  = 14.5
    eft_shader_hair_1.nodes["Reroute.002"].height = 100.0

    eft_shader_hair_1.nodes["Reroute.003"].width  = 14.5
    eft_shader_hair_1.nodes["Reroute.003"].height = 100.0


    # Initialize eft_shader_hair_1 links

    # normal_map.Normal -> principled_bsdf_001.Normal
    eft_shader_hair_1.links.new(
        eft_shader_hair_1.nodes["Normal Map"].outputs[0],
        eft_shader_hair_1.nodes["Principled BSDF.001"].inputs[6]
    )
    # invert_color.Color -> principled_bsdf_001.Roughness
    eft_shader_hair_1.links.new(
        eft_shader_hair_1.nodes["Invert Color"].outputs[0],
        eft_shader_hair_1.nodes["Principled BSDF.001"].inputs[2]
    )
    # principled_bsdf_001.BSDF -> group_output.BSDF
    eft_shader_hair_1.links.new(
        eft_shader_hair_1.nodes["Principled BSDF.001"].outputs[0],
        eft_shader_hair_1.nodes["Group Output"].inputs[0]
    )
    # group_input.N Converted -> normal_map.Color
    eft_shader_hair_1.links.new(
        eft_shader_hair_1.nodes["Group Input"].outputs[3],
        eft_shader_hair_1.nodes["Normal Map"].inputs[1]
    )
    # group_input.G -> invert_color.Color
    eft_shader_hair_1.links.new(
        eft_shader_hair_1.nodes["Group Input"].outputs[2],
        eft_shader_hair_1.nodes["Invert Color"].inputs[1]
    )
    # group_input.D -> reroute.Input
    eft_shader_hair_1.links.new(
        eft_shader_hair_1.nodes["Group Input"].outputs[0],
        eft_shader_hair_1.nodes["Reroute"].inputs[0]
    )
    # group_input.D alpha -> reroute_002.Input
    eft_shader_hair_1.links.new(
        eft_shader_hair_1.nodes["Group Input"].outputs[1],
        eft_shader_hair_1.nodes["Reroute.002"].inputs[0]
    )
    # reroute.Output -> reroute_001.Input
    eft_shader_hair_1.links.new(
        eft_shader_hair_1.nodes["Reroute"].outputs[0],
        eft_shader_hair_1.nodes["Reroute.001"].inputs[0]
    )
    # reroute_002.Output -> reroute_003.Input
    eft_shader_hair_1.links.new(
        eft_shader_hair_1.nodes["Reroute.002"].outputs[0],
        eft_shader_hair_1.nodes["Reroute.003"].inputs[0]
    )
    # reroute_001.Output -> principled_bsdf_001.Base Color
    eft_shader_hair_1.links.new(
        eft_shader_hair_1.nodes["Reroute.001"].outputs[0],
        eft_shader_hair_1.nodes["Principled BSDF.001"].inputs[0]
    )
    # reroute_003.Output -> principled_bsdf_001.Alpha
    eft_shader_hair_1.links.new(
        eft_shader_hair_1.nodes["Reroute.003"].outputs[0],
        eft_shader_hair_1.nodes["Principled BSDF.001"].inputs[4]
    )

    return eft_shader_hair_1


def NG_Shader_Puddle(node_name = "EFT_Puddle"):
    """Initialize EFT_Puddle node group"""
    eft_puddle_1 = bpy.data.node_groups.new(type = 'ShaderNodeTree', name = node_name)

    eft_puddle_1.color_tag = 'NONE'
    eft_puddle_1.description = ""
    eft_puddle_1.default_group_node_width = 140
    # eft_puddle_1 interface

    # Socket Shader
    shader_socket = eft_puddle_1.interface.new_socket(name="BSDF", in_out='OUTPUT', socket_type='NodeSocketShader')
    shader_socket.attribute_domain = 'POINT'
    shader_socket.default_input = 'VALUE'
    shader_socket.structure_type = 'AUTO'

    # Socket Color
    color_socket = eft_puddle_1.interface.new_socket(name="D", in_out='INPUT', socket_type='NodeSocketColor')
    color_socket.default_value = (0.800000011920929, 0.800000011920929, 0.800000011920929, 1.0)
    color_socket.attribute_domain = 'POINT'
    color_socket.default_input = 'VALUE'
    color_socket.structure_type = 'AUTO'

    # Socket Alpha
    alpha_socket = eft_puddle_1.interface.new_socket(name="D alpha", in_out='INPUT', socket_type='NodeSocketFloat')
    alpha_socket.default_value = 0.0
    alpha_socket.min_value = -3.4028234663852886e+38
    alpha_socket.max_value = 3.4028234663852886e+38
    alpha_socket.subtype = 'NONE'
    alpha_socket.attribute_domain = 'POINT'
    alpha_socket.default_input = 'VALUE'
    alpha_socket.structure_type = 'AUTO'

    # Initialize eft_puddle_1 nodes

    # Node Principled BSDF
    principled_bsdf = eft_puddle_1.nodes.new("ShaderNodeBsdfPrincipled")
    principled_bsdf.name = "Principled BSDF"
    principled_bsdf.show_options = True
    principled_bsdf.distribution = 'MULTI_GGX'
    principled_bsdf.subsurface_method = 'RANDOM_WALK'
    principled_bsdf.panel_states[0].is_collapsed = True
    principled_bsdf.panel_states[1].is_collapsed = True
    principled_bsdf.panel_states[2].is_collapsed = False
    principled_bsdf.panel_states[3].is_collapsed = True
    principled_bsdf.panel_states[4].is_collapsed = True
    principled_bsdf.panel_states[5].is_collapsed = True
    principled_bsdf.panel_states[6].is_collapsed = True
    principled_bsdf.panel_states[7].is_collapsed = True
    # Metallic
    principled_bsdf.inputs[1].default_value = 0.0
    # Roughness
    principled_bsdf.inputs[2].default_value = 0.09365558624267578
    # IOR
    principled_bsdf.inputs[3].default_value = 1.3329999446868896
    # Thin Wall
    principled_bsdf.inputs[5].default_value = False
    # Normal
    principled_bsdf.inputs[6].default_value = (0.0, 0.0, 0.0)
    # Diffuse Roughness
    principled_bsdf.inputs[8].default_value = 0.0
    # Subsurface Weight
    principled_bsdf.inputs[9].default_value = 0.0
    # Subsurface Radius
    principled_bsdf.inputs[10].default_value = (1.0, 0.20000000298023224, 0.10000000149011612)
    # Subsurface Scale
    principled_bsdf.inputs[11].default_value = 0.004999999888241291
    # Subsurface Anisotropy
    principled_bsdf.inputs[13].default_value = 0.0
    # Specular IOR Level
    principled_bsdf.inputs[14].default_value = 0.33000001311302185
    # Specular Tint
    principled_bsdf.inputs[15].default_value = (1.0, 1.0, 1.0, 1.0)
    # Anisotropic
    principled_bsdf.inputs[16].default_value = 0.0
    # Anisotropic Rotation
    principled_bsdf.inputs[17].default_value = 0.0
    # Tangent
    principled_bsdf.inputs[18].default_value = (0.0, 0.0, 0.0)
    # Transmission Weight
    principled_bsdf.inputs[19].default_value = 0.0
    # Coat Weight
    principled_bsdf.inputs[20].default_value = 0.0
    # Coat Roughness
    principled_bsdf.inputs[21].default_value = 0.029999999329447746
    # Coat IOR
    principled_bsdf.inputs[22].default_value = 1.5
    # Coat Tint
    principled_bsdf.inputs[23].default_value = (1.0, 1.0, 1.0, 1.0)
    # Coat Normal
    principled_bsdf.inputs[24].default_value = (0.0, 0.0, 0.0)
    # Sheen Weight
    principled_bsdf.inputs[25].default_value = 0.0
    # Sheen Roughness
    principled_bsdf.inputs[26].default_value = 0.5
    # Sheen Tint
    principled_bsdf.inputs[27].default_value = (1.0, 1.0, 1.0, 1.0)
    # Emission Color
    principled_bsdf.inputs[28].default_value = (1.0, 1.0, 1.0, 1.0)
    # Emission Strength
    principled_bsdf.inputs[29].default_value = 0.0
    # Thin Film Thickness
    principled_bsdf.inputs[30].default_value = 0.0
    # Thin Film IOR
    principled_bsdf.inputs[31].default_value = 1.3300000429153442

    # Node Mix Shader
    mix_shader = eft_puddle_1.nodes.new("ShaderNodeMixShader")
    mix_shader.name = "Mix Shader"
    mix_shader.show_options = True

    # Node Transparent BSDF
    transparent_bsdf = eft_puddle_1.nodes.new("ShaderNodeBsdfTransparent")
    transparent_bsdf.name = "Transparent BSDF"
    transparent_bsdf.show_options = True
    # Color
    transparent_bsdf.inputs[0].default_value = (1.0, 1.0, 1.0, 1.0)

    # Node Fresnel
    fresnel = eft_puddle_1.nodes.new("ShaderNodeFresnel")
    fresnel.name = "Fresnel"
    fresnel.show_options = True
    # IOR
    fresnel.inputs[0].default_value = 1.3300000429153442
    # Normal
    fresnel.inputs[1].default_value = (0.0, 0.0, 0.0)

    # Node Group Output
    group_output = eft_puddle_1.nodes.new("NodeGroupOutput")
    group_output.name = "Group Output"
    group_output.show_options = True
    group_output.is_active_output = True

    # Node Group Input
    group_input = eft_puddle_1.nodes.new("NodeGroupInput")
    group_input.name = "Group Input"
    group_input.show_options = True

    # Set locations
    eft_puddle_1.nodes["Principled BSDF"].location = (-159.414794921875, -39.111572265625)
    eft_puddle_1.nodes["Mix Shader"].location = (143.085205078125, 84.22176361083984)
    eft_puddle_1.nodes["Transparent BSDF"].location = (-109.414794921875, 84.22177124023438)
    eft_puddle_1.nodes["Fresnel"].location = (-109.414794921875, 227.5550994873047)
    eft_puddle_1.nodes["Group Output"].location = (333.085205078125, 84.22176361083984)
    eft_puddle_1.nodes["Group Input"].location = (-349.414794921875, -92.1693115234375)

    # Set dimensions
    eft_puddle_1.nodes["Principled BSDF"].width  = 240.0
    eft_puddle_1.nodes["Principled BSDF"].height = 100.0

    eft_puddle_1.nodes["Mix Shader"].width  = 140.0
    eft_puddle_1.nodes["Mix Shader"].height = 100.0

    eft_puddle_1.nodes["Transparent BSDF"].width  = 140.0
    eft_puddle_1.nodes["Transparent BSDF"].height = 100.0

    eft_puddle_1.nodes["Fresnel"].width  = 140.0
    eft_puddle_1.nodes["Fresnel"].height = 100.0

    eft_puddle_1.nodes["Group Output"].width  = 140.0
    eft_puddle_1.nodes["Group Output"].height = 100.0

    eft_puddle_1.nodes["Group Input"].width  = 140.0
    eft_puddle_1.nodes["Group Input"].height = 100.0


    # Initialize eft_puddle_1 links

    # fresnel.Factor -> mix_shader.Factor
    eft_puddle_1.links.new(
        eft_puddle_1.nodes["Fresnel"].outputs[0],
        eft_puddle_1.nodes["Mix Shader"].inputs[0]
    )
    # principled_bsdf.BSDF -> mix_shader.Shader
    eft_puddle_1.links.new(
        eft_puddle_1.nodes["Principled BSDF"].outputs[0],
        eft_puddle_1.nodes["Mix Shader"].inputs[2]
    )
    # transparent_bsdf.BSDF -> mix_shader.Shader
    eft_puddle_1.links.new(
        eft_puddle_1.nodes["Transparent BSDF"].outputs[0],
        eft_puddle_1.nodes["Mix Shader"].inputs[1]
    )
    # group_input.Alpha -> principled_bsdf.Alpha
    eft_puddle_1.links.new(
        eft_puddle_1.nodes["Group Input"].outputs[1],
        eft_puddle_1.nodes["Principled BSDF"].inputs[4]
    )
    # group_input.Color -> principled_bsdf.Base Color
    eft_puddle_1.links.new(
        eft_puddle_1.nodes["Group Input"].outputs[0],
        eft_puddle_1.nodes["Principled BSDF"].inputs[0]
    )
    # mix_shader.Shader -> group_output.Shader
    eft_puddle_1.links.new(
        eft_puddle_1.nodes["Mix Shader"].outputs[0],
        eft_puddle_1.nodes["Group Output"].inputs[0]
    )

    return eft_puddle_1

