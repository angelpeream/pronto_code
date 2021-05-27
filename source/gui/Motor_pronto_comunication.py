# -*- coding: utf-8 -*-
"""
Created on Wed May  5 17:58:09 2021

@author: Pedro
"""

import serial
import tkinter as tk
from tkinter import ttk
import time
import threading

MENU = """
F) move forward
B) move backward
H) seek home
C) comm check
S) start sweep
"""

secs = 1
 

COMMAND_FORWARD = 0
COMMAND_BACKWARD = 1
COMMAND_HOME = 2
COMMAND_MOVE = 3
COMMAND_POS = 4
COMMAND_CHECK = 5
COMMAND_RAW = 6
COMMAND_ENABLE = 7
COMMAND_DISABLE = 8




class MotorControl:
    """
    main application for motor control
    """  
    def __init__(self):
        """
        """
        self.degreesStep = 10
        self.timeStep = 600 * secs
        self.port='/dev/ttyUSB1'
        self.baudrate=9600
        #self.ser = serial.Serial('/dev/ttyUSB1', 9600) #timeout=10);
        self.availableCommands = {
            "H":  self.fn_homeSeek,
            "F":  self.fn_moveForward,
            "C":  self.fn_commCheck,
            "B":  self.fn_moveBackward,
            "0":  self.fn_goTo0,
            "S":  self.fn_fullSeries,
            "R":  self.fn_rawCommand,
            "0":  self.fn_disable,
            "1":  self.fn_enable,
            }
                   
               
    def connect(self):
        self.ser= serial.Serial(self.port,self.baudrate)
        
        
    def write(self, command, param1, param2):
        """
        """
        command = int(command)
        print(bytes(f"{command} {param1} {param2}", "utf-8"))
        #self.ser.write(bytes(f"{command} {param1} {param2}", "utf-8"))
        #self.ser.flush()

   
    def readline(self):
        """
        """
        return self.ser.readline()[:-1].decode("utf-8")
   
   
    def interactive(self):
        """
        """
        while 1:
            print(MENU)
            x = input(">").strip().upper()
           
            #self.ser.reset_input_buffer()
            if x in self.availableCommands:
                self.availableCommands[x]()
            elif x == "x":
                break
               
            print(str(self.readline()))        
            print(str(self.readline()))
            print(str(self.readline()))
       
               
    def fn_commCheck(self):
        """
        """
        print("comms check")
        self.write(COMMAND_CHECK, 1, 2)
       
     
    def fn_homeSeek(self):
        """
        """
        pass
   
   
    def fn_goTo0(self):
        """
        """
        pass
   
   
    def fn_moveForward(self):
        """
        """
        while 1:
            x = input("steps?")
            try:
                if int(x) > 0:
                    break
            except:
                pass
       
        steps = int(x)
        self.write(COMMAND_FORWARD, steps, 0)
   
   
    def fn_moveBackward(self):
        """
        """
        while 1:
            x = input("steps?")
            try:
                if int(x) > 0:
                    break
            except:
                pass
       
        steps = int(x)
        self.write(COMMAND_BACKWARD, steps, 0)
     
     
    def fn_rawCommand(self):
        """
        """
        pin = int(input("pin number?"));
        value = int(input("value"));
       
        if value != 0:
            value = 1
       
        self.write(COMMAND_RAW, pin, value);
       
    def fn_fullSeries(self):
        """
        """
        print("not implemented")
       
    def fn_enable(self):
        self.write(COMMAND_ENABLE, 0, 0);
   
    def fn_disable(self):
        self.write(COMMAND_DISABLE, 0, 0);
