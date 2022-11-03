Python 3.10.8 (tags/v3.10.8:aaaf517, Oct 11 2022, 16:50:30) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> file = open("sample2.txt","r")
>>> Lines = file.readlines()
>>> for i in range(len(Lines)):
...     t = Lines[i]
...     print(t.upper())
... 
MY SECOND OUTPUT FILE!
>>> fname = input("Enter file name: ")
Enter file name: sample2.txt
>>> file = open(fname,"r")
>>> for i in range(len(Lines)):
...     t=Lines[i]
...     print(t.upper())
... 
...     
MY SECOND OUTPUT FILE!
>>> fname = input("Enter file name: ")
Enter file name: sample2.txt
>>> writeFileName = "UPPER" + fname
>>> file3 = open(writeFileName, "w")
>>> Lines = file.readlines()
>>> for i in range(len(Lines)):
...     t = Lines[i]
...     file3.write(t.upper())
... 
... 
...     
22
