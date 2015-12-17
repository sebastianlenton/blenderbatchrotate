Blender gif batch script notes
By Sebastian Lenton

└(=^‥^=)┐

Below are instructions re the complete process:

PREPARING THE MODELS:

1. IMPORTANT: in your preferences, enable absolute paths (File > untick relative paths), or else there won't be any textures. Ensure this has been set when saving the OBJ into a .blend file.

2. Open initial.blend (consider temporarily setting this as your default blend file). Note, the only rendering settings set in the script are X and Y dimensions. Number of animation frames is also set within the script. Everything else is done as per settings in initial.blend. If you want to set consistent render settings, either set them in initial.blend or modify the script to set these.

3. Import your OBJ file.

4. Scale and rotate it to the correct size and orientation. Ensure the origin is set correctly. The mesh should fit within the camera viewport (when viewed via 0 key).

5. Ensure only one mesh is present (the OBJ). Do not set lamps and camera- this is done via the script. (But, you do not need to delete the lamp or camera either).

6. Save as .blend. IMPORTANT: ensure the model is saved in object mode (this is why the script wouldn't work the other day). I tried to set this via the script, but couldn't get it to work.



RUNNING THE SCRIPT:

1. Ensure correct path to Blender is set in batchModels.sh (see script for example- obv this path will be different for you).

Note, you cannot set an alias to Blender in your .profile file, unless you source your .profile in the script(?).

2. Ensure path to blendBatchRotate.py is set in batchModels.sh (see script for example- obv this path will be different for you).

3. Run the script as follows:

/path/to/batchModels.sh /path/to/input/blends /path/to/output

eg: /Users/sebastianlenton/Code/blender/batchModels.sh /Users/sebastianlenton/Desktop/blendermodels /Users/sebastianlenton/Desktop/output

The output folder will be created if it does not exist already.



MISC NOTES, CAVEATS ETC

- amount of colours are set in batchModels.sh. Anim frames and dimensions are set in blendBatchRotate.py. Maybe more arguments could be added to the script in future.

- everything else (eg render settings) should be set in the .blend files themselves- eg in initial.blend.

- the script has to create the camera (after deleting any camera present in the initial .blends). I tried leaving the camera in (set manually in the .blend), and for some reason the rotation was being set on the camera instead of the object. This could be a problem with certain meshes.

- the script creates the lighting (so that each model is lit the same)

- file deletion has to be done manually. This is important to note as, for example if you reduce the number of frames and re-run the script, the frames from the previous run will be baked into the resulting gif.

- do try to be as frugal as possible re colours and frames in .gif, as obv they get quite large!