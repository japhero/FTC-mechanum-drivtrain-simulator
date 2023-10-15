import pygame
import math
from RotSquare import rotSquare
from MechanumWheel import MechanumWheel

class Robot(rotSquare):
    
    def __init__(self, wheelWidth,wheelHeight,  *args, **kwargs):
        super().__init__( *args,**kwargs)
        
        self.totalForce = pygame.Vector2(0,0)
        
        # grabs the cords based off the points passed into the super class/rotSquare or the constructor for the mechanum square
        self.leftFrontWheelTransform =  (self.points[0][0],self.points[0][1])
        self.rightFrontWheelTransform = (self.points[1][0],self.points[1][1])
        self.leftBackWheelTransform =   (self.points[2][0],self.points[2][1])
        self.rightBackWheelTransform =  (self.points[3][0],self.points[3][1]) 
        
        #passes the color and the transform to the mechanum wheel class with the angle of its vector and the power of the wheel
        self.leftFrontWheel = MechanumWheel(45,0,wheelWidth,wheelHeight, self.leftFrontWheelTransform, color = (0,0,50),rotation = 0)
        self.rightFrontWheel = MechanumWheel(135,0,wheelWidth,wheelHeight, self.rightFrontWheelTransform, color = (0,0,100),rotation = 0)
        self.leftBackWheel = MechanumWheel(135,0,wheelWidth,wheelHeight, self.leftBackWheelTransform, color = (0,0,150),rotation = 0)
        self.rightBackWheel = MechanumWheel(45,0,wheelWidth,wheelHeight, self.rightBackWheelTransform, color = (0,0,200),rotation = 0)
        
        self.wheelList = [self.leftFrontWheel,self.leftBackWheel,self.rightBackWheel,self.rightFrontWheel]
        
    def getWheelList(self):
        return self.wheelList
    
    def moveAll(self,changVal,rotChangeVal):
        newPos = (self.transform[0] + changVal[0],self.transform[1] + changVal[1])
        
        newRot = self.getRotationInDeg() + rotChangeVal
        
        self.go(newPos,newRot) # could reduce variables becasue they have the same rotchange and posChange

        for i,wheel in enumerate(self.wheelList):
            newRot = wheel.getRotationInDeg() + rotChangeVal
            newPos = (self.points[i][0] + changVal[0],self.points[i][1] + changVal[1])
            wheel.go(newPos,newRot)
            
    
    def setPower(self,wheelDict ):
        
        
         
        
        for wheelName,power in wheelDict.items():
            match wheelName:
                case "leftFrontWheel" | 0 :
                    self.leftFrontWheel.changePower(power)
                case "rightFrontWheel"| 3:
                    self.rightFrontWheel.changePower(power)
                case "leftBackWheel"  | 1 :
                    self.leftBackWheel.changePower(power)
                case "rightBackWheel" | 2 :
                    self.rightBackWheel.changePower(power)
        
                
            
    def getTotalForce(self):
        self.totalForce = pygame.Vector2(0,0)
        for wheel in self.wheelList:
            self.totalForce += wheel.getForceVector()
            
        return self.totalForce
    
    def moveOnForce(self) -> None :
        vectorPos = (round(self.getTotalForce().y,2),round(self.getTotalForce().x,2))
        print(vectorPos,math.atan2(vectorPos[0],vectorPos[1]))
        self.moveAll(vectorPos,0)
        
