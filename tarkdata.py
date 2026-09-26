import numpy as np

def load() :

    print("Loading data lists")

    NODE_DELETE_LIST = ["Principled BSDF","Normal Map"]

    DGN_TYPE_LIST = np.array([["_D.png", "_G.png", "_N.png"],
                          ["_d.png", "_g.png", "_n.png"],
                          ["_diff.png", "_gloss.png", "_nrm.png"],
                          ["_DIF.png", "_GLOS.png", "_NRM.png"],
                          ["_dif.png", "_glos.png", "_nrm.png"],
                          ["_albedo.png", "_gloss.png", "_normal.png"],
                          ["[Albedo].png", "[Gloss].png", "[Normal].png"]])

    ATLAS_EXCEPTIONS = ["Atlas2.png", "atlas_1_D.png", "atlas_2_D.png", "atlas_cafe_DIF.png",
                    "barns_atlas_1_D.png", "barns_atlas_2_D.png", "bipod_all_atlas_v8_bt10_LOD0_diff.png",
                    "bipod_all_atlas_v8_bt10_LOD0_diff_0.png", "bipod_all_atlas_v8_bt10_LOD0_diff_1.png",
                    "bipod_all_atlas_v8_bt10_LOD1_diff.png", "bipod_all_atlas_v8_bt10_LOD1_diff_0.png",
                    "City_puddle_atlas_D.png", "details_atlas_bridge_albedo.png", "fck_atlas_d.png",
                    "fck_atlas_d_0.png", "Icebreaker_decal_atlas_02_d.png","Icebreaker_parts_atlas_01_D.png",
                    "Icebreaker_parts_atlas_01_D_0.png", "Lab_cable_atlas_dif.png",
                    "Lighthouse_Plywood_atlas_D.png", "muzzle_ar10_odin_works_atlas_7_muzzle_brake_762x51_LOD0_diff.png",
                    "muzzle_ar10_odin_works_atlas_7_muzzle_brake_762x51_LOD1_diff.png",
                    "Old_Electrical_Atlas_Part_1_D.png", "Old_Electrical_Atlas_Part_2_D.png",
                    "Quests_photo_atlas_2_D.png", "Reserve_Hospital_and_HQ_posters_atlas.png", 
                    "Reserve_sport_posters_atlas.png", "sanatorium_ATLAS_1.png",
                    "shopping_mall_LED_panel_atlas_albedo.png", "Strahovaya_posters_atlas_1.png",
                    "Strahovaya_posters_atlas_2.png", "stump05_Atlas.png", "summerhouse_atlas_d.png",
                    "Woodbox_atlas_d.png", "Xmass_posters_atlas_01.png", "Xmass_posters_atlas_02.png",
                    "Xmass_posters_atlas_03.png"]

    TRANSPARENT_NAMES = ["decal", "Decal", "_hair_", "Hair_", "bruno",
                    "setka", "chain_fence", "plastic_bucket",
                    "drop_wood", "Cactus_D_Mask", "facecover_gasmask_GP5_glass",
                    "gasmask_gp7_glass.png", "smoke_thin_2-2_random",
                    "City_road_marking", "Reserve_paint_edge", "Red_Stripes",
                    "Reserve_Wall_Crack", "curtains5", "Web_atlas"
                    "Lighthouse_plaster_damaged_bottom_trim_no_border",
                    "Lighthouse_Concrete_Damaged_opacity_light",
                    "City_glass5_transparent", "Chemical_plant", "grille"
                    "City_glass_broken_transparent", "Concrete_trims",
                    "Electronica_4_glass", "city_palm_plant_d_DRAFT_TO_CHANGE",
                    "item_barter_valuable_rolex_Glass", "lab_glass",
                    "Glass_stains", "paper_garbage2_footsteps", "Floor_metal_grate_rust_01",
                    "City_broken_glass_atlas", "Flowers_D", "lab_ChemProtectGlass",
                    "bulletholes_concrete", "Reserve_factroy_glass",
                    "City_glass_broken_transparent", "City_Asphalt_Trim",
                    "Vendors_snow_footprint"]

    OBJ_TO_DELETE = ["Cube", "BLOCKER", "Blocker", "LOD1", "LOD2", "LOD3", "LOD4",
                "Box0", "Plane", "shadow", "Shadow", "SHADOW", "collider",
                "colider", "Collider", "Stencil", "stencil", "STENCIL", "Stensil",
                "factory_Trigger"]

    EMISSIVE_TYPE_LIST = ["Emissive","emissive","_E.png", "emisiive", "emission"]

    print("Data lists loaded")

    return NODE_DELETE_LIST, DGN_TYPE_LIST, ATLAS_EXCEPTIONS, TRANSPARENT_NAMES, OBJ_TO_DELETE, EMISSIVE_TYPE_LIST