import serial
import pynput
from time import sleep
from pynput.keyboard import Key, Controller

keyboard = Controller()
ser =  serial.Serial('COM3')
ser.baudrate = 9600

while True:
    relayed = ser.read(1)
    print(relayed)
    if(relayed == b'1'):
        keyboard.press(Key.ctrl)
        keyboard.press('s')
        keyboard.release(Key.ctrl)
        keyboard.release('s')
        sleep(1)
