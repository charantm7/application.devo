import sys
import os.path

fname = input("Enter the file path: ")
if not os.path.isfile(fname):
    print("File does not exist")
    sys.exit(0)

infile = open(fname,"r")
mylist = infile.readlines()
linelist = []

for line in mylist:
    linelist.append(line.strip())
linelist.sort()

outfile = open("sorted.txt","w")
for line in linelist:
    outfile.write(line+"\n")

outfile.close()
infile.close()

if os.path.isfile("sorted.txt"):
    print("The sorted.txt file has been created successfully")
    print("The sorted.txt has",len(linelist),'lines')
    print("The sorted.txt file contents:")

rdfile = open("sorted.txt","r")
for lines in rdfile:
    print(lines,end=" ")
