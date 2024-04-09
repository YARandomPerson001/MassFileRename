
import os, sys, os.path

Arguments = [ ]

Directory = "./"
SelectedWord = ""
ReplacmentWord = ""

AutoYes = False

CommandList = [ ['-d', '-dir', '--d', '--dir'],
                ['-p', '-part', '--p', '--part'],
                ['-r', '-replace', '--r', '--replace'],
                ['-h', '-help', '--h', '--help'],
                ['-e', '-empty', '--e', '--empty'], 
                ['-y', '-yes', '--y', '--yes'] ] 

CommandDescription = [ "The directory the mass rename!",
                       "The word to replace.",
                       "The word to replace with.",
                       "The command list!",
                       "Set to empty text.",
                       "For a automatic yes."]

if __name__ == "__main__":
    # Loop though commands.
    for index in range(2, len(sys.argv), 2):
        for cmd in CommandList[0]:
            if sys.argv[index - 1] == cmd:
                Directory = sys.argv[index]
        for cmd in CommandList[1]:
            if sys.argv[index - 1] == cmd:
                SelectedWord = sys.argv[index]
        for cmd in CommandList[2]:
            if sys.argv[index - 1] == cmd:
                ReplacmentWord = sys.argv[index]

    # Loop for yes
    for arg in sys.argv:
        for cmd in CommandList[5]:
            if arg == cmd:
                AutoYes = True
    
    # Loop though help commands.
    for arg in sys.argv:
        for cmd in CommandList[3]:
            if arg == cmd:
                print("\033[1;32m" + "|Command List|" + "\033[0;37m")
                for index in range(0, len(CommandList)):
                    print(str(CommandList[index]) + " | " + str(CommandDescription[index]))
                print("\033[0m")
    
    # Make all empty flag to into empty strings
    for cmd in CommandList[4]:
        if ReplacmentWord == cmd:
            ReplacmentWord = ""
        if SelectedWord == cmd:
            SelectedWord = ""
        if Directory == cmd:
            Directory = "./"
    
    # Check if the user wants to proceed.
    print("\033[1;32m" + "|List of files to rename|" + "\033[0m")
    for f in os.scandir(Directory): print(f.name)
    
    # Get the value that are going to be used.
    print("\n\033[1;32m" + "|Values|" + "\033[0m")
    print("\033[37m" + "Word: " + "\033[0m" + SelectedWord)
    print("\033[37m" + "Replacement: " + "\033[0m" + ReplacmentWord)
    print("\033[37m" + "Directory: " + "\033[0m" + Directory + "\n")
    
    Proceed = ""
    
    if not AutoYes:
        Proceed = input("Do you wish to proceed? (Yes) | (No): ")
        
    if(Proceed.lower() == "yes" or Proceed.lower() == 'y' or AutoYes):
        for f in os.scandir(Directory):
            if SelectedWord in f.path:
                Name = f.name.replace(SelectedWord, ReplacmentWord)
                FullName = str(Directory) + "/" + Name
                
                if not os.path.isfile(FullName):
                    os.rename(f.path, FullName)
    else:
        exit(-1)
    