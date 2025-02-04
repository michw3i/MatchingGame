import random as r
import Variables as v
import pygame as p


class Hunter():
    WIDTH = HEIGHT = v.SQ_LENGTH
    RADIUS = v.SQ_LENGTH//2

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.color = 'orange'
        self.energy = v.INITIAL_HUNTER_ENERGY

    def draw(self, screen):
        image = p.image.load('hunter.png')
        image = p.transform.scale(image, (15, 15))
        screen.blit(image, (self.x * Hunter.WIDTH + Hunter.WIDTH // 2, self.y * Hunter.WIDTH + Hunter.WIDTH // 2))

    def move(self):
        self.energy -= 1

        direction = r.choice(['up', 'down', 'left', 'right'])
        if direction == 'up':
            if self.y > 0:
                self.y -= 1
        elif direction == 'left':
            if self.x > 0:
                self.x -= 1
        elif direction == 'right':
            if self.x <v.NUM_OF_SQUARES - 1:
                self.x += 1
        elif direction == 'down':
            if self.y <v.NUM_OF_SQUARES - 1:
                self.y += 1

    def isAlive(self):
        if self.energy > 0:
            return True
        return False

    def update(self, wolfList):
        foundwolf = []
        if self.isAlive():
            for i in range(len(wolfList)):
                if wolfList[i].x == self.x and wolfList[i].y == self.y:
                    foundwolf.append(wolfList[i])

            if len(foundwolf) == 0:
                self.move()
            elif len(foundwolf) > 0:
                self.energy = self.energy + wolfList[0].energy
                foundwolf[0].energy = 0
                self.move()

        else:
            self.color = 'red'





