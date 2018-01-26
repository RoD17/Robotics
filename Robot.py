####################################################
##   Author:     Rodney Greene, John Greenan
##
##   Written:	 01/18/2018
##	 Updated:	 01/25/2018
##   
##   Library for iRobot Create 2 commands.
##
####################################################


import struct
import serial 
import time

class Robot:
	# commands definitions
	start					=  128
	seekDock				=  143
	full					=  132
	safe					=  131
	clean 					=  135
	everClean 				=  136
	spot 					=  134
	power 					=  133
	schedule				=  167
	setDayTime				=  168
	reset					=  7
	stop					=  173
	buttons					=  142
	driveDirect				=  145
	drive					=  137
	drivePWM				=  146
	motors					=  138
	motorsPWN				=  144
	leds					=  139
	schLeds					=  162
	sevenSeg				=  164
	buttons 				=  165
	song 					=  140
	sensor					=  142
	query					=  149
	stream					=  148
	pause					=  150
	
	# packet IDs definitions
	wall					=  8
	bmpWhl					=  7
	cliffLeft				=  9
	cliffFrontLeft			=  10
	cliffFrontRight			=  11
	cliffRight				=  12
	virtualWall				=  13
	button					=  18
	distance				=  19
	angle					=  20
	chargingState			=  21
	voltage					=  22
	temperature				=  24
	batteryCharge			=  25
	wallSignal				=  27
	cliffLeftSignal			=  28
	cliffFrontLeftSignal	=  29
	cliffFrontRightSignal	=  30
	cliffRightSignal		=  31
	
	def __init__(self, port):																					#Initializes connection via serial port.
		try:
			self.serial_connection = serial.Serial(port, baudrate=115200, timeout =1)
			print "Connected!"
		except serial.SerialException:
			print "Connection failure!"
		time.sleep(0.2)
		self.serial_connection.close()
		time.sleep(0.2)
		self.serial_connection.open()

	def sendCommand(self, input):																				#Sends commands via established serial connection.
		self.serial_connection.write(input)

	def read(self, howManyBytes):
		buttonState = connection.read()
		byte = struct.unpack('B', buttonState)[0]
		binary = '{0:08b}'.format(byte)
		return binary

	def start(self):																							#Start bit opcode.
		self.sendCommand(chr(self.start))
		time.sleep(0.2)

	def stop(self):																								#Stop bit opcode.
		self.sendCommand(chr(self.stop))
		time.sleep(0.2)

	def reset(self):																							#Resets create.
		self.sendCommand(chr(self.reset))
		time.sleep(0.2)

	def seekDock(self):																							#Finds and returns to charging station.
		self.sendCommand(chr(self.seekDock))
		sleep(0.2)
		

	def drive(self, velocityHighByte, velocityLowByte, radiusHighByte, radiushLowByte, time):					#Moves robot by designating shared velocity of wheels, 
		self.sendCommand(chr(velocityHighByte))																	#turn radius, and duration in seconds.
		self.sendCommand(chr(self.drive))
		self.sendCommand(chr(velocityLowByte))
		self.sendCommand(chr(radiusHighByte))
		self.sendCommand(chr(radiusLowByte))
		time.sleep(time)

	def driveDirect(self, rightWheelHighByte, rightWheelLowByte, leftWheelHighByte, leftWheelLowByte, time):	#Moves robot by designating the individual velocity of
		self.sendCommand(chr(self.driveDirect))																	#each wheel. Formatted by high byte and low byte.
		self.sendCommand(chr(rightWheelHighByte))
		self.sendCommand(chr(rightWheelLowByte))
		self.sendCommand(chr(leftWheelHighByte))
		self.sendCommand(chr(leftWheelLowByte))
		time.sleep(time)

	def leds(self, ledBits, powerColor, powerIntensity, time):													#Toggles the LED lights by LED bit designation, color, 
		self.sendCommand(chr(self.leds))																		#and instensity of the light.
		self.sendCommand(chr(ledBits))
		self.sendCommand(chr(powerColor))
		self.sendCommand(chr(powerIntensity))
		time.sleep(time)

	def debris(self, time):																						#Helper function for the debris light.
		leds(self.debris, 255, 255, time)

	def spot(self, time):																						#Helper function for the spot light.
		leds(self.spot, 255, 255, time)

	def dock(self, time):																						#Helper function for the dock light.
		leds(self.dock, 255, 255, time)

	def checkRobot(self, time):																					#Helper function for the check robot light.
		leds(self.checkRobot, 255, 255, time)

		

	def digitLEDsASCII(self, digit3, digit2, digit1, digit0, time):												#Sends opcode for seven segment display followed
		self.sendCommand(chr(self.sevenSeg))																	#by the desired characters to be displayed.
		self.sendCommand(chr(digit3))
		self.sendCommand(chr(digit2))
		self.sendCommand(chr(digit1))
		self.sendCommand(chr(digit0))
		time.sleep(time)
	
	def full(self):																								#Sets the create to full mode.
		self.sendCommand(chr(self.full))
		time.sleep(0.2)

	def safe(self):																								#Sets the create to safe mode.
		self.sendCommand(chr(self.safe))
		time.sleep(0.2)
	
	def sensor(self, packet):																					#Polls a sensor designated by packet id.
		self.sendCommand(self.sensor)
		self.sendCommand(chr(packet))
		time.sleep(0.2)
		return read()

	def wall(self):																								#Polls the wall sensor.
		print(sensor(wall))

	def bmpWhl(self):																							#Polls the bump and wheel sensors.
		sensor(self.bmpWhl)

	def cliffL(self):																							#Polls the left cliff sensor.
		sensor(self.cliffL)

	def cliffFL(self):																							#Polls the front left cliff sensor.
		sensor(self.cliffFL)

	def cliffFR(self):																							#Polls the front right cliff sensor.
		sensor(self.cliffFR)

	def cliffR(self):																							#Polls the right cliff sensor.
		sensor(self.cliffR)

	def vWall(self):																							#Polls the virtual wall sensor.
		sensor(self.virtualWall)

	def button(self):																							#Polls the button sensors.
		sensor(self.button)

	def dist(self):																								#Polls the wall sensor, reads a returned value.
		sensor(self.distance)

	def angle(self):																							#Reads the angle sensor.
		sensor(self.angle)

	def isCharge(self):																							#Determines if the create is charging.
		sensor(self.chargingState)

	def volt(self):																								#Returns how many volts the create is charging at.
		sensor(self.voltage)

	def temp(self):																								#Returns the battery temperature.
		sensor(self.temperature)

	def batCharge(self):																						#Returns remaining charge in battery.
		sensor(self.batteryCharge)

	def wallSig(self):																							#Returns whether or not a wall is detected.
		sensor(self.wallSignal)

	def cliffLSig(self):																						#Polls the left cliff sensor. Detects cliffs.																				
		sensor(self.cliffLeftSignal)

	def cliffFLSig(self):																						#Polls the front left cliff sensor. Detects cliffs.
		sensor(self.cliffFrontLeftSignal)

	def cliffFRSig(self):																						#Polls the front right cliff sensor. Detects cliffs.
		sensor(self.cliffFrontRightSignal)

	def cliffRSig(self):																						#Polls the right cliff sensor. Detects cliffs.
		sensor(self.cliffRight)


