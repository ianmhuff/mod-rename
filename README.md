# mod-rename
A simple script that renames file folders for Super Smash Bros. Ultimate character skin mods


Setup is simple: download "rename.py" and save it on the root of your SD card.
Once downloaded, run it and follow the instructions as prompted.


To use this program you'll need to enter a few things:

### 1. The name of the mod folder that the mod is in
This varies per mod. It may be helpful to rename some of these folders to make them easier to remember.

### 2. The code name for the character that the mod applies to
For axample, for a Banjo skin, enter "buddy"
A full list of these code names can be found here: https://gamebanana.com/tools/6934

### 3. The slot that the mod is currently applied to
For example, for a mod on c03, enter "3".
Note that this prompt does not check for valid input. Any string entered for this prompt will be looked for as though it is valid. For example, if you enter "asdf" here, the program will look for folders named "c0asdf".

### 4. The slot that the mod should be moved to
For example, to apply the skin to c06, enter "6".
Note that this prompt does not check for valid input. Any string entered for this prompt will be appended onto the folder names. For example, if you enter "asdf" here, the folders will be renamed to "c0asdf".

### Notes
You will be prompted for each of these four items individually. Simply type each into the command prompt window and press Enter to continue on to the next.

If any errors are encountered, such as the folder not being found, or an invalid codename being entered, you will be prompted to try again, rather than continuing to the next prompt.

After all four items are entered, the program will attempt to rename any folders containing skins for the slot specified. Every attempt to rename a file will be accompanied by a message in the command promt window, indicating whether the file was successfully found and renamed.

"Failures" usually indicate that the file in question does not exist in the mod files. This behavior is expected and intended.
