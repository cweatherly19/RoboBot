import RoboPiLib as RPL
RPL.RoboPiInit("/dev/ttyAMA0",115200)

# To establish motors

LMotor = 1
RMotor = 0

#Define spot of motor plug in

def stop():
    RPL.servoWrite(LMotor, 0)
    RPL.servoWrite(RMotor, 0)

# So the robot can stop

def forward():
    RPL.servoWrite(LMotor, 1000)
    RPL.servoWrite(RMotor, 2000)

#So the robot can move forward

def backward():
    RPL.servoWrite(LMotor, 2000)
    RPL.servoWrite(RMotor, 1000)

#So the robot can move backwards

def right():
    RPL.servoWrite(LMotor, 1000)
    RPL.servoWrite(RMotor, 1000)

#So the robot can move right

def left():
    RPL.servoWrite(LMotor, 2000)
    RPL.servoWrite(RMotor, 2000)

#So the robot can move left

if "q":
    stop()
else:
    if 'w':
        forward()
    elif "a":
        left()
    elif "s":
        backward()
    elif "d":
        right()
    else:
        stop()
