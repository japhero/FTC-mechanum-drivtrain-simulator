# Importing pygame module
import pygame
from pygame.locals import *
import math
import pygame.draw
 
# initiate pygame and give permission
# to use pygame's functionality.
pygame.init()
 
# create the display surface object
# of specific dimension.
window = pygame.display.set_mode((600, 600))
 
# Fill the scree with white color
window.fill((255, 255, 255))
clock = pygame.time.Clock()


import math
import pygame.draw


def draw_rectangle(x, y, width, height, color, rotation=0):
    points = []

    # The distance from the center of the rectangle to
    # one of the corners is the same for each corner.
    radius = math.sqrt((height / 2)**2 + (width / 2)**2)

    # Get the angle to one of the corners with respect
    # to the x-axis.
    angle = math.atan2(height / 2, width / 2)

    # Transform that angle to reach each corner of the rectangle.
    angles = [angle, -angle + math.pi, angle + math.pi, -angle]

    # Convert rotation from degrees to radians.
    rot_radians = (math.pi / 180) * rotation

    # Calculate the coordinates of each point.
    for angle in angles:
        y_offset = -1 * radius * math.sin(angle + rot_radians)
        x_offset = radius * math.cos(angle + rot_radians)
        points.append((x + x_offset, y + y_offset))

    pygame.draw.polygon(window, color, points)

i = 0
while True:
    # Handle events
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            False
    
    # Update game state
    
    
    
    # Draw to the screen
    
    window.fill((255, 255, 255))
    
    
    draw_rectangle(200,200,200,100,(0,0,0),235)
    pygame.display.update()