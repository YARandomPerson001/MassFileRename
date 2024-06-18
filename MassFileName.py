
import os, re, sys, os.path

def GetFileName(Directory:str):
    arr = os.listdir(Directory)
    ret_arr:list = [ ]
    
    for f in arr:
        ftemp = ''
        etemp = ''

        flag = False

        # Get Name
        for i in range(0, len(f)):
            if i > 0:
                if f[i] == '.':
                    break
                else:
                    ftemp += str(f[i])
            else:
                ftemp = str(f[i])

        # Get extension
        for i in range(0, len(f)):
            if flag:
                etemp += str(f[i])

            if i > 0:
                if f[i] == '.':
                    flag = True
        
        flag = False
        ret_arr.append((ftemp, etemp, ftemp, etemp))

    return ret_arr

def RenameFile(Files:list, Word:str, Replacement:str):
    arr:list = [ ]

    for l in Files:
        temp = l[0].replace(str(Word),str(Replacement), 1)
        arr.append((temp, str(l[1]), l[2], l[3]))

    return arr

def RenameExtension(Files:list, Word:str, Replacement:str):
    arr:list = [ ]

    for l in Files:
        temp = l[1].replace(str(Word),str(Replacement), 1)
        arr.append((l[0], str(temp), l[2], l[3]))

    return arr

if __name__ == "__main__":
    print(str(RenameExtension(GetFileName("./"), "m", "")))
