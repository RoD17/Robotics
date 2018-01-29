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

	#def definitions(self):
	'''
		#Globalization
		global startCMD
		global seekDockCMD
		global fullCMD
		global safeCMD
		global cleanCMD
		global everCleanCMD
		global spotCMD
		global powerCMD
		global scheduleCMD
		global setDayTimeCMD
		global resetCMD
		global stopCMD
		global buttonsCMD
		global driveDirectCMD
		global driveCMD
		global drivePWMCMD
		global motorsCMD
		global motorsPWNCMD
		global ledsCMD
		global schLedsCMD
		global sevenSegCMD
		global buttonsCMD
		global songCMD
		global sensorCMD
		global queryCMD
		global streamCMD
		global pauseCMD
		global wallPKT
		global bmpWhlPKT
		global cliffLeftPKT
		global cliffFrontLeftPKT
		global cliffFrontRightPKT
		global cliffRightPKT
		global virtualWallPKT
		global buttonPKT
		global distancePKT
		global anglePKT
		global chargingStatePKT
		global voltagePKT
		global temperaturePKT
		global batteryChargePKT
		global wallSignalPKT
		global cliffLeftSignalPKT
		global cliffFrontLeftSignalPKT
		global cliffFrontRightSignalPKT
		global cliffRightSignalPKT



	'''
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



	def __init__(self, port):																						#Initializes connection via serial port.
		try:
			self.serial_connection = serial.Serial(port, baudrate=115200, timeout =1)
			print "Connected!"
		except serial.SerialException:
			print "Connection failure!"
		time.sleep(0.2)
		self.serial_connection.close()
		time.sleep(0.2)
		self.serial_connection.open()

	def sendCommand(self, input):																					#Sends commands via established serial connection.
		self.serial_connection.write(input)

	def read(self, howManyBytes):
		buttonState = connection.read()
		byte = struct.unpack('B', buttonState)[0]
		binary = '{0:08b}'.format(byte)
		return binary

	def start(self):																								#Start bit opcode.
		self.sendCommand(chr(self.startCMD))
		time.sleep(0.2)

	def stop(self):																									#Stop bit opcode.
		self.sendCommand(chr(self.stopCMD))
		time.sleep(0.2)

	def reset(self):																								#Resets create.
		self.sendCommand(chr(self.resetCMD))
		time.sleep(0.2)

	def seekDock(self):																								#Finds and returns to charging station.
		self.sendCommand(chr(self.seekDockCMD))
		time.sleep(0.2)
		

	def drive(self, velocityHighByte, velocityLowByte, radiusHighByte, radiusLowByte, time):						#Moves robot by designating shared velocity of wheels, 
		self.sendCommand(chr(self.driveCMD))																		#turn radius, and duration in seconds.
		self.sendCommand(chr(velocityHighByte))
		self.sendCommand(chr(velocityLowByte))
		self.sendCommand(chr(radiusHighByte))
		self.sendCommand(chr(radiusLowByte))
		time.sleep(time)

	def driveDirect(self, rightWheelHighByte, rightWheelLowByte, leftWheelHighByte, leftWheelLowByte):				#Moves robot by designating the individual velocity of
		self.sendCommand(chr(self.driveDirectCMD))																	#each wheel. Formatted by high byte and low byte.
		self.sendCommand(chr(rightWheelHighByte))
		self.sendCommand(chr(rightWheelLowByte))
		self.sendCommand(chr(leftWheelHighByte))
		self.sendCommand(chr(leftWheelLowByte))

	def straight(self):
		self.drive(0,200,0,0)

	def turnAround(self):
		self.driveDirect(0,200,255,56)
		time.sleep(1.85)

	def turnRight(self):
		self.driveDirect(255,56,0,200)

	def turnLeft(self):
		self.driveDirect(0,200,255,56)

	def noDrive(self):
		self.driveDirect(0,0,0,0)

	def leds(self, ledBits, powerColor, powerIntensity, time):													#Toggles the LED lights by LED bit designation, color, 
		self.sendCommand(chr(self.ledsCMD))																		#and instensity of the light.
		self.sendCommand(chr(ledBits))
		self.sendCommand(chr(powerColor))
		self.sendCommand(chr(powerIntensity))
		time.sleep(time)

	def debris(self, time):																						#Helper function for the debris light.
		self.leds(debrisCMD, 255, 255, time)

	def spot(self, time):																						#Helper function for the spot light.
		self.leds(spotCMD, 255, 255, time)

	def dock(self, time):																						#Helper function for the dock light.
		self.leds(dockCMD, 255, 255, time)

	def checkRobot(self, time):																					#Helper function for the check robot light.
		self.leds(checkRobotCMD, 255, 255, time)

		

	def digitLEDsASCII(self, digit3, digit2, digit1, digit0, time):												#Sends opcode for seven segment display followed
		self.sendCommand(chr(self.sevenSegCMD))																	#by the desired characters to be displayed.
		self.sendCommand(chr(digit3))
		self.sendCommand(chr(digit2))
		self.sendCommand(chr(digit1))
		self.sendCommand(chr(digit0))
		time.sleep(time)
	
	def full(self):																								#Sets the create to full mode.
		self.sendCommand(chr(self.fullCMD))
		time.sleep(0.3)

	def safe(self):																								#Sets the create to safe mode.
		self.sendCommand(chr(self.safeCMD))
		time.sleep(0.3)
	
	def sensor(self, packet):																					#Polls a sensor designated by packet id.
		self.sendCommand(self.sensorCMD)
		self.sendCommand(chr(packet))
		time.sleep(0.2)
		return read()

	def wall(self):																								#Polls the wall sensor.
		print(sensor(self.wallPKT))

	def bmpWhl(self):																							#Polls the bump and wheel sensors.
		self.sensor(self.bmpWhlPKT)

	def cliffL(self):																							#Polls the left cliff sensor.
		self.sensor(self.cliffLPKT)

	def cliffFL(self):																							#Polls the front left cliff sensor.
		self.sensor(self.cliffFLPKT)

	def cliffFR(self):																							#Polls the front right cliff sensor.
		self.sensor(self.cliffFRPKT)

	def cliffR(self):																							#Polls the right cliff sensor.
		self.sensor(self.cliffRPKT)

	def vWall(self):																							#Polls the virtual wall sensor.
		self.sensor(self.virtualWallPKT)

	def button(self):																							#Polls the button sensors.
		self.sensor(self.buttonPKT)

	def dist(self):																								#Polls the wall sensor, reads a returned value.
		self.sensor(self.distancePKT)

	def angle(self):																							#Reads the angle sensor.
		self.sensor(self.anglePKT)

	def isCharge(self):																							#Determines if the create is charging.
		self.sensor(self.chargingStatePKT)

	def volt(self):																								#Returns how many volts the create is charging at.
		self.sensor(self.voltagePKT)

	def temp(self):																								#Returns the battery temperature.
		self.sensor(self.temperaturePKT)

	def batCharge(self):																						#Returns remaining charge in battery.
		self.sensor(self.batteryChargePKT)

	def wallSig(self):																							#Returns whether or not a wall is detected.
		self.sensor(self.wallSignalPKT)

	def cliffLSig(self):																						#Polls the left cliff sensor. Detects cliffs.																				
		self.sensor(self.cliffLeftSignalPKT)

	def cliffFLSig(self):																						#Polls the front left cliff sensor. Detects cliffs.
		self.sensor(self.cliffFrontLeftSignalPKT)

	def cliffFRSig(self):																						#Polls the front right cliff sensor. Detects cliffs.
		self.sensor(self.cliffFrontRightSignalPKT)

	def cliffRSig(self):																						#Polls the right cliff sensor. Detects cliffs.
		self.sensor(self.cliffRightPKT)


