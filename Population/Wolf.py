import random as r
import Variables as v
import pygame as p


class Wolf():
    WIDTH = HEIGHT = v.SQ_LENGTH
    RADIUS = v.SQ_LENGTH//2

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.color = 'black'
        self.energy = v.INITIAL_WOLF_ENERGY

    def draw(self, screen):
        image = p.image.load('wolf.png')
        image = p.transform.scale(image, (13, 13))
        screen.blit(image, (self.x * Wolf.WIDTH + Wolf.WIDTH//2, self.y * Wolf.WIDTH + Wolf.WIDTH//2))

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

    def update(self, sheepList):
        foundsheep = []
        if self.isAlive():
            for i in range(len(sheepList)):
                if sheepList[i].x == self.x and sheepList[i].y == self.y:
                    foundsheep.append(sheepList[i])

            if len(foundsheep) == 0:
                self.move()
            elif len(foundsheep) > 0:
                self.energy = self.energy + foundsheep[0].energy
                foundsheep[0].energy = 0
                self.move()

        else:
            self.color = 'purple'





