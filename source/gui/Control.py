import tkinter as tk
import tkinter.ttk as ttk
    
class Control:
    """
    As changes in the textboxes directly change the tk variable, 
    this class encapsulates calls to get the values in float format
    """
    
    def __init__(self):
        """
        initializes all the tkinter variables
        """
        self.serial_port = tk.StringVar(value='/dev/ttyUSB0') # device name  
        self.serial_baudrate = tk.StringVar(value='9600')     # baud rate
        
        self.measurement_time = tk.StringVar(value='0')       # time per position, in seconds
        self.step = tk.StringVar(value='1.8')   #
        self.initial_angle = tk.StringVar(value='0')     # initial angle for a sweep
        self.final_angle = tk.StringVar(value='180')     # final angle for a sweep
        
        self.steps = tk.StringVar(value='1.8')           # current number of steps??
        
        self.angle_phantom = tk.StringVar(value='0')     # current angle of the phantom


    def getInitAngle(self):
        """
        returns the initial angle, in steps away from home
        """
        pass

    
    def getFinalAngle(self):
        """
        @return the final angle, in steps away from home. Data is stored in a tktext
        """
        return float(self.final_angle.get())


    def getCurrentAngle(self):
        """
        @return the stored angle of the motor in steps. Data is stored in a tktext
        """    
        return float(self.angle_phantom.get())

    def setAngle(self, angle):
        """
        """
        self.angle_phantom.set(angle)
        
        
    def getSteps(self):
        """
        returns how many degrees / step
        """
        return int(float(self.step.get()))
    
    
    
