grid = [['#','#','#','#','#','#','#','#'], 
        ['#','#','#','#','#','#','#','#'],
        ['#','#','#','#','#','#','#','#'], 
        ['#','#','#','#','#','#','#','#'],
        ['#','#','#','#','#','#','#','#'], 
        ['#','#','#','#','#','#','#','#'],
        ['#','#','#','#','#','#','#','#'], 
        ['#','#','#','#','#','#','#','#']]
enemyIndicies = {}

def enemyLines(shipCount):
    column = int(input(f"Enter column for ship {shipCount}: "))
    row = int(input(f"Enter row for ship {shipCount}: ")) 
    orientation = input("Enter Orientation (N,E,W,S): ")
    while(not calculateEnemyPlacement(shipCount, (8 * row)+ column , orientation)):
        print("Enter Valid Placement")
        row = int(input(f"Enter row for ship {shipCount}: "))
        column = int(input(f"Enter column for ship {shipCount}: "))
        orientation = input("Enter Orientation (N,E,W,S): ")
    

def calculateEnemyPlacement(ashipCount, beginIndex, aorientation):
    if(beginIndex < 0 or beginIndex > 63):
        return False
    global enemyIndicies
    fixedrow = beginIndex//8
    multiplier = 1
    list1 = []
    if(aorientation.lower() == "w" or aorientation.lower() == "n"):
        multiplier *= -1
    if(aorientation.lower() == "s" or aorientation.lower() == "n"):
        for i in range(ashipCount + 2):
            if(len(enemyIndicies) == 1):
                if(beginIndex in enemyIndicies[ashipCount - 1] or (beginIndex > 63 or beginIndex < 0)):
                    return False
            elif(len(enemyIndicies) == 2):
                if(beginIndex in enemyIndicies[ashipCount - 1] or beginIndex in enemyIndicies[ashipCount - 2] or (beginIndex > 63 or beginIndex < 0)):
                    return False
            list1.append(beginIndex)
            beginIndex += (8 * multiplier)
    else:
        for i in range(ashipCount + 2):
            row = beginIndex//8
            if(beginIndex in enemyIndicies or row != fixedrow or (beginIndex > 63 or beginIndex < 0)):
                return False
            list1.append(beginIndex)
            beginIndex += (1 * multiplier)
    enemyIndicies[ashipCount] = list1
    return True

numOfMiss = 0
numOfDestroyed = 0
def evaluateUserInput(beginIndex):
    global numOfMiss
    global enemyIndicies
    global numOfDestroyed
    global grid
    shipIndex = 0
    for n in enemyIndicies.values():
        if(beginIndex in n):
            n.remove(beginIndex)
            grid[beginIndex//8][beginIndex%8] = 'X'
            if(len(n) == 0):
                print(f"Ship {shipIndex + 1} Destroyed!")
                numOfDestroyed += 1
                print(f"{numOfDestroyed} ships destroyed")
            else:
                print("Hit!")
            return
        shipIndex += 1
    print("Miss!")
    grid[beginIndex//8][beginIndex%8] = 'O'
    numOfMiss += 1

def printGrid(agrid):
    for i in agrid:
        print(i)

for i in range(1,4):
    enemyLines(i)
        
while(numOfDestroyed < 3 and numOfMiss < 10):
    printGrid(grid)
    userColumn = int(input("Enter Column to attack: "))
    userRow= int(input("Enter Row to attack: "))
    evaluateUserInput(userColumn + userRow * 8)

if(numOfDestroyed >= 3):
    print("You Won!")
else:
    print("You Lost!")