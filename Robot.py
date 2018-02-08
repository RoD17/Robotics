####################################################
##   Author:     Rodney Greene, John Greenan
##
##   Written:	 01/18/2018
##	 Updated:	 02/7/2018
##   
##   Library for iRobot Create 2 commands.
##
####################################################


import struct
import serial 
import time

class Robot:

	# commands definitions
	startCMD					=  128
	seekDockCMD					=  143
	fullCMD						=  132
	safeCMD						=  131
	cleanCMD 					=  135
	everCleanCMD 				=  136
	spotCMD 					=  134
	powerCMD 					=  133
	scheduleCMD					=  167
	setDayTimeCMD				=  168
	resetCMD					=  7
	stopCMD						=  173
	buttonsCMD					=  142
	driveDirectCMD				=  145
	driveCMD					=  137
	drivePWMCMD					=  146
	motorsCMD					=  138
	motorsPWNCMD				=  144
	ledsCMD						=  139
	schLedsCMD					=  162
	sevenSegCMD					=  164
	buttonsCMD 					=  165
	songCMD 					=  140
	sensorCMD					=  142
	queryCMD					=  149
	streamCMD					=  148
	pauseCMD					=  150
	
	# packet IDs definitions
	wallPKT						=  8
	bmpWhlPKT					=  7
	cliffLeftPKT				=  9
	cliffFrontLeftPKT			=  10
	cliffFrontRightPKT			=  11
	cliffRightPKT				=  12
	virtualWallPKT				=  13
	buttonPKT					=  18
	distancePKT					=  19
	anglePKT					=  20
	chargingStatePKT			=  21
	voltagePKT					=  22
	temperaturePKT				=  24
	batteryChargePKT			=  25
	wallSignalPKT				=  27
	cliffLeftSignalPKT			=  28
	cliffFrontLeftSignalPKT		=  29
	cliffFrontRightSignalPKT	=  30
	cliffRightSignalPKT			=  31

	#Initializes connection via serial port.
	def __init__(self, port):
		try:
			self.serial_connection = serial.Serial(port, baudrate=115200, timeout =1)
			print "Connected!"
		except serial.SerialException:
			print "Connection failure!"
		time.sleep(0.2)
		self.serial_connection.close()
		time.sleep(0.2)
		self.serial_connection.open()

	#Sends commands via established serial connection.
	def sendCommand(self, input):
		self.serial_connection.write(input)

	#Sends the sensorCMD plus the specified packet and catches byte code and converts to string for comparison.
	def read(self, pkt):
		self.sendCommand(chr(self.sensorCMD))
		self.sendCommand(chr(pkt))
		time.sleep(0.1)
		buttonState = self.serial_connection.read()
		byte = struct.unpack('B', buttonState)[0]
		binary = '{0:08b}'.format(byte)
		return binary

	#Start bit opcode.
	def start(self):																								
		self.sendCommand(chr(self.startCMD))
		time.sleep(0.2)

	#Stop bit opcode.
	def stop(self):																									
		self.sendCommand(chr(self.stopCMD))
		time.sleep(0.2)

	#Resets create.
	def reset(self):																								
		self.sendCommand(chr(self.resetCMD))
		time.sleep(0.2)

	#Finds and returns to charging station.
	def seekDock(self):																								
		self.sendCommand(chr(self.seekDockCMD))
		time.sleep(0.2)
		
	#Moves robot by designating shared velocity of wheels, turn radius, and duration in seconds.
	def drive(self, velocityHighByte, velocityLowByte, radiusHighByte, radiusLowByte, time):						
		self.sendCommand(chr(self.driveCMD))
		self.sendCommand(chr(velocityHighByte))
		self.sendCommand(chr(velocityLowByte))
		self.sendCommand(chr(radiusHighByte))
		self.sendCommand(chr(radiusLowByte))
		time.sleep(time)

	#Moves robot by designating the individual velocity of each wheel. Formatted by high byte and low byte.
	def driveDirect(self, rightWheelHighByte, rightWheelLowByte, leftWheelHighByte, leftWheelLowByte):				
		self.sendCommand(chr(self.driveDirectCMD))
		self.sendCommand(chr(rightWheelHighByte))
		self.sendCommand(chr(rightWheelLowByte))
		self.sendCommand(chr(leftWheelHighByte))
		self.sendCommand(chr(leftWheelLowByte))

	#Moves the bot forwards at 200 mm/s for a specified number of seconds.
	def straight(self, seconds):
		self.drive(0,200,0,0)
		time.sleep(seconds)

	#Turns the bot around.
	def turnAround(self):
		self.driveDirect(0,200,255,56)
		time.sleep(1.85)

	#Rotated the bot clockwise at 200 mm/s.
	def turnRight(self):
		self.driveDirect(255,56,0,200)

	#Rotated the bot counter-clockwise at 200 mm/s.
	def turnLeft(self):
		self.driveDirect(0,200,255,56)

	#Stops the robot.
	def noDrive(self):
		self.driveDirect(0,0,0,0)

	#Toggles the LED lights by LED bit designation, color, and instensity of the light.
	def leds(self, ledBits, powerColor, powerIntensity):													
		self.sendCommand(chr(self.ledsCMD))																		
		self.sendCommand(chr(ledBits))
		self.sendCommand(chr(powerColor))
		self.sendCommand(chr(powerIntensity))

	#Helper method that turns off all LEDs warning lights.
	def noLED(self, color):
		self.leds(0, color, 255)

	#Helper function for the debris light.
	def debris(self, color):																						
		self.leds(1, color, 255)

	#Helper function for the spot light.
	def spot(self):																						
		self.leds(spotCMD, 255, 255)

	#Helper function for the dock light.
	def dock(self, time):																						
		self.leds(dockCMD, 255, 255)

	#Helper function for the check robot light.
	def checkRobot(self, color):																					
		self.leds(8, color, 255)

	#Helper function for checking both bumpers.
	def checkDebbie(self, color):
		self.leds(9, color, 255)

		
	#Sends opcode for seven segment display followed by the desired characters to be displayed.
	def digitLEDsASCII(self, digit3, digit2, digit1, digit0, time):												
		self.sendCommand(chr(self.sevenSegCMD))																	
		self.sendCommand(chr(digit3))
		self.sendCommand(chr(digit2))
		self.sendCommand(chr(digit1))
		self.sendCommand(chr(digit0))
		time.sleep(time)

	#Sets the create to full mode.
	def full(self):																								
		self.sendCommand(chr(self.fullCMD))
		time.sleep(0.3)

	#Sets the create to safe mode.
	def safe(self):																								
		self.sendCommand(chr(self.safeCMD))
		time.sleep(0.3)

	#Polls the wall sensor.
	def wall(self):																								
		return self.read(self.wallPKT)

	#Polls the bump and wheel sensors.
	def bmpWhl(self):																							
		return self.read(self.bmpWhlPKT)

	#Polls the left cliff sensor.
	def cliffL(self):																							
		return self.read(self.cliffLPKT)

	#Polls the front left cliff sensor.
	def cliffFL(self):																							
		return self.read(self.cliffFLPKT)

	#Polls the front right cliff sensor.
	def cliffFR(self):																							
		return self.read(self.cliffFRPKT)

	#Polls the right cliff sensor.
	def cliffR(self):																							
		return self.read(self.cliffRPKT)

	#Polls the virtual wall sensor.
	def vWall(self):																							
		return self.read(self.virtualWallPKT)

	#Polls the button sensors.
	def button(self):																							
		return self.read(self.buttonPKT)

	#Polls the wall sensor, reads a returned value.
	def dist(self):																								
		return self.read(self.distancePKT)

	#Reads the angle sensor.
	def angle(self):																							
		return self.read(self.anglePKT)

	#Determines if the create is charging.
	def isCharge(self):																							
		return self.read(self.chargingStatePKT)

	#Returns how many volts the create is charging at.
	def volt(self):																								
		return self.read(self.voltagePKT)

	#Returns the battery temperature.
	def temp(self):																								
		return self.read(self.temperaturePKT)

	#Returns remaining charge in battery.
	def batCharge(self):																						
		return self.read(self.batteryChargePKT)

	#Returns whether or not a wall is detected.
	def wallSig(self):																							
		return self.read(self.wallSignalPKT)

	#Polls the left cliff sensor. Detects cliffs.
	def cliffLSig(self):																																										
		return self.read(self.cliffLeftSignalPKT)

	#Polls the front left cliff sensor. Detects cliffs.
	def cliffFLSig(self):																						
		return self.read(self.cliffFrontLeftSignalPKT)

	#Polls the front right cliff sensor. Detects cliffs.
	def cliffFRSig(self):																						
		return self.read(self.cliffFrontRightSignalPKT)

	#Polls the right cliff sensor. Detects cliffs.
	def cliffRSig(self):																						
		return self.read(self.cliffRightPKT)

	#Compared sensor reading to left bumper value.
	def isBumpLeft(self, sense, color):
		if(sense == '00000001'):
			self.debris(color)

	#Compared sensor reading to right bumper value.
	def isBumpRight(self, sense, color):
		if(sense == '00000010'):
			self.checkRobot(color)

	#Compared sensor reading to combined bumper value.
	def isBumpBoth(self, sense, color):
		if(sense == '00000011'):
			self.checkDebbie(color)

	#Compared sensor reading to the lack of bumpers value.
	def isNotBump(self, sense, color):
		if(sense == '00000000'):
			self.noLED(color)

	#Helper method that compares all bumper byte values to the sensor reading in sequence.
	def isBump(self, sense, color):
		self.isBumpLeft(sense, color)
		self.isBumpRight(sense, color)
		self.isBumpBoth(sense, color)
		self.isNotBump(sense, color)




