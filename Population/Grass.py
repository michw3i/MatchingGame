import pygame as p
import Variables as v


class Grass():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.energy = v.MAX_GRASS_GRAZES
        self.turnsToRegrowth = v.GRASS_REFRESH_RATE  # countdown variable
        self.colors = [(122, 124, 43),
                       (151, 163, 44),
                       (128, 178, 42),
                       (117, 196, 39),
                       (101, 206, 26),
                       (110, 235, 21)]

    def draw(self, screen):
        p.draw.rect(screen, self.colors[self.energy],
                    (self.x * v.SQ_LENGTH, self.y * v.SQ_LENGTH,
                     v.SQ_LENGTH, v.SQ_LENGTH))

    def update(self):
        if self.turnsToRegrowth <= 0 and self.energy < v.MAX_GRASS_GRAZES:
            self.energy += 1  # photosynthesis
            self.turnsToRegrowth = v.MAX_GRASS_GRAZES  # reset countdown
        else:
            self.turnsToRegrowth -= 1
