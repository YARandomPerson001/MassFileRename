
import os, sys

Arguments = [ ]

Directory = ""
SelectedWord = ""
ReplacmentWord = ""

CommandList = [ ['-d', '-dir', '--d', '--dir'],
                ['-p', '-part', '--p', '--part'],
                ['-r', '-replace', '--r', '--replace'],
                ['-h', '-help', '--h', '--help'] ]

ValueList = [ ['-e', '-empty', '--e', '--empty'] ]

CommandDescription = [ "The path the mass rename!",
                       "The word to replace.",
                       "The word to replace with."
                       "The command list!" ]

if __name__ == "__main__":
    if(len(sys.argv) > 1):
        # Loop though command line arguments.
        for index in range(1, len(sys.argv)):
            Flag = False
            
            for cmd in CommandList[3]:
                if sys.argv[index] == cmd:
                    
                    ## Todo: Print Command List
                    
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
                    
        # Make all empty flag to into empty strings
        for cmd in ValueList[0]:
            if ReplacmentWord == cmd:
                ReplacmentWord = ""
            if SelectedWord == cmd:
                SelectedWord = ""
            if Directory == cmd:
                Directory = ""
                
    