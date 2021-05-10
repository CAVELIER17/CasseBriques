import random

import pygame
from pygame.math import Vector2, Vector3


class Brique:
    def __init__(self, x, y):
        self.val = random.choice([0, 0, 3, 8, 12, 18])

        color = self.CouleurF()

        self.couleur = color

        self.position = Vector2(x, y)

    def afficher(self, core):

        color = self.CouleurF()

        self.couleur = color
        if self.val != 0:
            pygame.draw.rect(core.screen, self.couleur, (self.position.x, self.position.y, 35, 35))

    def CouleurF(self):

        if 1 <= self.val < 8:
            coleurF = int(round(255 - self.val * (255 / 8)))
            color = Vector3(coleurF, 255, 0)
        elif 8 <= self.val <= 18:
            coleurF = int(round((18-self.val) * 255 / 10))
            color = Vector3(255, coleurF, 0)
        else:
            color = Vector3(0, 0, 0)
        return color