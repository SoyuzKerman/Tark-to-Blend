# Tark_to_Blend
A Blender add-on to easily import Escape from Tarkov scenes with Assetstudio.

If you need help, send an email at [contact@soyuzkerman.net](mailto:contact@soyuzkerman.net).

Visit [soyuzkerman.net](https://soyuzkerman.net/article/tarkov-maps/0-0-introduction/) for more information on the program and the material setup.

Check my [Open3DLab profile](https://open3dlab.com/user/254875/) to see the stuff I already ported to Blender.

## Requirements
- The game _Escape from Tarkov_ downloaded on your PC.
- Assetstudio. The original version is not maintained. I recommend [aelurum's fork](https://github.com/aelurum/AssetStudioMod) or [Razviar's fork](https://github.com/Razviar/assetstudio). Razviar's version has a mapping function that is useful for exporting characters.
- Blender. The add-on was tested on 5.2.0.

## How to install

1. On the [main github page](https://github.com/SoyuzKerman/Tark-to-Blend), click the green **Code** button and select **Download ZIP**.
2. In Blender, go to Edit > Preferences > Add-ons. Click on the arrow button and select **Install from disk**.

<img width="463" height="286" alt="image" src="https://github.com/user-attachments/assets/1ca45b55-9e1b-45a8-86bb-8598b23a9a3f" />

3. Select the ZIP folder you downloaded on Step 1.
4. Check if the add-on appears in your add-on list :

<img width="784" height="283" alt="image" src="https://github.com/user-attachments/assets/43fa1f29-da1b-4b9d-b8ce-25393481118c" />


## How to use

### Getting level files

1. Select a map of interest in the [Map List](https://github.com/SoyuzKerman/Tark-to-Blend/blob/main/map_list.csv). This map list was built based on [DrakiaXYZ's Map Info Extractor](https://github.com/DrakiaXYZ/SPT-MapInfoExtractor/). As an example, we will choose the Ragman scene contained in the **level643** file.
2. Load the **level** file in AssetStudio :
   - File > Load file, then go to the game folders and select the file : Escape from Tarkov > EscapeFromTarkov_Data > level643
   - Wait for a few minutes for the assets to load.
   - In *Scene Hierarchy*, tick the box next to the **level** file :
   - Click Model > Export selected objects (merge)
<img width="549" height="477" alt="image" src="https://github.com/user-attachments/assets/2513a6b7-4bc3-434b-8085-73c56f8e3718" />

   - Choose a folder to save the scene as a FBX file. I like to rename the file with the name of the level to remember where it comes from.
    The output folder opens automatically once the process is over. It should contain a FBX file (containing geometry and material data) and PNG texture files.

<img width="613" height="387" alt="image" src="https://github.com/user-attachments/assets/59c8a0d5-5178-4cf7-bb66-a600f151b113" />

   - I prefer to keep the textures in a separate "textures" folder.

NOTE : The normal map textures are red. This is normal and the material setup takes it into account.

### Using the add-on

1. Start from an empty scene in Blender.
2. Drag and drop the FBX file in the scene to import it. It should look like this :
<img width="1000" height="500" alt="image" src="https://github.com/user-attachments/assets/6ee3e3a9-10fd-49b5-b33f-013424a8203c" />

The actual scene is hidden behind objects that will be deleted by the add-on. If we hide them, the actual scene becomes visible. By default, the objects look transparent because Blender interprets the *Alpha* channel of the texture as transparency, when it is not. This will be fixed by the add-on.

3. If you previously put the textures in a separate folder, check if the textures are missing by using **Material Preview**. If everything is pink, the textures are missing. Go to File > External data > Find missing files, and select your "textures" folder.
4. In the **3D Viewport**, press **N** to open the **side panel** and go to the "Tark to Blend" panel.

<img width="239" height="265" alt="6_addon" src="https://github.com/user-attachments/assets/799579d6-e8e8-43bc-9d25-09c2f0c6da1d" />

5. To use the panel :
    - *Clean scene* will remove all empties. **This is recommended for maps, but not characters** as it will break some animations (more precisely, the item animations).
    - *Save CSV* will create a CSV file with all material properties in your "textures" folder. **This is intended for debug and you do not need to use it**.
    - Click on the folder icon to indicate the path to your "texture" folder. This is where the program will search for missing textures. **This is mandatory**.
    - Before starting the program, you can toggle the Blender console in Window > Toggle system console.
    - Click *Start process* to start the automatic cleanup and material setup. **Do not click anything in the Blender interface until the *Start process* button turned to gray again**. You can follow the progress in the console if you activated it.
    - During the process, the scene is scaled from 0.01 to 1. Look around to find it if it moved. The scene should now look like this :
<img width="1023" height="576" alt="image" src="https://github.com/user-attachments/assets/5eae6a2b-f44b-4830-8123-10c03160fddb" />

### Manual Cleanup

1. Delete the character and leftover objects. In this example we have Ragman and some random backpacks flying around.
2. Create collections to sort the objects. I like having a *Walls* collection to be able to hide them easily, and a *Effects* collection where I can hide the volumetric textures that we do not need in Blender. Now we can see a bit clearer :
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/1a83903c-0d9d-4238-8b7c-eaea9db90a14" />

3. The **bright red objects** have missing textures. If it's simple, you can create it (for example, a solid color material or the glass material for a wall clock appearing on some levels). Otherwise, hide/delete it.

<img width="361" height="531" alt="image" src="https://github.com/user-attachments/assets/6ed456ec-65e2-4ca8-a795-f6cb55bf2970" />

4. **Combination of textures :** Some materials use a combination of textures combined by masking and vertex painting, they are called *VP Materials*. Such materials should be detected by the add-on and appear as **blue** in the 3D viewport with `solid` shading. Otherwise, it will appear as **red** in `material` shading (missing textures). An example is shown below.

<img width="1403" height="843" alt="10_vpmaterials" src="https://github.com/user-attachments/assets/ab983fd7-4bcc-4a73-a690-461a21ff0cf6" />

When a *VP material* is detected, a node setup is loaded in the <samp>Shader Editor</samp>. It must be manually completed with different textures :
- **A "MASK" texture** must be plugged into the <mark>EFT_VP_Mask</mark> custom node group. Once it's done, the areas corresponding to each of the three materials will appear as red, green and blue in the viewport with `material` shading.
- At least **three textures** must be added, one diffuse texture for each material, located in the *RED*, *GREEN* and *BLUE* frames. Generally, six textures will be needed (a diffuse and a normal map per material).
- The "MASK" texture and the normal maps must be set to **non-color** mode.

To know which textures to add, use reference screenshots from the game. The material name is usually close to the "MASK" texture name and to one of the materials involved. The result of the **EFT_VP_Mask** group can also be used for comparison with a reference image.

<img width="1512" height="761" alt="10_vpnodes" src="https://github.com/user-attachments/assets/0dc3b528-1ede-488c-a93a-37a98f02f168" />

5. Remove [detail maps](https://docs.unity3d.com/560/Documentation/Manual/StandardShaderMaterialParameterDetail.html) leftovers. These are normal maps without diffuse textures. I am searching for a way to use them (see this [BlenderArtists thread](https://blenderartists.org/t/detail-maps-how-to-apply-a-second-normal-map/1653265)), but for now I just plug a `Transparent BSDF` and forget about them.

<img width="778" height="592" alt="14_detailmap" src="https://github.com/user-attachments/assets/b8f27174-17d9-4e1c-a266-99312dfd6a03" />

6. Check for **materials that should be transparent but are opaque**. In this example scene the GP7 gas mask does not have transparent glass. In this case go to the glass material and change the central node from "EFT_Shader_DGN" to "EFT_Shader_Hair".
<img width="1705" height="886" alt="image" src="https://github.com/user-attachments/assets/8127991d-1a1b-41c5-80f9-27d10e3c074a" />

NOTE : There is no way to detect which material is transparent and which is not, it's basically hardcoded in the [tarkdata.py](https://github.com/SoyuzKerman/Tark-to-Blend/blob/main/tarkdata.py) file. I added every texture name I could find in the trader scenes, but you can also add yours in the **TRANSPARENT_NAMES** list if needed.

7. Do the same for **emissive** materials, for the same reasons they might not be detected correctly.

8. Add the lights to the scene. The EFT lights are quite saturated, so using the **Blackbody** colors is not necessarily the closest to the game lighting. I also like to add a cube with a **Volume scatter** to make the light rays visible.

### Merge data (optional)

For big maps like *Factory*, the scene in contained in different <samp>level</samp> files. For performance reasons, it is more efficient to open each <samp>level</samp> file in separated <samp>blend</samp> files. Once the material setup is complete for each file, the sub-scenes can all be appended to a single, final <samp>blend</samp> file.

In that case, the custom node groups, as well as some textures and materials, will have duplicate versions of themselves. In the *Tark to Blend* panel, click `Merge duplicate data` to remove the duplicates and replace them with a single version of the node group/material/texture.

### Result

Here is an example of a final result :
<img width="1920" height="1080" alt="scene_ragman_render_eevee" src="https://github.com/user-attachments/assets/c3ff9c83-bd34-4ea0-b0dd-c2a52f183f21" />



