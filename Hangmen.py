import random
import sys
 
GAME = [
    [" ","|","-","-","-","-"," "," "],
    [" ","|"," "," "," ","|"," "," "],
    [" ","|"," "," "," ","|"," "," "],
    [" ","|"," "," "," ","°"," "," "],
    [" ","|"," "," "," ","|"," "," "],
    [" ","|"," "," ","/","|","\\"," "],
    [" ","|"," "," "," ","|"," "," "],
    [" ","|"," "," "," ","|"," "," "],
    [" ","|"," "," ","/"," ","\\"," "],
    ["_","_","_"," "," "," "," "," "]
]
DEATHPOS = [["8","4"],["7","5"],["8","6"],["6","5"],["5","5"],["5","6"],["5","4"],["4","5"],["3","5"],True]
GessLetter = []
AllLeter = []

#Open and prepare the dictionary 
try : 
    f = open("doc.txt","r")
    p = []
    for s in f :
        s = s.rstrip()
        p.append(s)
except :
    print("Please make sure you have a readable doc.txt in the folder as this program and it is UTF-8 formated")
    sys.exit(1)


def updateScreen(word):
    #draw the game in the command prompt
    for col in GAME :
        print(*col)
    currentLetter(word)
    print("Used letter : ")
    print(*AllLeter)

def removeLife(pos):
    #place a X on a the specified space
    if pos != True : 
        x = int(pos[0])
        y = int(pos[1])
        GAME[x][y] = "X"
        return True
    else:
        return False

def currentLetter(word):
    #print the current advancement of the word
    output = []
    for letter in word :
        out = "_"
        for gessed in GessLetter :
            if letter == gessed :
                out = letter
        output.append(out)
    print(*output)

def LetterHasBeenUse(l):
    #verify if a letter as already been used by the user 
    for letter in AllLeter : 
        if l == letter :
            return True
    return False

def numberOfOccurence(l):
    #see the number of time the letter appear in the word
    n = 0 
    for letter in word:
        if l == letter:
            n+=1
    return n 

#Init
word = p[random.randint(0,len(p))]
print(word)
endgame = True
error = 0
win = 0 
updateScreen(word)

#Main loop
while(endgame):
    l = input(str(error + win) + " gess ? ")
    l = l.lower()
    if l != "" and not LetterHasBeenUse(l) and not len(l) > 1: #to be added : check for a char !int
        AllLeter.append(l)
        if l not in word :
            endgame = removeLife(DEATHPOS[error])
            error+=1
            updateScreen(word)
        else :
            GessLetter.append(l)
            win += numberOfOccurence(l)
            updateScreen(word)
            if(win >= len(word)-1):
                print(word)
                print("Your winner")#Did you get it ?
                sys.exit(0)
    if(not endgame):
        print("The correct word was : " + word)
        sys.exit(0)

