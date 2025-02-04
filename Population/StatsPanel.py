import pygame as p
import Variables as v


def draw(screen, sheepList, count, number, wolfList, alivewolf, deadwolf, alivehunter, deadhunter):
    p.font.init()
    font = p.font.SysFont('Comic Sans MS', 15)  # load any font from computer
    text = font.render("number of sheep: " + str(len(sheepList)), True, 'black')  # create the text to blit
    screen.blit(text, (530, 30))

    p.font.init()
    font = p.font.SysFont('Comic Sans MS', 15)  # load any font from computer
    text = font.render("number of alive sheep: " + str(count), True, 'black')  # create the text to blit
    screen.blit(text, (530, 60))

    p.font.init()
    font = p.font.SysFont('Comic Sans MS', 15)  # load any font from computer
    text = font.render("number of dead sheep: " + str(number), True, 'black')  # create the text to blit
    screen.blit(text, (530, 90))

    p.font.init()
    font = p.font.SysFont('Comic Sans MS', 15)  # load any font from computer
    text = font.render("number of wolf: " + str(len(wolfList)), True, 'black')  # create the text to blit
    screen.blit(text, (530, 120))

    p.font.init()
    font = p.font.SysFont('Comic Sans MS', 15)  # load any font from computer
    text = font.render("number of alive wolf: " + str(alivewolf), True, 'black')  # create the text to blit
    screen.blit(text, (530, 150))

    p.font.init()
    font = p.font.SysFont('Comic Sans MS', 15)  # load any font from computer
    text = font.render("number of dead wolf: " + str(deadwolf), True, 'black')  # create the text to blit
    screen.blit(text, (530, 180))

    p.font.init()
    font = p.font.SysFont('Comic Sans MS', 15)  # load any font from computer
    text = font.render("fps: " + str(v.MAX_FPS), True, 'black')  # create the text to blit
    screen.blit(text, (530, 270))

    p.font.init()
    font = p.font.SysFont('Comic Sans MS', 15)  # load any font from computer
    text = font.render("number of alive hunters: " + str(alivehunter), True, 'black')  # create the text to blit
    screen.blit(text, (530, 210))

    p.font.init()
    font = p.font.SysFont('Comic Sans MS', 15)  # load any font from computer
    text = font.render("number of dead hunters: " + str(deadhunter), True, 'black')  # create the text to blit
    screen.blit(text, (530, 240))


