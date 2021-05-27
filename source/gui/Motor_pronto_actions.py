#!/usr/bin/env python
#-*- coding: utf-8 -*-

import sys
import logging
import time
import threading
import serial

import Motor_pronto_comunication

logging.basicConfig(filename='MotorLog' + time.strftime("%d-%m-%y-%H-%M-%S") + '.log',
                    level=logging.DEBUG,
                    format='%(asctime)s %(message)s',
                    datefmt='%m/%d/%Y %I:%M:%S')

try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True


COMMAND_FORWARD = 0
COMMAND_BACKWARD = 1
COMMAND_HOME = 2
COMMAND_MOVE = 3
COMMAND_POS = 4
COMMAND_CHECK = 5
COMMAND_RAW = 6
COMMAND_ENABLE = 7
COMMAND_DISABLE = 8

control = None  

    
    
def init(top, gui, *args, **kwargs):
    """
    """
    global w, top_level, root, motor
    w = gui
    top_level = top
    root = top
    motor = Motor_pronto_comunication.MotorControl()


def actionBackward_step():
    """
    function called if backward step button pressed
    """
    logging.info('starts Backward_step')
    
    #angle_phantom_step.set((float(angle_phantom_step.get()) // 1.8)*1.8)    
    #steps_in_action=int(float(angle_phantom_step.get()) // 1.8)
        
    try:      
        steps = int(control.getSteps())
        motor.write(COMMAND_BACKWARD, steps, 0)        
        control.setAngle(control.getCurrentAngle() + steps)
        

        logging.info('Backward_step:Step %s'  ';position %s'
                 % (control.getSteps(), control.getCurrentAngle()) )
        
        print('Motor_pronto_actions.Backward_step')
        
    except Exception as e:
        raise
        logging.error('problem Backward_step (%s). Position %s' % (e, control.getCurrentAngle()))
        print('problems during Backward_step')

    

def actionForward_step():
    """
    """
    logging.info('starts Forward_step')
    #control.setAngle_phantom_step.set((float(angle_phantom_step.get())//1.8)*1.8)    
    

    try:
        steps = int(control.getSteps())
        motor.write(COMMAND_FORWARD, steps , 0)
        control.setAngle(control.getCurrentAngle() - steps)
        
        logging.info('Forward_step:Step '+ str(control.getSteps()) +
                      ';position '+ str(control.getCurrentAngle()))
        print('Motor_pronto_actions.Forward_step')
    
    except:
        raise
        logging.error('problem Forward_step: position %2.1f' % (control.getCurrentAngle()))
        print('problem Forward_step')
        
        

def actionHome():
    """    
    """
    
    logging.info('starts Home')
    number_steps_home = control.getCurrentAngle()
    
    try:
        if control.getCurrentAngle() < 0:
            motor.write(COMMAND_BACKWARD, int(number_steps_home) , 0)
            logging.info('Home; number steps backward:'+str(number_steps_home))
            
        else:
            motor.write(COMMAND_FORWARD, int(number_steps_home) , 0)
            logging.info('Home; number steps forward:'+str(number_steps_home))
            
        angle_phantom.set(0)
        print('Motor_pronto_actions.Home')
        
    except:
        logging.error('problem Home' + ';position ' +str(angle_phantom.get()))
        print('problem Home')
        



def actionConnect():
    """
    connects to the arduino controller
    """
    print('Connect button pressed')
    global motor 
    
    try:        
        motor.port = control.Serial_port.get()
        motor.baudrate = int(control.Serial_baudrate.get())
        motor.connect()
        logging.info('connect to port '+ control.Serial_port.get()+'baudrate '+ control.Serial_baudrate.get())        
        print ("connection successful at %s:%s" % (motor.port, motor.baudrate))
             
    except Exception as e:   
        logging.error('Not Connect to '+  control.Serial_port.get() + 'baudrate ' + control.Serial_baudrate.get())
        print('Connection not possible: %s' % e)
        
        
def actionDisable():
    """
    function called on button disable pressed
    """
    logging.info('disable')
    motor.fn_disable()
    print('Disable button pressed')
    
    
def actionEnable():
    """
    """
    logging.info('Enable')
    motor.fn_enable()
    print('Enable button pressed')
    


def actionStart():
    """
    function called on button start pressed
    """
    #parameter
    global state_automatic
    
    Initial_angle.set(round(float(Initial_angle.get())/1.8)*1.8)
    Steps.set(round(float(Steps.get())/1.8)*1.8)
    steps_in_measure=(float(Final_angle.get())-float(Initial_angle.get()))/float(Steps.get())
    if steps_in_measure<=1:
        steps_in_measure=1

    #go to initial angle    
    seekHome();    
    
    logging.info('Start automatic measure; actual angle ' + angle_phantom.get() 
                 + ' angle step: '+angle_phantom_step.get() 
                 + ' initial angle: '+Initial_angle.get()
                 + ' final angle: '+ Final_angle.get() 
                 + ' Measurement_time: '+Measurement_time.get()
                 )
                 
    state_automatic = True             
    rotation()
    print('Motor_pronto_actions.Start')    
    

def actionStop():
    """
    called on button stop pressed
    """
    global state_automatic
    state_automatic = False
    logging.info('Stop; actual angle: '+angle_phantom.get())
    print('Motor_pronto_actions.Stop')
    
    
    
def rotation():
    """
    """
    def begin_rotation():
        measure=0
        while (state_automatic == True):
            Backward_step()
            measure += 1
            time.sleep(int(Measurement_time.get())+1)
            
            if float(control.getFinalAngle() < control.getCurrentAngle() ):
                seekHome()
                break
            
            if state_automatic == False:
                Home()
                break
            
    thread = threading.Thread(target=begin_rotation)
    thread.start()
    


def actionPause():
    """
    function called when pause button is pressed
    """
    global state_automatic
    state_automatic = False
    logging.info('Paused; current angle: %2.1f' % (control.getCurrentAngle()))
    print('Pause button pressed')
    


def seekHome2():
    """
    moves the motor until home position is reached
    """
    steps_initial=int((float(Initial_angle.get())-float(angle_phantom.get()))//1.8)
    
    if steps_initial < 0:
        logging.info('Initial_step:Step ' + str(angle_phantom_step.get()) + ';position '
                 + str(angle_phantom.get()))
        motor.write(COMMAND_FORWARD, abs(steps_initial), 0)
        time.sleep(int(Measurement_time.get()))
        #sys.stdout.flush()
        
    elif steps_initial > 0: 
        motor.write(COMMAND_BACKWARD, abs(steps_initial), 0)
        logging.info('Initial_step:Step ' + str(angle_phantom_step.get()) + ';position '
                 +str(angle_phantom.get()))
        time.sleep(int(Measurement_time.get()))
        #sys.stdout.flush()
    else:
        pass
        
    angle_phantom.set(Initial_angle.get())
    


def destroy_window():
    """
    Function which closes the window.
    """
    global top_level
    logging.info('END SESSION')
    Stop()
    top_level.destroy()
    top_level = None



if __name__ == '__main__':
    import Motor_pronto_GUI
    Motor_pronto_GUI.vp_start_gui()




