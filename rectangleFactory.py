import math

x = 0
y = 0
rot = 90
width = 2
height = 4

relativeAngle = math.atan2(width,height) + math.radians(rot)

angles = [relativeAngle,-relativeAngle + math.pi ,relativeAngle-math.pi,-relativeAngle]

points = []

for angle in angles:
    points.append((math.cos(angle),math.sin(angle))) 
    
    

