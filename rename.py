import os
import shutil

#TODO:
#Add support for effect and voice folders
#Fix: crashes if you attempt to rename files to a slot that already exists in the same folder

def printHelp():
    print("SSBU Mod File Renamer v.1.1 by Ian Huff")
    print("Place the executable in the root of your SD card if it is not already.")
    print("This tool is intended to make the process of renaming files to change the skin slot that a mod replaces easier.")
    print("This tool can NOT make a mod work on a slot that it is otherwise incompatible with, i.e. moving a c00 Wario mod to c01.")
    print("The current version of this tool may struggle with Ice Climbers, Pokemon Trainer/Squirtle/Ivysaur/Charizard, and Pyra/Mythra due to the way some of their files are formatted.")
    print("\"Failures\" indicated by this tool should usually mean that the file does not exist and can usually be safely ignored.")
    print("For a list of character codenames, visit https://gamebanana.com/tools/6934")
    print("")


###data

#list of ALL fighter and boss codenames (INCLUDING DLC)
codeNames = ["mario", "donkey", "link", "samus", "samusd", "yoshi", "kirby", "fox", "pikachu", "luigi", "ness", "captain", "purin", "peach", "daisy", "koopa", "koopag", "ice_climber", "nana", "popo", "sheik", "zelda", "mariod", "pichu", "falco", "marth", "lucina", "younglink", "ganon", "mewtwo", "roy", "chrom", "gamewatch", "metaknight", "pit", "pitb", "szerosuit", "wario", "snake", "ike", "ptrainer", "pzenigame", "pfushigisou", "plizardon", "diddy", "lucas", "sonic", "dedede", "pikmin", "lucario", "robot", "toonlink", "wolf", "murabito", "rockman", "wiifit", "rosetta", "littlemac", "gekkouga", "miifighter", "miiswordsman", "miigunner", "palutena", "pacman", "reflet", "shulk", "koopajr", "duckhunt", "ryu", "ken", "cloud", "kamui", "bayonetta", "inkling", "ridley", "simon", "richter", "krool", "shizue", "gaogaen", "packun", "jack", "brave", "buddy", "dolly", "master", "tantan", "pickel", "edge", "eflame", "elight", "element", "demon", "trail", "crazyhand", "darz", "dracula", "dracula2", "galleom", "ganonboss", "kiila", "kiila_darz", "koopag", "lioleus", "marx", "mastercrazy", "masterhand"]

#list of DLC character code names
patchChars = ["packun", "jack", "brave", "buddy", "dolly", "master", "tantan", "pickel", "edge", "eflame", "eflame_only", "eflame_first", "elight", "elight_only", "elight_first", "element", "demon", "trail"]

#list of UI element IDs
elements = ["0", "1", "2", "3", "4", "5", "6", "7", "10", "12", "13"]


while True:

    ###input


    #mod name input
    modName = ""
    modExists = False
    while modExists != True:
        print("Enter the name of the folder containing the mod files (or enter \"help\" for more information, or \"exit\" to quit):")
        modName = input()
        modExists = os.path.exists("ultimate/mods/" + modName)
        if modName == "exit":
            print("Exiting...")
            exit()
        elif modName == "help":
            printHelp()
        elif modExists != True:
            print("Directory \"ultimate/mods/" + modName + "\" not found")

    #character name input
    charName = ""
    nameValid = False
    while nameValid != True:
        print("Enter the codename of the character the mod is for (or enter \"help\" for more information, or \"exit\" to quit):")
        charName = input()
        nameValid = (charName in codeNames)
        if charName == "exit":
            print("Exiting...")
            exit()
        elif charName == "help":
            printHelp()
        elif nameValid != True:
            print("Invalid codename")
            
        

    #old slotID input
    print("Enter the number of the mod's current slot (0-7, or \"exit\" to cancel and exit)")
    slotFrom = input()
    if slotFrom == "exit":
        print("Exiting...")
        exit()

    #new slotID input
    print("Enter the slot to rename files to (0-7, or \"delete\" to delete the files, or \"exit\" to cancel and exit)")
    slotTo = input()
    if slotTo == "exit":
        print("Exiting...")
        exit()
    
    
    
    
    ###fun stuff goes below here
    
    
    #fighter folder
    #file structure: fighter/charName/modelType/modelPart/c0X
    #where X = slotID
    
    modelTypes = os.listdir("ultimate/mods/" + modName + "/fighter/" + charName + "/") #get list of folders in fighter/charName
    
    for modelType in modelTypes:
    
        modelParts = os.listdir("ultimate/mods/" + modName + "/fighter/" + charName + "/" + modelType) #get a list of folders in there
        
        for modelPart in modelParts: #for each of THOSE folders (modelParts):
            
            oldFileName = "ultimate/mods/" + modName + "/fighter/" + charName + "/" + modelType + "/" + modelPart + "/c0" + slotFrom
            newFileName = "ultimate/mods/" + modName + "/fighter/" + charName + "/" + modelType + "/" + modelPart + "/c0" + slotTo
            
            fileExists = os.path.exists(oldFileName) #check if the folder oldFileName exists
    
            if fileExists:
                if slotTo == "delete":
                    print("Deleting " + oldFileName + " ...") #print a success message
                    shutil.rmtree(oldFileName) #delete it
                else:
                    print("Renaming " + oldFileName + " ...") #print a success message
                    os.rename(oldFileName, newFileName) #rename it
            else:
                print("Failed to locate " + oldFileName) #print a failure message
                
                
    #ui folder
    #file structure: ui/[replace or replace_patch]/chara/chara_Y/chara_Y_charName_0X.bntx
    #where X = slotID and Y = UI Element ID
    
    #check whether files are under replace or replace_patch
    if charName in patchChars:
        replace = "replace_patch"
    else:
        replace = "replace"
    
    for element in elements:
    
        oldFileName = "ultimate/mods/" + modName + "/ui/" + replace + "/chara/chara_" + element + "/chara_" + element + "_" + charName + "_0" + slotFrom + ".bntx"
        newFileName = "ultimate/mods/" + modName + "/ui/" + replace + "/chara/chara_" + element + "/chara_" + element + "_" + charName + "_0" + slotTo   + ".bntx"
        
        fileExists = os.path.exists(oldFileName) #check if the file oldFileName exists
        
        if fileExists:
            if slotTo == "delete":
                print("Deleting " + oldFileName + " ...") #print a success message
                os.remove(oldFileName) #rename it
            else:
                print("Renaming " + oldFileName + " ...") #print a success message
                os.rename(oldFileName, newFileName) #delete it
        else:
            print("Failed to locate " + oldFileName) #print a failure message
            
    
    
    
    print("")