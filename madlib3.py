Python 3.10.8 (tags/v3.10.8:aaaf517, Oct 11 2022, 16:50:30) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
def getKeys(formatString):
    keyList = list()
    end = 0
    repetitions = formatString.count('{')
    for i in range(repetitions):
        start = formatString.find('{', end) + 1
...         end = formatString.find('}', start)
...         key = formatString[start : end]
...         keyList.append(key)
...     return set(keyList)
... 
>>> def addPick(cue, dictionary):
...     promptFormat = "Enter a specific example for {name}: "
...     prompt = promptFormat.format(name=cue)
...     response = input(prompt)
...     dictionary[cue] = response
... 
...     
>>> def getUserPicks(cues):
...     userPicks = dict()
...     for cue in cues:
...         addPick(cue, userPicks)
...     return userPicks
... 
>>> def tellStory(storyFormat):
...     cues = getKeys(storyFormat)
...     userPicks = getUserPicks(cues)
...     story = storyFormat.format(**userPicks)
...     print(story)
... 
>>> def main():
...     filename=input('Enter the filename: ')
...     originalStoryFormat=''
...     f=open(filename,'r')
...     for line in f:
...         originalStoryFormat=originalStoryFormat+line.strip()
... 
...     tellStory(originalStoryFormat)
...     input("Press Enter to end the program.")
... 
...     
>>> main()
Enter the filename: sample2.txt
My second output file!
Press Enter to end the program.
