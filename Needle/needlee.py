import pygame as p
import random as r
import math as m


class Needle():
    def __init__(self, length):
        self.length = length
        self.startPoint = (r.randint(30, 570), r.randint(30, 570))  # randomized starting point of needle
        self.angle = r.uniform(0, 2*m.pi)  # randomized angle to tilt needle
        self.endPoint = (self.startPoint[0] + self.length * m.cos(self.angle),
                         self.startPoint[1] + self.length * m.sin(self.angle))  # use trig to calculate endpoint of needle
        self.box = None  # later, use bounding rectangle to test collisions

    def draw(self, screen):
        self.box = p.draw.line(screen, 'black', self.startPoint, self.endPoint, 2)  # draw line and save bounding rectangle to self.box

    def isSuccess(self, lines):  # parameter is list of floorboard gaps
        for line in lines:  # for each gap in the floorboards
            #print(line >= min(self.startPoint[1], self.endPoint[1]) and line <= max(self.startPoint[1], self.endPoint[1]))
            if (line <= max(self.startPoint[1], self.endPoint[1])) and (line >= min(self.startPoint[1], self.endPoint[1])):  # if this needle crosses the gap (because the bounding box collides with the gap line)
                return True  # success
        return False  # needle lies on a floorboard, not across any gaps
