# FTC-mechanum-drivtrain-simulator
a very shoddy simulator for a mechanum wheel drive train.

## instructions

### Dependancies
- Python i used 3.12
- pygame i used 2.5.2


### Usage
to use copy everything in src and put your code in between the lines saying update game state.

code will look like below
```python
...

while True:
    # Handle events
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            False
    
    # Update game state
    # PUT ALL YOUR CODE UNDER HERE 

    
    ##    ------------------------------------    ##
    Robot.moveOnForce() # updates the robot position based on wheel power
    Robot.drawOnScreen(pygameWindow) # draws the robot on the screen
```

# Documentation

## Robot.setPower({"wheelName": power})
The set power method sets power for whatever the desired wheels. 
The function takes a dictionary/Hashmap of wheel names and power values.
```python

wheelDict = {"leftBackWheel":1, # a dict of what wheel powers to set.
             "rightBackWheel":1,
             "rightFrontWheel":1,
             "leftFrontWheel":1,
             }

Robot.setPower(wheelDict)
```

## Robot.go((x,y),rotation) 
The go method moves the robot to a position on the screen. Pass a tuple with the x position, y position and the rotation in degrees. It goes to the position it doesnt move 
```python
Robot.go((100,100),0) # moves the robot to 100,100 and sets the rotation to 0 degrees
```
---