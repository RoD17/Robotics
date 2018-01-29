import Robot
import time

bob = Robot.Robot('/dev/tty.usbserial-DA01NOMJ')

bob.start()

bob.safe()

bob.turnRight()

time.sleep(0.95)

bob.noDrive()

time.sleep(1)

bob.turnLeft()

time.sleep(0.95)

bob.noDrive()

time.sleep(1)

bob.turnAround()

bob.noDrive()

time.sleep(1)

bob.stop()