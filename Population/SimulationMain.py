import pygame as p
import Variables as v
import Wolf
import Sheep
import Grass
import random as r
import StatsPanel
import Hunter


def setup():
    global screen, clock
    p.init()
    WIDTH = HEIGHT = v.SQ_LENGTH*v.NUM_OF_SQUARES
    screen = p.display.set_mode((800, 500))
    clock = p.time.Clock()


def main():
    setup()
    p.display.set_caption("Wolf and Sheep Population Simulation")
    clock = p.time.Clock()
    hunterList = spawnHunter(v.NUM_OF_HUNTER)
    grassList = createGrass()
    sheepList = spawnSheep(v.NUM_OF_SHEEP)
    wolfList = spawnWolf(v.NUM_OF_WOLF)
    done = False
    while not done:
        screen.fill((0, 0, 0))
        for event in p.event.get():
            if event.type == p.QUIT:
                done = True

            if event.type == p.KEYDOWN:
                if event.key == p.K_q:
                    done = True

            if event.type == p.KEYDOWN:
                if event.key == p.K_s:  # spawn 1 new sheep if we press the S key
                    sheepList.extend(spawnSheep(1))
        statistics(sheepList, wolfList, hunterList)
        # update grass, sheep wolves first
        for row in grassList:
            for grassSquare in row:
                grassSquare.update()
        for s in sheepList:
            s.update(grassList[s.x][s.y])  # pass the grassSquare underneath the sheep
        for w in wolfList:
            w.update(sheepList)
        for h in hunterList:
            h.update(wolfList)
        # then, draw everything
        for row in grassList:
            for grassSquare in row:
                grassSquare.draw(screen)
        for h in hunterList:
            h.draw(screen)
        for w in wolfList:
            w.draw(screen)
        for s in sheepList:
            s.draw(screen)
        p.display.flip()
        clock.tick(v.MAX_FPS)
    p.quit()


def spawnSheep(num):
    sheepList = []  # 1-D list of sheep objects
    for i in range(num):
        s = Sheep.Sheep(r.randint(0, v.NUM_OF_SQUARES-1),
                        r.randint(0, v.NUM_OF_SQUARES-1))  # make a sheep object
        sheepList.append(s)  # append the sheep to the list
    return sheepList


def spawnWolf(num):
    wolfList = []
    for i in range(num):
        w = Wolf.Wolf(r.randint(0, v.NUM_OF_SQUARES-1), r.randint(0, v.NUM_OF_SQUARES-1))
        wolfList.append(w)
    return wolfList


def spawnHunter(num):
    hunterList = []
    for i in range(num):
        h = Hunter.Hunter(r.randint(0, v.NUM_OF_SQUARES-1), r.randint(0, v.NUM_OF_SQUARES-1))
        hunterList.append(h)
    return hunterList


def createGrass():
    grassList = []  # 2-D list of grass squares
    for i in range(v.NUM_OF_SQUARES):
        grassRow = []
        for j in range(v.NUM_OF_SQUARES):
            g = Grass.Grass(i, j)
            grassRow.append(g)
        grassList.append(grassRow)
    return grassList


def numberOfAliveSheeps(sheepList):
    count = 0
    for i in range(len(sheepList)):
        if sheepList[i].energy >0:
            count += 1

    return count


def numberOfAliveWolf(wolfList):
    hi = 0
    for i in range(len(wolfList)):
        if wolfList[i].energy > 0:
            hi += 1

    return hi


def numberOfAliveHunter(hunterList):
    ok = 0
    for i in range(len(hunterList)):
        if hunterList[i].energy > 0:
            ok += 1

    return ok


def numberOfDeadWolf(wolfList):
    no = 0
    for i in range(len(wolfList)):
        if wolfList[i].energy == 0:
            no += 1
    return no


def numberOfDeadSheeps(sheepList):
    number = 0
    for i in range(len(sheepList)):
        if sheepList[i].energy == 0:
            number += 1
    return number


def numberOfDeadHunter(hunterList):
    so = 0
    for i in range(len(hunterList)):
        if hunterList[i].energy == 0:
            so += 1
    return so


def statistics(sheepList, wolfList, hunterList):
    p.draw.rect(screen, 'beige', (500, 0, 700, 500))
    clock.tick(v.MAX_FPS)
    deadhunter = numberOfDeadHunter(hunterList)
    alivehunter = numberOfAliveHunter(hunterList)
    deadwolf = numberOfDeadWolf(wolfList)
    alivewolf = numberOfAliveWolf(wolfList)
    deadsheep = numberOfDeadSheeps(sheepList)
    alivesheep = numberOfAliveSheeps(sheepList)
    StatsPanel.draw(screen, sheepList, alivesheep, deadsheep, wolfList, alivewolf, deadwolf, alivehunter, deadhunter)


if __name__ == '__main__':
    main()
