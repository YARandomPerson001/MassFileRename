
import os, sys

Arguments = [ ]

CommandList = [ ['-d', '-dir', '--d', '--dir'],
                ['-p', '-part', '--p', '--part'],
                ['-r', '-replace', '--r', '--replace'],
                ['-h', '-help', '--h', '--help'] ]

CommandDescription = [ "The path the mass rename!",
                       "The word to replace.",
                       "The word to replace with."
                       "The command list!" ]

if __name__ == "__main__":
    # Loop though command line arguments.
    for index in range(1, len(sys.argv)):
        Flag = False
        
        for cmd in CommandList[3]:
            if sys.argv[index] == cmd:
                
                ## Todo: Print Command List
                
                Flag = True

        if not Flag: Arguments.append(sys.argv[index])
        
    print(len(Arguments))
    pass
