import pygame
from RobotBody import Robot

pygame.init()
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Robotics Simulator")
clock = pygame.time.Clock()

Robot = Robot(22, 15, 100, 50, (screen_width / 2, screen_height / 2), color=(100, 100, 100), rotation=0)

while True:
    # Handle events
    clock.tick(120)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    # Update game state
    powerDict = {"leftBackWheel":   1,
                 "rightBackWheel":  0,
                 "rightFrontWheel": 0,
                 "leftFrontWheel":  0,
                 }

    Robot.setPower(wheelDict=powerDict)

    # Index guide for wheels
    # leftFrontWheel,leftBackWheel,rightBackWheel,rightFrontWheel

    Robot.moveOnForce()

    # Draw to the screen
    Robot.drawOnScreen(screen)


