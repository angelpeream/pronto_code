#!/usr/bin/env python3

import serial
import time
import sys


MENU = """
F) move forward        %) HOME SENSOR TEST
B) move backward       &) MOVEMENT TEST
H) seek home           0) DISABLE
C) comm check          1) ENABLE
S) start sweep         R) RAW COMMAND
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
COMMAND_ATHOME = 9



class MotorControl:
    """
    main application for motor control
    """
    
     
    def __init__(self, dev):
        """
        """
        self.degreesStep = 10
        self.timeStep = 600 * secs
        self.ser = serial.Serial(dev, 9600) #timeout=10);
        self.availableCommands = {
            "H":  self.fn_homeSeek,
            "F":  self.fn_moveForward,
            "C":  self.fn_commCheck,
            "B":  self.fn_moveBackward,
            "S":  self.fn_fullSeries,
            "R":  self.fn_rawCommand,
            "0":  self.fn_disable,
            "1":  self.fn_enable,
            "&":  self.fn_hardTest,
            "%":  self.fn_checkHome,
            }            
                
    
    def write(self, command, param1, param2):
        """
        writes a command to the arduino 
        """
        command = int(command)
        self.ser.write(bytes(f"{command} {param1} {param2}", "utf-8"))
        self.ser.flush()
        
    
    def readline(self):
        """
        reads a line from arduino serial interface
        """
        return self.ser.readline()[:-1].decode("utf-8")
    
    
    def sweep(self):
        """
        makes a full sweep
        """
        steps = readInt("steps per position")
        times = readInt("number of positions")
        t = readInt("seconds per position")
        
        for i in times:
            # 1) wait
            
            for s in range(t):
                print(f"{s} secs to go")
                
            # 2) wait for acquisition to change            
            print("time finished. STOP ACQUISITION and press a key")
            _ = input()
            
            # 2 move steps
            move(steps)
            
            
        
    def interactive(self):
        """
        opens the menu and waits for user selections
        """
        while 1: 
            
            print ("\n" * 30)
            while self.ser.inWaiting():  # Or: while ser.inWaiting():
                print(str(self.readline()))
            print(MENU)
            
            try:
                x = input(">").strip().upper()
            
                #self.ser.reset_input_buffer()
                if x in self.availableCommands:                
                    self.availableCommands[x]()                
                    #print(str(self.readline()))        
                    #print(str(self.readline()))
                    #print(str(self.readline()))

                elif x == "X":
                    break
                
                

            except KeyboardInterrupt as e:
                print("CTRL-C. use x to exit")
                continue
            
           
        
        
    def fn_hardTest(self):
        """
        keeps moving forward the motor 200 steps, enabling and disabling
        300 iterations
        """
        for i in range(300):
            print("iteration %s" %i)
            self.write(COMMAND_ENABLE, 0, 0)
            time.sleep(1)
            self.write(COMMAND_BACKWARD, 200, 0)
            time.sleep(1)
            self.write(COMMAND_DISABLE, 0, 0)
            time.sleep(30)
        
        
                
    def fn_commCheck(self):
        """
        checks communications with arduino
        """
        print("comms check")
        self.write(COMMAND_CHECK, 1, 2)
        
      
    def fn_homeSeek(self):
        """
        starts the home seeking routine in arduino
        """
        print("home seek")
        self.write(COMMAND_HOME, 0, 0)
    
    
    def fn_checkHome(self):
        """
        starts an infinite loop that displays the state of the home sensor every 2 seconds
        """
        while 1:
            self.write(COMMAND_ATHOME, 0, 0);
            time.sleep(2)
            print("..")
            while self.ser.inWaiting():  # Or: while ser.inWaiting():
                print(str(self.readline()))
        
        
    
    def fn_moveForward(self):
        """
        interactive function to move the motor forward
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
        time.sleep(steps * 0.02)
    
    
    def fn_moveBackward(self):
        """
        interactive function to move the motor backward
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
        time.sleep(steps * 0.02)
     
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
        

    
if __name__ == "__main__":
    a = MotorControl(sys.argv[1]);
    a.interactive();
