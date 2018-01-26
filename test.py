import Robot

bob = Robot.Robot('/dev/tty.usbserial-DA01NNEY')

bob.start()

bob.full()

bob.debris(3)

bob.stop()