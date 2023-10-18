import math
import pygame

from RotSquare import rotSquare


class MechanumWheel(rotSquare):

    def __init__(self, vectorRot, power=0, *args, **kwargs, ) -> None:
        super().__init__(*args, **kwargs)

        self.vectorRot = math.radians(vectorRot)
        self.power = power
        self.forceVector = pygame.Vector2(math.cos(self.vectorRot), math.sin(self.vectorRot)) * power
        self.angularTorque = 0

    def changePower(self, power):
        self.power = power
        self.forceVector = pygame.Vector2(math.cos(self.vectorRot), math.sin(self.vectorRot)) * power
        return self.forceVector

    def getForceVector(self):
        return self.forceVector

    def getPower(self):
        return self.power
