import math, random
from Robot.graphics import *
NUM_OF_PAIRS = 4
DIMENSION = math.ceil(math.sqrt(NUM_OF_PAIRS*2))   # number of rows and columns
SQ_SIZE = 600//DIMENSION


def setup():
    # algorithm to populate and randomize list of matching numbers
    numbers = []  # start with blank list
    for i in range(NUM_OF_PAIRS):  # repeat 8 times
        numbers.append(i + 1)
        numbers.append(i + 1)  # append the same value twice
    random.shuffle(numbers)  # randomize the list (scramble the pairs)
    # print(numbers)

    # next, write algorithm to make a 2D list from the 1D scrambled list above
    grid = []
    for row in range(DIMENSION):   # for each row
        grid.append([])   # create a blank row
        for col in range(DIMENSION):   # for each number in the row
            if len(numbers) != 0:   # if numbers list is not empty
                grid[row].append(numbers.pop(0))   # append a number AND remove it from numbers list
            else:   # once we run out of numbers
                grid[row].append(0)   # 0 is our placeholder

    # open graphics window
    win = GraphWin("Matching Game", 600, 600, autoflush=False)
    win.setBackground('white')
    return win, grid


def drawSquares(win, grid):
    for row in range(len(grid)):
        for col in range(len(grid[0])):

            square = Rectangle(Point(col * SQ_SIZE, row * SQ_SIZE), Point(col * SQ_SIZE + SQ_SIZE, row * SQ_SIZE + SQ_SIZE)).draw(win)
            if grid[row][col] > 0:
                square.setFill('white')
            else:
                if grid[row][col] == -1:
                    square.setFill('mistyrose')
                elif grid[row][col] == -2:
                    square.setFill('lemon chiffon')
                elif grid[row][col] == -3:
                    square.setFill('lightcyan')
                else:
                    square.setFill('lavender')
                label = Text(Point(col*SQ_SIZE+SQ_SIZE/2, row*SQ_SIZE+SQ_SIZE/2), str(grid[row][col])).draw(win)
            if grid[row][col] == 0:
                square.setFill('black')

    if player1Turn:
        label1 = Text(Point(300, 250), "player 1 ").draw(win)
    else:
        label2 = Text(Point(300, 250), "player 2 ").draw(win)


def main():
    global player1Turn
    player1Turn = True
    win, grid = setup()   # setup function returns the window and the grid list
    drawSquares(win, grid)

    cardsSelected = 0   # number of cards clicked each turn (0, 1, 2, loop)
    matchesFound = 0  # total number of matches found, used to end the game
    card1 = (-1, -1)   # this is a tuple, representing the first card clicked
    card2 = (-1, -1)   # second card clicked, (-1, -1) is a placeholder
    # While a turn is in progress, these will be (col, row) of click

    gameOver = False
    while not gameOver:
        print(grid)
        click = win.getMouse()   # save the location of the click
        key = win.checkKey()  # temporary ending the game
        col = int(click.getX()/SQ_SIZE)
        row = int(click.getY()/SQ_SIZE)
        # print((col, row))
        drawSquares(win, grid)
        if cardsSelected == 2:   # end of a turn, reset the cards
            cardsSelected = 0
            if grid[card1[1]][card1[0]] != grid[card2[1]][card2[0]]:
                grid[card1[1]][card1[0]] *= -1  # resetting the value to positive, flipping the card
                grid[card2[1]][card2[0]] *= -1
                drawSquares(win, grid)
            card1 = (-1, -1)
            card2 = (-1, -1)
            player1Turn = not player1Turn
        else:   # during a turn
            if grid[row][col] > 0:   # click on card, not on placeholder or a previous match
                grid[row][col] *= -1   # reveal the card
                drawSquares(win, grid)
                if cardsSelected == 0:   # selecting first card
                    card1 = (col, row)
                elif cardsSelected == 1:   # selecting second card
                    card2 = (col, row)
                cardsSelected += 1
                print(card1, card2)
                if cardsSelected == 2:  # check for matching cards
                    if grid[card1[1]][card1[0]] == grid[card2[1]][card2[0]]:
                        matchesFound += 1  # a match has been found
                        print("A match has been found")
                        cardsSelected = 0  # reset
                        card1 = (-1, -1)  # reset
                        card2 = (-1, -1)  # reset
                        if matchesFound == NUM_OF_PAIRS:  # if all matches found
                            ending = Text(Point(300, 350), "want to play again? y/n ").draw(win)
                            key = win.getKey()
                            if key == 'n':
                                gameOver = True  # game is over
                            elif key == 'y':
                                cardsSelected = 0
                                matchesFound = 0
                                card1 = (-1, -1)
                                card2 = (-1, -1)
                                # win, grid = setup()  # choice 1
                                # drawSquares(win, grid)
                                for row in range(len(grid)):  # choice 2
                                    for col in range(len(grid[0])):
                                        grid[row][col] *= -1


if __name__ == '__main__':
    main()
