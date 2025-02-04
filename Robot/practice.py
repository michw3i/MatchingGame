from Robot.graphics import *

'''
Returns the row and the column of the robot (in that order, separated by a comma)
'''


def getRobotPosition():
    row = getRobotRow()
    column = getRobotColumn()
    return row, column


'''
TODO - Returns the row of the robot (use getRobotPosition() function)
'''


def getRobotRow():
    for j in range(len(grid)):
        for i in range(len(grid[j])):
            if grid[j][i] == 1:
                return j


'''
TODO - Returns the column of the robot (use getRobotPosition() function)
'''


def getRobotColumn():
    for j in range(len(grid)):
        for i in range(len(grid[j])):
            if grid[j][i] == 1:
                return i


'''
TODO - Make the robot turn 90 degrees to the right by changing the variable facing
(Hint: you may need to add 'global facing' to your code)
'''


def turnRight():
    global facing
    if facing == 'R':
        facing = 'D'
    elif facing == 'D':
        facing = 'L'
    elif facing == 'L':
        facing = 'U'
    else:
        facing = 'R'



'''
TODO - Make the robot turn left 90 degrees by changing the variable facing
'''


def turnLeft():
    global facing
    if facing == 'L':
        facing = 'D'
    elif facing == 'D':
        facing = 'R'
    elif facing == 'R':
        facing = 'U'
    else:
        facing = 'L'


def goUp():
    global facing
    if facing == 'R' or facing == 'D' or facing == 'L':
        facing = 'U'


def goDown():
    global facing
    if facing == 'U'or facing == 'R' or facing == 'L':
        facing = 'D'


'''
TODO - Returns true if the robot can move forward, and false if the way is blocked (no more spaces to move)
'''


def canMoveForward(columnPos, rowPos):
    row = getRobotRow()
    col = getRobotColumn()
    if columnPos == 0 and facing == 'L':
        return False
    elif columnPos == len(grid[0])-1 and facing == 'R':
        return False
    if rowPos == len(grid)-1 and facing == 'D':
        return False
    elif rowPos == 0 and facing == 'U':
        return False
    return True


'''
TODO - Moves the robot forward in the direction he is facing. 
Prints "unable to move" if the way is blocked
'''


def moveForward():
    global grid
    rCol = getRobotColumn()
    rRow = getRobotRow()
    if canMoveForward(rCol, rRow):
        print(grid[rRow][rCol])
        print(facing)
        grid[rRow][rCol] = 0
        if facing == 'R':
            grid[rRow][rCol + 1] = 1
        elif facing == 'L':
            grid[rRow][rCol-1] = 1
        elif facing == 'U':
            grid[rRow-1][rCol] = 1
        elif facing == 'D':
            grid[rRow+1][rCol] = 1
    else:
        print("Robot cannot move.")


'''
Displays the current grid in the graphics window
'''


def displayGridSquares():
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            square = Rectangle(Point(20 * c, 20 * r), Point(20 * c + 20, 20 * r + 20)).draw(win)
            square.setFill('white')
    pos = getRobotPosition()
    row = pos[0]
    col = pos[1]
    goal = Rectangle(Point(0, 20), Point(20, 0)).draw(win)
    goal.setFill('lemon chiffon')
    robot = Polygon(Point(20 * r, 0), Point(20 * r, 20), Point(20 * r + 20, 10))
    if facing == 'R':
        robot = Polygon(Point(20 * col, 20 * row), Point(20 * col + 20, 20 * row + 10),
                        Point(20 * col, 20 * row + 20)).draw(win)
    elif facing == 'U':
        robot = Polygon(Point(20 * col + 10, 20 * row), Point(20 * col, 20 * row + 20),
                        Point(20 * col + 20, 20 * row + 20)).draw(win)
    elif facing == 'L':
        robot = Polygon(Point(20 * col + 20, 20 * row), Point(20 * col + 20, 20 * row + 20),
                        Point(20 * col, 20 * row + 10)).draw(win)
    elif facing == 'D':
        robot = Polygon(Point(20 * col, 20 * row), Point(20 * col + 20, 20 * row),
                        Point(20 * col + 10, 20 * row + 20)).draw(win)
    robot.setFill('grey23')
 


'''
Initializes the graphics and the list representing the grid
'''


def checkGoal():
    ro = getRobotRow()
    co = getRobotColumn()
    if ro == 0 and co == 0:
        return True


def setup():
    global win, grid, facing  # these variables can be accessed throughout program

    # grid is a list of lists. Each list corresponds to a row of squares.
    grid = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0]]

    facing = "R"  # R or L or U or D

    # figure out reasonable height and width of the graphics window
    gridHeight = 0
    if len(grid) * 20 < 350:
        gridHeight = 350
    else:
        gridHeight = len(grid) * 20

    gridWidth = 0
    if len(grid[0]) * 20 < 350:
        gridWidth = 350
    else:
        gridWidth = len(grid[0]) * 20

    # set up initial window
    win = GraphWin("Robot", gridWidth, gridHeight, autoflush=False)
    win.setBackground("misty rose")
    directionText = Text(Point(win.getWidth() / 2, win.getHeight() / 5 * 4),
                         "Press right arrow or 'r' to turn right 90 degrees\n" +
                         "Press left arrow or 'l' to turn left 90 degrees\n" +
                         "Press up arrow or 'u' to move forward 1 space\n" +
                         "Press 's' to stop")
    directionText.setFill("grey23")
    directionText.draw(win)


'''
The driver of the program. Takes user input through keys
and manipulates the robot appropriately.
'''


def main():
    print("Your goal is to reach the golden square")
    global facing
    setup()
    facing = "R"
    notOver = True
    print(getRobotPosition())
    while notOver:
        displayGridSquares()
        key = win.getKey()  # waits for user key press
        if key == 's':  # if user presses 's' key, closes window
            notOver = False
            win.close()
        elif key == 'r' or key == 'Right':
            turnRight()
        elif key == 'l' or key == 'Left':
            turnLeft()
        elif key == 'd' or key == 'Down':
            goDown()
        elif key == 'u' or key == 'Up':
            moveForward()
        if checkGoal():
            print("congrats")


if __name__ == '__main__':
    main()
