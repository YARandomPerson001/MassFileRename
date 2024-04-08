
import os, sys

Arguments = [ ]

Directory = "./"
SelectedWord = ""
ReplacmentWord = ""

Threads = 1

CommandList = [ ['-d', '-dir', '--d', '--dir'],
                ['-p', '-part', '--p', '--part'],
                ['-r', '-replace', '--r', '--replace'],
                ['-t', '-threads', '--t', '--threads'],
                ['-h', '-help', '--h', '--help'] ]

ValueList = [ ['-e', '-empty', '--e', '--empty'] ]

CommandDescription = [ "The directory the mass rename!",
                       "The word to replace.",
                       "The word to replace with.",
                       "The amont of thread to work with.",
                       "The command list!" ]

if __name__ == "__main__":
    if(len(sys.argv) > 1):
        # Loop though command line arguments.
        for index in range(1, len(sys.argv)):
            Flag = False
            
            for cmd in CommandList[4]:
                if sys.argv[index] == cmd:
                    print("\033[1;32m" + "|Command List|" + "\033[0m")
                    print("\033[37m" + str(CommandList[0]) +  "\t\033[1:37m" + str(CommandDescription[0]) + "\033[0m")
                    print("\033[37m" + str(CommandList[1]) +  "\t\033[1:37m" + str(CommandDescription[1]) + "\033[0m")
                    print("\033[37m" + str(CommandList[2]) +  "\t\033[1:37m" + str(CommandDescription[2]) + "\033[0m")
                    print("\033[37m" + str(CommandList[3]) +  "\t\033[1:37m" + str(CommandDescription[3]) + "\033[0m")
                    print("\033[37m" + str(CommandList[4]) +  "\t\033[1:37m" + str(CommandDescription[4]) + "\033[0m\n")
                    
                    Flag = True

            if not Flag: Arguments.append(sys.argv[index])
        
        # Loop though commands.
        for index in range(1, len(Arguments), 2):
            for cmd in CommandList[0]:
                if Arguments[index - 1] == cmd:
                    Directory = Arguments[index]
            for cmd in CommandList[1]:
                if Arguments[index - 1] == cmd:
                    SelectedWord = Arguments[index]
            for cmd in CommandList[2]:
                if Arguments[index - 1] == cmd:
                    ReplacmentWord = Arguments[index]
            for cmd in CommandList[3]:
                if Arguments[index - 1] == cmd:
                    Threads = Arguments[index]
                    
        # Make all empty flag to into empty strings
        for cmd in ValueList[0]:
            if ReplacmentWord == cmd:
                ReplacmentWord = ""
            if SelectedWord == cmd:
                SelectedWord = ""
            if Directory == cmd:
                Directory = "./"
                
    # Make sure threads make sense
    if int(Threads) < 1: Threads = 8  
        
        
    # Check if the user wants to proceed.
    print("\033[1;32m" + "|List of files to rename|" + "\033[0m")
    for f in os.scandir(Directory): print(f.path)
    
    # Get the value that are going to be used.
    print("\n\033[1;32m" + "|Values|" + "\033[0m")
    print("\033[37m" + "Word: " + "\033[0m" + SelectedWord)
    print("\033[37m" + "Replacement: " + "\033[0m" + ReplacmentWord)
    print("\033[37m" + "Directory: " + "\033[0m" + Directory)
    print("\033[37m" + "Threads: " + "\033[0m" + str(Threads))
    
    Proceed = input("Do you wish to proceed? (Yes) | (No): ")
    if(Proceed.lower() == "yes" or Proceed.lower() == 'y'):
        for f in os.scandir(Directory):
            if SelectedWord in f.path:
                Name = f.path.replace(SelectedWord, ReplacmentWord)
                os.rename(f.path, Name)
    else:
        exit(-1)
    