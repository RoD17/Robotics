import serial
import time

port = "/dev/cu.usbserial-DA01NNEY"

global connection 
connection = serial.Serial(port, baudrate=115200, timeout=1)


#def onConnect():
#    global connection
#
#    port = "/dev/cu.usbserial-DA01NOB4"
#
#    try:
#        connection = serial.Serial(port, baudrate=115200, timeout=1)
#        print("Connected!")
#    except serial.SerialException:
#        print("Failed to connect!")

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

def driveDirect(left,right):
    send(b'\x91')
    send(b'\x')
    send(b'\x')
    send(b'\x')
    send(b'\x')

def drive(velocity,radius):
    send(b'\x89')
    send(b'\x')
    send(b'\x')
    send(b'\x')
    send(b'\x')
    
def led(led,color,intensity):
    send(b'\x8B')
    send(b'\x'+led)
    send(b'\x'+color)
    send(b'\x'+intensity)

def debris(color,intensity):
    led(b'\x00',color,intensity)

def spot(color,intensity):
    led(b'\x01',color,intensity)

def dock(color,intensity):
    led(b'\x02',color,intensity)

def check(color,intensity):
    led(b'\x03',color,intensity)

start()

time.sleep(2)

communication.write(b'x07')

time.sleep(1)

communication.write(b'\x00\x32\x00\x32')

time.sleep(3)

stop()

time.sleep(1)

close()

