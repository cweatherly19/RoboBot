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

ch = sys.stdin.read(1) # reads one character at a time

if ch == "q":
    stop()
else:
    if ch == 'w':
        forward()
    elif ch == "a":
        left()
    elif ch == "s":
        backward()
    elif ch == "d":
        right()
    else:
        stop()
