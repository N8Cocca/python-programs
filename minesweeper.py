import random
grid = int(input("How big is the grid: ")) +2
field = []

for i in range(0,grid):
    size = [0]*grid
    field.append(size)
    
def check(row, col):
    value = 0
    if field[row][col] == '\u00B1':
        return '\u00B1'
    else:
        for i in range(-1, 2, 2):
            try:
                if field[row][col+i] == '\u00B1':
                    value += 1
                if field[row+i][col] == '\u00B1':
                    value += 1
                if field[row+i][col+i] == '\u00B1':
                    value +=1
                if field[row+i][col-i] == '\u00B1':
                    value += 1
            except:
                pass
        return value
    
for i in range(0, int((grid**2)/10)):
    bombRow = random.randint(1, grid-2)
    bombCol = random.randint(1, grid-2)
    field[bombRow][bombCol] = '\u00B1'

for i in range(0, len(field)):
    for ii in range(0, len(field[0])):
        field[i][ii] = check(i, ii)

for i in range(1, grid-1):
    print(*field[i][1:grid-1], sep='   ')

input("")
