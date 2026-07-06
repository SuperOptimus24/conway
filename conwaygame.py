import random
import time


screenlengthx = 15
screenlengthy = 20

grid = []
temprow = []

#create screen

for columns in range(screenlengthx):
    for row in range(screenlengthy):
        temprow.append(random.randint(0,1))
    
    grid.append(temprow.copy())
    temprow.clear()

futuregrid = [row.copy() for row in grid]
#print screen
    
def printgrid():
    print("New: ")
    for i in range(len(grid)):
        print(futuregrid[i])
        i += 1

printgrid()

#input coords

#checkx = int(input("X coord:"))
#checky = int(input("Y coord:"))

#check how many cells are alive around input cell

def checkcell(x,y):

    tempcellcount = 0

    if y+1 < len(grid):
        tempcellcount += grid[y + 1][x]
    if y-1 >= 0:
        tempcellcount += grid[y-1][x]
    if x+1 < len(grid[y]):
        tempcellcount += grid[y][x+1]
    if x-1 >= 0:
        tempcellcount += grid[y][x-1]

    return tempcellcount

def setcell(x, y, status):
    futuregrid[y].pop(x)
    futuregrid[y].insert(x, status)


#print("Coordinate location: " + str(checkx) + ", " + str(checky))
#print("Cells alive around it: " + str(checkcell(checkx, checky)))

def cellsatwork(screen):

    futuregrid = [row.copy() for row in screen]

    for row in range(len(grid)):
        for columns in range(len(grid[0])):
            cellcount = checkcell(columns, row)
            if cellcount < 2:
                #if cell has less than two neighbors, cell dies
                setcell(columns, row, 0)
            elif cellcount > 3:
                #if cell has more than 3 neighbors, dies
                setcell(columns, row, 0)
            elif screen[row][columns] == 0 and cellcount == 3:
                #if cell is dead and neighbors are three, comes to life
                setcell(columns, row, 1)


for i in range(5):
    time.sleep(3)
    cellsatwork(grid)
    printgrid()