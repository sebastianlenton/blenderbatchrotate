#!/bin/bash
# Script to batch Blender .blend files into .gifs
#by Sebastian Lenton
#requires blendBatchRotate.py (requires path to be entered below)

#note: this does not handle cleaning of old folder, if the script is rerun (you will need to do this manually, or add to the script)

#path to Blender, and blendBatchRotate.py
#these must be set correctly in order for the script to work
#blender="/Applications/blender/blender.app/Contents/MacOS/blender"

blender="/Applications/blender/blender.app/Contents/MacOS/blender"
blendBatchRotate="./blendBatchRotate.py"

#if both arguments (input and output folder) are present:
if [ $# -eq 2 ]
then
	for f in "$1/"*.blend
	do
		printf "\nRunning script...\n"

		bfile=$(basename "$f")

		#run Blender in background mode, using the script
		blender -P "$blendBatchRotate" -b -- "$f" "$2"

		#imageMagick - make frames into gif
		#check files are there first
		filescount=`ls -1 "$2/$bfile/"*.png 2>/dev/null | wc -l`

		if [ $filescount == 0 ]; then
			printf "\nNo PNGs found, so cannot convert to .gif\n"
		else
			printf $filescount" files found. Converting to .gif...\n"
			convert -dispose background -delay 5 -loop 0 "$2/$bfile"/*.png "$2/$bfile"/"$bfile".gif
		fi
	done
else
	printf '\nTwo arguments are required: input and output paths. These are not present.\n\n'
	exit 1
fi

printf "\nbatchModels.sh has ended.\n"
