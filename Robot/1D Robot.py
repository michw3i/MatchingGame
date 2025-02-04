from Robot.graphics import *


def setup():
    global grid, facing, win
    grid = [0, 0, 0, 0, 1, 0, 0]  # robot starts at index 2
    facing = "R"  # robot starts facing right, will eventually be "L" for left

    win = GraphWin("Robot", 400, 400)
    win.setBackground("green")
    directionText = Text(Point(win.getWidth()/2, win.getHeight()/5*4), "Robot")
    directionText.setFill("white")
    directionText.draw(win)


def displayGridSquares():
    for col in range(len(grid)):
        rectangle = Rectangle(Point(20*col, 0), Point(20*col+20, 20)).draw(win)
        rectangle.setFill("white")
    pos = getRobotColumn()  # robot's current position
    if facing == 'R':
        robot = Polygon(Point(20*pos, 0), Point(20*pos, 20), Point(20*pos+20, 10)).draw(win)
    elif facing == 'L':
        robot = Polygon(Point(20*pos, 20), Point(20*pos, 10), Point(20*pos+20, 20)).draw(win)


def consoleDisplay():
    for square in grid:
        if square == 1:   # location of robot
            print(facing, end=' ')
        else:
            print("0", end = ' ')
    print()  # newline


def turnAround():
    global facing  # changing the global variable
    if facing == 'R':
        facing = 'L'
    elif facing == 'L':
        facing = 'R'


def moveForward():
    # ask if the robot can move (not at the edge of the grid)
    # use direction to move the robot either left or right (edit grid)
    # to do this, we will define some helper functions: getRobotColumn(), canMove()
    global grid
    col = getRobotColumn()  # integer location of robot
    if canMove(col):
        grid[col] = 0  # delete the robot from current position
        if facing == 'R':
            grid[col + 1] = 1
        elif facing == 'L':
            grid[col - 1] = 1
    else:
        print("Robot can't move.")


def getRobotColumn():
    for i in range(len(grid)):
        if grid[i] == 1:
            return i


def canMove(currentPosition):
    if currentPosition == 0 and facing == 'L':
        return False
    elif currentPosition == len(grid)-1 and facing == 'R':
        return False
    return True


def main():
    setup()
    print(getRobotColumn())
    over = False
    while not over:
        consoleDisplay()
        displayGridSquares()
        key = win.getKey()
        # choice = input("Enter 't' to turn the robot, 'f' to move forward, or press 's' to stop")
        if key == 's':  # if user inputs 's'
            over = True  # the program will end
        elif key == 't':
            turnAround()
        elif key == 'f':
            moveForward()
        else:
            print("Invalid input, try again.")


if __name__ == '__main__':
    main()
