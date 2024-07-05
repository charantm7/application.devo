import sys 
import os.path
import string

fname = input("Enter the file path: ")
if not os.path.isfile(fname):
    print("file does not exist: ", fname)
    sys.exit(0)

infile = open(fname,"r")
filecontent = " "
for line in infile:
    for ch in line:
        if ch not in string.punctuation:
            filecontent += ch 
        else:
            filecontent +=" "

wordfreq = {}
wordlist = filecontent.split()
for word in wordlist:
    if word in wordfreq:
        wordfreq[word] += 1
    else:
        wordfreq[word] = 1
for word,frequency in wordfreq.items():
    print(word,"occurs",frequency,"times")

sortedword = sorted(wordfreq.items(), key=lambda x:x[1], reverse=True)
print(type(sortedword))*
print(sortedword)*
for i in range(10):
    print(f"sorted{sortedword[i][0]} occurs {sortedword[i][1]}")
