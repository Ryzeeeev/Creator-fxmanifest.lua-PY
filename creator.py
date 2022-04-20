import os
from pathlib import Path
import time
import sys


def main():
    ryze_none_file = "false"
    print("[1] Create FxManifest.lua")
    print("[2] Create _resource.lua")
    print("")
    print("[3] Information ")
 
    solution = input("Choose your solution : ")


    if solution == "1": 
        os.system('cls')
        print("[Solution #1] Create FxManifest.lua")
        print("")
        print("")
        print("[Files] Use the file directory :")
        solution_fx = input("")

        for f in os.listdir(solution_fx):
                if f.find('fx') != -1 or f.find('manifest') != -1:
                    print(f, "| You have this file you want a (fix or edit)")
                    print("[1] Fix your fxmanifest.lua")
                    print("[2] Edit your fxmanifest.lua")
                    fixoredit = input("")
                    if fixoredit == "1":
                        os.system('cls')
                        path = solution_fx + "\\fxmanifest.lua"                        
                        fp = open(path, 'r+');
                        print(path)

                        fd = os.open(path, os.O_RDONLY)
                        n = 3500000
                        readBytes = os.read(fd, n).decode()
                        print(readBytes)
                        ryze_none_file = "true"    


    if (ryze_none_file == "false"):
            print("[No FxManifest.lua detected] Creator fxmanifest.lua by Ryze")
            print("")
            print("")

            for ryze in os.listdir(solution_fx):
                if os.path.isfile(solution_fx+"\\"+ryze):
                    print("yes")
                else:
                    print("no")


main()