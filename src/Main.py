import time
import pygame
import math
import MechanumWheel
from RotSquare import rotSquare
from RobotBody import Robot

pygame.init()

screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Robotics Simulator")
clock = pygame.time.Clock()



Robot = Robot(45,30,200,100,(screen_width / 2,screen_height / 2),color = (100,100,100),rotation = 0)



while True:
    # Handle events
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            False
    
    # Update game state
    powerDict = {"leftBackWheel":1,
                 "rightBackWheel":1,
                 "rightFrontWheel":1,
                 "leftFrontWheel":1,
                 }
    
    Robot.setPower( wheelDict = powerDict )
    
    # Index guide for wheels
    # leftFrontWheel,leftBackWheel,rightBackWheel,rightFrontWheel
    
    Robot.moveOnForce()
    
    
    # Draw to the screen
    
    screen.fill((255, 255, 255))
    pygame.draw.polygon(screen, Robot.getColor(), Robot.getPoints())
    for wheel in Robot.getWheelList():
        pygame.draw.polygon(screen, wheel.getColor(), wheel.getPoints())
    pygame.display.update()
    
    
    

pygame.quit()
