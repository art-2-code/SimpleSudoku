
# Online Python - IDE, Editor, Compiler, Interpreter
import sys

MainPuzzle = []
MainPuzzle += [[0,5,0,8,0,6,0,7,0]]
MainPuzzle += [[0,0,0,7,9,0,0,0,0]]
MainPuzzle += [[4,0,0,0,0,0,0,0,8]]
MainPuzzle += [[9,0,0,6,0,4,0,8,1]]
MainPuzzle += [[0,1,0,0,0,0,0,6,0]]
MainPuzzle += [[6,3,0,5,0,7,0,0,9]]
MainPuzzle += [[1,0,0,0,0,0,0,0,3]]
MainPuzzle += [[0,0,0,0,6,5,0,0,0]]
MainPuzzle += [[0,9,0,4,0,2,0,1,0]]

WorkingGrid = MainPuzzle #The working grid - this allows us to always keep a copy of the original puzzle
MaskedGrid = []          #contains 0s for places that are blocked, 1 for free places
NewFillGrid = []         #contains 1s for places that a digit can be added, others are 0

def MaskFor(Digit):
    #We will make our masked grid such that we eliminate everywhere the given digit can't be
    #The MaskedGrid will contain 1s where the digit can be and 0s where it can't be.
    global MaskedGrid
    MaskedGrid = []
    
    #mark off rows
    for Line in WorkingGrid:
        if Digit in Line:
            MaskedGrid += [[0,0,0,0,0,0,0,0,0]]
        else:
            MaskedRow = []
            for Item in Line:
                if Item != 0:
                    MaskedRow += [0]
                else:
                    MaskedRow += [1]
            MaskedGrid += [MaskedRow]
    #mark off columns
    for Column in range(9):
        for Row in range(9):
            if WorkingGrid[Row][Column] == Digit:
                for MaskRow in range(9):
                    MaskedGrid[MaskRow][Column] = 0
            else:
                if WorkingGrid[Row][Column] != 0:
                    MaskedGrid[Row][Column] = 0
    #mark off 3x3 boxes
    for BoxY in range(3):
        for BoxX in range(3):
            for WorkRow in range(3):
                for WorkColumn in range(3):
                    if WorkingGrid[BoxY*3+WorkRow][BoxX*3+WorkColumn] == Digit:
                        #fill the BoxX
                        for FillRow in range(3):
                            for FillColumn in range(3):
                                MaskedGrid[BoxY*3+FillRow][BoxX*3+FillColumn] = 0
                    else:
                        if WorkingGrid[BoxY*3+WorkRow][BoxX*3+WorkColumn] != 0:
                            MaskedGrid[BoxY*3+WorkRow][BoxX*3+WorkColumn] = 0

def PlacesFor(Digit):
    global NewFillGrid
    
    print("We will determine new places for digit", Digit, ":")
    NewFillGrid = []
    for Line in range(9):
        NewFillGrid += [[0,0,0,0,0,0,0,0,0]]
    #check if rows give a new valid location
    LastMatchRow = -1
    LastMatchColumn = -1
    for Row in range(9):
        MatchCount = 0
        for Column in range(9):
            if MaskedGrid[Row][Column] == 1:
                LastMatchRow = Row
                LastMatchColumn = Column
                MatchCount += 1
        if MatchCount == 1:
            NewFillGrid[LastMatchRow][LastMatchColumn] = Digit
    for Column in range(9):
        MatchCount = 0
        for Row in range(9):
            if MaskedGrid[Row][Column] == 1:
                LastMatchRow = Row
                LastMatchColumn = Column
                MatchCount += 1
        if MatchCount == 1:
            NewFillGrid[LastMatchRow][LastMatchColumn] = Digit
    for BoxY in range(3):
        for BoxX in range(3):
            MatchCount = 0
            for Row in range(3):
                for Column in range(3):
                    if MaskedGrid[BoxY*3+Row][BoxX*3+Column] == 1:
                        LastMatchRow = BoxY*3+Row
                        LastMatchColumn = BoxX*3+Column
                        MatchCount += 1
            if MatchCount == 1:
                NewFillGrid[LastMatchRow][LastMatchColumn] = Digit

def MergeWorkingGridAndNewFillGrid():
    global WorkingGrid
    global NewFillGrid
    
    for Row in range(9):
        for Column in range(9):
            WorkingGrid[Row][Column] += NewFillGrid[Row][Column]

def DisplayGrid(Grid):
    for Line in Grid:
        print(Line)

def RunRowsColumnsBoxesForDigit(Digit):
    global WorkingGrid
    global MaskedGrid
    global NewFillGrid

    #print("Mask for ",Digit,":")
    MaskFor(Digit)
    #DisplayGrid(MaskedGrid)
    print("Determine places for ",Digit,":")
    PlacesFor(Digit)
    DisplayGrid(NewFillGrid)
    #print("Merging places for ",Digit,":")
    MergeWorkingGridAndNewFillGrid()
    #DisplayGrid(WorkingGrid)

Continue = True
while Continue:
    print("Current Working Grid:")
    DisplayGrid(WorkingGrid)
    print("Action:?")
    print("1) Run rows, columns, and 3x3s for a given digit.")
    print("2) Run rows, columns, and 3x3s for all digits five times.")
    print("")
    print("x) Exit.")
    print("")
    Selection = input("Selection:")
    print("  (You selected ",Selection,".)")
    if Selection == 'x':
        print("Quitting.")
        Continue = False
        sys.exit()
    elif Selection == '1':
        Digit = int(input("Enter digit to run:"))
        RunRowsColumnsBoxesForDigit(Digit)
    elif Selection == '2':
        for Cycle in range(5):
            for Digit in range(9):
                RunRowsColumnsBoxesForDigit(Digit+1)
