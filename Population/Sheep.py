import pygame as p
import Variables as v
import random as r


class Sheep():
    '''
    A blueprint for creating sheep objects
    Attributes:
        x, y
        color
        energy
    Functions:
        draw
        move
    '''
    WIDTH = HEIGHT = v.SQ_LENGTH
    RADIUS = v.SQ_LENGTH//2

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.color = 'white'
        self.energy = v.INITIAL_SHEEP_ENERGY

    def draw(self, screen):
        image = p.image.load('sheep.png')
        image = p.transform.scale(image, (10, 10))
        screen.blit(image, (self.x * Sheep.WIDTH + Sheep.WIDTH // 2, self.y * Sheep.WIDTH + Sheep.WIDTH // 2))

    def move(self):
        '''
        Move a sheep randomly in one of 4 directions (up, down, left, right)
        Make sure the sheep doesn't go off the screen
        '''
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

    def graze(self, grassSquare):
        self.energy += 1
        grassSquare.energy -= 1

    def canGraze(self, grassSquare):
        if grassSquare.energy > 0:  # grass has energy for sheep to take
            return True
        return False

    def isAlive(self):
        if self.energy > 0:
            return True
        return False

    def update(self, grassSquare):
        '''
        depending on conditions of the sheep and the grass patch,
        sheep might move or graze or die
        '''
        if self.isAlive():
            if self.canGraze(grassSquare):
                # choose to move or graze
                action = r.choice(['graze', 'move'])
                if action == 'graze':
                    self.graze(grassSquare)
                elif action == 'move':
                    self.move()
            else:
                self.move()
        else:
            self.color = 'gray'






