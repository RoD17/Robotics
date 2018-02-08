import Robot
import time

#ls /dev/cu.usbserial-*

#instantiates the Robot class.
bob = Robot.Robot('/dev/tty.usbserial-DA01NOMJ')

#Start bit.
bob.start()

#Puts robot into safe mode.
bob.safe()

#Initial variables.
color = 255;
count = 0;

#Loop for 170 interations.
while (count < 170):
	#Is the current loop number divisible by 10 and is it less than 160?
	if(count%10 == 0 and count <= 160):
	#If so, decrease the color value by 15
		color -= 15
	#Always increment count.
	count += 1
	#Get a reading from the bump and wheel sensors.
	sense = bob.bmpWhl()
	#Print the string returned.
	print(sense)
	#Check if any or both of the bumpers are depressed.
	bob.isBump(sense, color)
	#Print the current loop bumber.
	print(count)
	#If the loop number is the max of 170, restart it.
	if(count == 170):
		color = 255
		count = 0
#Stop bit.
bob.stop()