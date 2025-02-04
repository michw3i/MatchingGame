import math

import pygame as p
import Needle, Button, Statistics


def setup():
    global screen, clock
    p.init()
    screen = p.display.set_mode((900, 600))
    clock = p.time.Clock()


def main():

    setup()
    needles = []
    done = False
    global NumOfNeedles
    buttons = buttonPanel()
    LinesIncrement = 149
    TotalNeedles = 0
    CrossedNeedles = 0
    NeedleLen = 100
    AutoThrow = False
    while not done:
        for event in p.event.get():
            if event.type == p.QUIT:
                done = True
            if event.type == p.MOUSEBUTTONDOWN:
                click = p.mouse.get_pos()
                if buttons[0].box.collidepoint(click):
                    AutoThrow = True
                elif buttons[1].box.collidepoint(click):
                    AutoThrow = False
                elif buttons[2].box.collidepoint(click):
                    AutoThrow = False
                    TotalNeedles = 0
                    CrossedNeedles = 0
                    needles = []
        lines = draw_floorboard(LinesIncrement)
        for b in buttons:
            b.draw(screen)
        if AutoThrow:
            needle = Needle.Needle(NeedleLen)
            needles.append(needle)
            if needle.isSuccess(lines):
                CrossedNeedles += 1
            TotalNeedles += 1

        for needle in needles:
            needle.draw(screen)
        statistics(CrossedNeedles, TotalNeedles, LinesIncrement, NeedleLen)
        p.display.flip()
        clock.tick(7)
    p.quit()


def draw_floorboard(linesIncrement):
    x = 0
    y = 300
    lines = []
    for i in range(5):
        p.draw.rect(screen, 'plum1', (0, x, 600, y))  # draw dartboard panel
        x = x+200
        y = y + 100
        p.draw.rect(screen, 'black', (0, i * linesIncrement, 600, 1))
        lines.append(i * linesIncrement)
    return lines


def buttonPanel(): #Celina
    p.draw.rect(screen, 'khaki1', (0, 400, 700, 600))
    start = Button.Buttons(10, 500, 110, 'green', 'START')
    pause = Button.Buttons(145, 500, 110, 'yellow', 'PAUSE')
    reset = Button.Buttons(280, 500, 110, 'red', 'RESET')
    buttons = [start, pause, reset]
    return buttons


def statistics(Crossed, Total, Increment, Length): # Ethan
    p.draw.rect(screen, 'white', (600, 0, 900, 600))
    if Total > 0 and Crossed > 0:
        ExperProb = Crossed/Total
        PiEstimate = (2 * Length * Total) / (Increment * Crossed)
    else:
        ExperProb = 0
        PiEstimate = 0
    TheorProb = (2*Length)/(Increment*math.pi)
    Statistics.draw(screen, Total, Crossed, ExperProb, TheorProb, PiEstimate)


if __name__ == "__main__":
    main()
