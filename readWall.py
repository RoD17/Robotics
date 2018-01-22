import serial
import time


def onConnect():
	global connection

	port = "/dev/cu.usbserial-DA01NOMJ"

	try:
		connection = serial.Serial(port, baudrate=115200, timeout=1)
		print("Connected!")
	except serial.SerialException:
		print("Failed to connect!")

def onQuit():
	root.destroy()

def close():
	connection.close()

def sleep(seconds):
	time.sleep(seconds);

def send(bit):
	connection.write(bit)

def start():
	send(b'\x80')

def stop():
	send(b'\xAD')

def reset():
	send(b'\x07')

def power():
	send(b'\x85')

onConnect()

start()

time.sleep(2)

connection.write(b'\x80')

time.sleep(1)

connection.write(b'\x84')

time.sleep(1)

connection.write(b'\x8E')

time.sleep(1)

connection.write(b'\x12')

time.sleep(1)

button = connection.write(b'\x01')

if(button > 0):
	print(1)
else:
	print(0)

time.sleep(1)

stop()

#time.sleep(1)

#close()