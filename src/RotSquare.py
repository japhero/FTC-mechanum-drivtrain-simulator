from typing import Any
import pygame
import math



class rotSquare():
    def __init__(self,width ,height , transform , color = (100,0,0),rotation = math.radians(90)):
        
        
        self.height = height
        self.width = width
        self.color = color
        self.transform = transform
        
        
        #points for the square
        self.points = []

        self.radius = math.sqrt((height / 2)**2 + (width / 2)**2)
        self.angle = math.atan2(height / 2, width / 2)
        self.angles = [self.angle, -self.angle + math.pi, self.angle + math.pi, -self.angle]

        self.rot_in_rads = math.radians(rotation) 

        for self.angle in self.angles:
            y_offset = -1 * self.radius * math.sin(self.angle + self.rot_in_rads)
            x_offset = self.radius * math.cos(self.angle + self.rot_in_rads)
            self.points.append((self.transform[0] + x_offset, self.transform[1] + y_offset))
            
            
    def go(self, transform, rotation):
        self.radius = math.sqrt((self.height / 2)**2 + (self.width / 2)**2)
        self.angle = math.atan2(self.height / 2, self.width / 2)
        self.angles = [self.angle, -self.angle + math.pi, self.angle + math.pi, -self.angle]

        self.rot_in_rads = math.radians(rotation)
        self.transform = transform  
            
        points = []
        for angle in self.angles:
            y_offset = -1 * self.radius * math.sin(angle + self.rot_in_rads)
            x_offset = self.radius * math.cos(angle + self.rot_in_rads)
            points.append((self.transform[0] + x_offset, self.transform[1] + y_offset))
        self.points = points
    
    def getPoints(self):
        return self.points
    def getColor(self):
        return self.color
    
    def getTransform(self):
        return self.transform
    def getRotationInDeg(self):
        return math.degrees(self.rot_in_rads)
    def getRotationInRad(self):
        return self.rot_in_rads
            
