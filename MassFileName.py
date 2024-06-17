
import os, sys, os.path

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
        ret_arr.append((ftemp, etemp))

    return ret_arr

if __name__ == "__main__":
    pass
