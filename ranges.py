Python 3.10.8 (tags/v3.10.8:aaaf517, Oct 11 2022, 16:50:30) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> for i in range(1,5):
...     print(i)
... 
...     
1
2
3
4
>>> n = int(input('enter a number: '))
enter a number: 4
>>> for i in range(1, n):
...     print(1, 2, 3, n)
... 
...     
1 2 3 4
1 2 3 4
1 2 3 4
>>> import random
>>> numlist = []
>>> for i in range(1, 6):
...     x = random.randint(1, n)
...     numlist.append(x)
...     print(numlist)
... 
...     
[2]
[2, 3]
[2, 3, 1]
[2, 3, 1, 4]
[2, 3, 1, 4, 2]
