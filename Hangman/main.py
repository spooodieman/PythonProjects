grid = [["_","_","_","_","_","_","_"],
        ["|"," "," "," "," "," ","|"],
        ["|"," "," "," "," "," "," "],
        ["|"," "," "," "," "," "," "," "],
        ["|"," "," "," "," "," "," "],
        ["|"," "," "," "," "," "," "," "],
        ["|","_","_","_","_","_","_","_"]]

usedLetters = []
numOfErrors = 0
numOfCorrect = 0

yIndex = [2,3,3,3,4,5,5]
xIndex = [6,6,5,7,6,5,7]

def printGrid(aGrid):
    for i in aGrid:
        for s in i:
            print(s, end="")
        print()

charArr = []

def inputWord():
    word = input("Enter the word: ")
    finalword = ""
    for i in word:
        if i != " ":
            finalword += i
    global charArr
    for i in range(len(finalword)):
        charArr.append(finalword[i])
inputWord()

gameinput = []
for i in range(len(charArr)):
    gameinput.append('_')

def printGameInput(gameInput):
    for i in gameInput:
        print(i,end= "")
    print()

def revealWords(inputLetter):
    global gameinput
    global numOfErrors
    global numOfCorrect
    global usedLetters
    if(inputLetter.lower() in charArr or inputLetter.upper() in charArr):
        for i in range(len(charArr)):
            if charArr[i].lower() == inputLetter.lower():
                gameinput[i] = charArr[i]
                numOfCorrect+= 1
    else:
        numOfErrors+= 1
        if(numOfErrors == 1):
            grid[yIndex[numOfErrors-1]][xIndex[numOfErrors-1]] = "O"
        elif(numOfErrors == 2 or numOfErrors == 5):
            grid[yIndex[numOfErrors-1]][xIndex[numOfErrors-1]] = "|"
        elif(numOfErrors == 3 or numOfErrors == 6):
            grid[yIndex[numOfErrors-1]][xIndex[numOfErrors-1]] = "/"
        else:
            grid[yIndex[numOfErrors-1]][xIndex[numOfErrors-1]] = "\ "
    usedLetters.append(inputLetter.lower())

while(numOfCorrect < len(charArr) and numOfErrors < 7):
    printGrid(grid)
    print(f"Used Letters: {usedLetters}")
    printGameInput(gameinput)
    userInputLetter = input("Enter letter: ")
    while(len(userInputLetter)!= 1 or userInputLetter.lower() in usedLetters or not userInputLetter.isalpha()):
        userInputLetter = input("Enter again: ")
    revealWords(userInputLetter)
printGrid(grid)
print(f"Used Letters: {usedLetters}")
printGameInput(gameinput)
if(numOfErrors == 7):
    print("You lose")
else:
    print("You win")