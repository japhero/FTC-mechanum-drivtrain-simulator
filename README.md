# FTC-mechanum-drivtrain-simulator
a very shoddy simulator for a mechanum wheel drive train.

## instructions

### Dependancies
- Python i used 12
- pygames latest version


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


    powerDict = {"leftBackWheel":1, # a dict of what wheel powers to set.
                 "rightBackWheel":1,
                 "rightFrontWheel":1,
                 "leftFrontWheel":1,
                 }
    
    Robot.setPower( wheelDict = powerDict )
    
    Robot.moveOnForce()
    
```
