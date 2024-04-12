# Name: L1_WheelClass
# Date: 4 / 12 / 2024
# 
# Author: Carter Cummings
# Purpose: Define wheel class 

# Define wheel class that controls speed
class Wheel:
    def __init__(self) -> None:
        self.speed = 0
        self.inputSpeed = 0


# Defines 
class WheelBlock:
    def __init__(self) -> None:
        self.leftW = Wheel() 
        self.rightW = Wheel()
        
        self.rotation = 0
        self.inputRotation = 0

