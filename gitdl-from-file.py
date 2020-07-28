import os
print(" ----------------------------- ")
print("| github downloader from file  |")
print("| created by darkness chieftain|")
print(" ----------------------------- ")

print("example of path for repos file = /home/user/dlfiles.txt")
filepath = input("please enter github repos file path = ")
file = open(filepath,"r")
lines = file.readlines()
linescount = len(lines)
i = 0
while(i<=linescount):
    os.popen("git clone " + lines[i] )
    i = i+1
