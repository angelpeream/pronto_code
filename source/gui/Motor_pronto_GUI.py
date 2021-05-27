
#  -*- coding: utf-8 -*-

import sys
import tkinter as tk
import tkinter.ttk as ttk
import Motor_pronto_actions
from Motor_pronto_actions import control
from Control import Control



def vp_start_gui():
    '''Starting point'''
    global val, w, root, control
    root = tk.Tk()
    #Motor_pronto_actions.set_Tk_var()
    Motor_pronto_actions.control = Control()
    control = Motor_pronto_actions.control
    top = Toplevel1 (root)
    Motor_pronto_actions.init(root, top)
    root.mainloop()

w = None



def create_Toplevel1(rt, *args, **kwargs):
    '''create_Toplevel1(root, *args, **kwargs)'''
    global w, w_win, root
    #rt = root
    root = rt
    w = tk.Toplevel(root)
    #Motor_pronto_actions.set_Tk_var()
    top = Toplevel1 (w)
    Motor_pronto_actions.init(w, top, *args, **kwargs)
    return (w, top)




def destroy_Toplevel1():
    '''End point'''
    global w
    w.destroy()
    w = None



class Toplevel1:
    def __init__(self, top=None):
        '''toplevel configuration.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.',background=_bgcolor)
        self.style.configure('.',foreground=_fgcolor)
        self.style.configure('.',font="TkDefaultFont")
        self.style.map('.',background=
            [('selected', _compcolor), ('active',_ana2color)])

        top.geometry("600x446+344+237")
        top.minsize(120, 1)
        top.maxsize(1284, 701)
        top.resizable(1,  1)
        top.title("New Toplevel")
        top.configure(background="#d9d9d9")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")
        
        #####################################################################
        #                                                                   #
        #Control                                                            #
        #                                                                   #
        #####################################################################
        self.Labelframe1 = tk.LabelFrame(top)
        self.Labelframe1.place(relx=0.017, rely=0.022, relheight=0.655
                , relwidth=0.25)
        self.Labelframe1.configure(relief='groove')
        self.Labelframe1.configure(foreground="black")
        self.Labelframe1.configure(text='''Control''')
        self.Labelframe1.configure(background="#d9d9d9")
        self.Labelframe1.configure(highlightbackground="#d9d9d9")
        self.Labelframe1.configure(highlightcolor="black")

        self.Control_port = tk.Entry(self.Labelframe1)
        self.Control_port.place(relx=0.467, rely=0.103, height=20, relwidth=0.493
                , bordermode='ignore')
        self.Control_port.configure(background="white")
        self.Control_port.configure(disabledforeground="#a3a3a3")
        self.Control_port.configure(font="TkFixedFont")
        self.Control_port.configure(foreground="#000000")
        self.Control_port.configure(highlightbackground="#d9d9d9")
        self.Control_port.configure(highlightcolor="black")
        self.Control_port.configure(insertbackground="black")
        self.Control_port.configure(selectbackground="blue")
        self.Control_port.configure(selectforeground="white")
        self.Control_port.configure(textvariable=control.serial_port)
        
        self.Label5 = tk.Label(self.Labelframe1)
        self.Label5.place(relx=0.067, rely=0.103, height=21, width=44
                , bordermode='ignore')
        self.Label5.configure(activebackground="#f9f9f9")
        self.Label5.configure(activeforeground="black")
        self.Label5.configure(background="#d9d9d9")
        self.Label5.configure(disabledforeground="#a3a3a3")
        self.Label5.configure(foreground="#000000")
        self.Label5.configure(highlightbackground="#d9d9d9")
        self.Label5.configure(highlightcolor="black")
        self.Label5.configure(text='''Port''')

        self.Label6 = tk.Label(self.Labelframe1)
        self.Label6.place(relx=0.067, rely=0.202, height=21, width=54
                , bordermode='ignore')
        self.Label6.configure(activebackground="#f9f9f9")
        self.Label6.configure(activeforeground="black")
        self.Label6.configure(background="#d9d9d9")
        self.Label6.configure(disabledforeground="#a3a3a3")
        self.Label6.configure(foreground="#000000")
        self.Label6.configure(highlightbackground="#d9d9d9")
        self.Label6.configure(highlightcolor="black")
        self.Label6.configure(text='''Baudrate''')

        self.Control_baudrate = tk.Entry(self.Labelframe1)
        self.Control_baudrate.place(relx=0.467, rely=0.202, height=20
                , relwidth=0.493, bordermode='ignore')
        self.Control_baudrate.configure(background="white")
        self.Control_baudrate.configure(disabledforeground="#a3a3a3")
        self.Control_baudrate.configure(font="TkFixedFont")
        self.Control_baudrate.configure(foreground="#000000")
        self.Control_baudrate.configure(highlightbackground="#d9d9d9")
        self.Control_baudrate.configure(highlightcolor="black")
        self.Control_baudrate.configure(insertbackground="black")
        self.Control_baudrate.configure(selectbackground="blue")
        self.Control_baudrate.configure(selectforeground="white")
        self.Control_baudrate.configure(textvariable=control.serial_baudrate)

        self.Button_connect = tk.Button(self.Labelframe1)
        self.Button_connect.place(relx=0.2, rely=0.411, height=34, width=87
                , bordermode='ignore')
        self.Button_connect.configure(activebackground="#ececec")
        self.Button_connect.configure(activeforeground="#000000")
        self.Button_connect.configure(background="#d9d9d9")
        self.Button_connect.configure(command=Motor_pronto_actions.actionConnect)
        self.Button_connect.configure(disabledforeground="#a3a3a3")
        self.Button_connect.configure(foreground="#000000")
        self.Button_connect.configure(highlightbackground="#d9d9d9")
        self.Button_connect.configure(highlightcolor="black")
        self.Button_connect.configure(pady="0")
        self.Button_connect.configure(text='''Connect''')

        self.Button_Disable = tk.Button(self.Labelframe1)
        self.Button_Disable.place(relx=0.2, rely=0.582, height=34, width=87
                , bordermode='ignore')
        self.Button_Disable.configure(activebackground="#ececec")
        self.Button_Disable.configure(activeforeground="#000000")
        self.Button_Disable.configure(background="#d9d9d9")
        self.Button_Disable.configure(command=Motor_pronto_actions.actionDisable)
        self.Button_Disable.configure(disabledforeground="#a3a3a3")
        self.Button_Disable.configure(foreground="#000000")
        self.Button_Disable.configure(highlightbackground="#d9d9d9")
        self.Button_Disable.configure(highlightcolor="black")
        self.Button_Disable.configure(pady="0")
        self.Button_Disable.configure(text='''Disable''')

        self.Button_Enable = tk.Button(self.Labelframe1)
        self.Button_Enable.place(relx=0.2, rely=0.753, height=34, width=87
                , bordermode='ignore')
        self.Button_Enable.configure(activebackground="#ececec")
        self.Button_Enable.configure(activeforeground="#000000")
        self.Button_Enable.configure(background="#d9d9d9")
        self.Button_Enable.configure(command=Motor_pronto_actions.actionEnable)
        self.Button_Enable.configure(disabledforeground="#a3a3a3")
        self.Button_Enable.configure(foreground="#000000")
        self.Button_Enable.configure(highlightbackground="#d9d9d9")
        self.Button_Enable.configure(highlightcolor="black")
        self.Button_Enable.configure(pady="0")
        self.Button_Enable.configure(text='''Enable''')
        
        #####################################################################
        #                                                                   #
        #Automatic                                                          #
        #                                                                   #
        #####################################################################
        self.Labelframe2 = tk.LabelFrame(top)
        self.Labelframe2.place(relx=0.283, rely=0.022, relheight=0.655
                , relwidth=0.7)
        self.Labelframe2.configure(relief='groove')
        self.Labelframe2.configure(foreground="black")
        self.Labelframe2.configure(text='''Automatic''')
        self.Labelframe2.configure(background="#d9d9d9")
        self.Labelframe2.configure(highlightbackground="#d9d9d9")
        self.Labelframe2.configure(highlightcolor="black")

        self.Automatic_initial_angle = tk.Entry(self.Labelframe2)
        self.Automatic_initial_angle.place(relx=0.595, rely=0.168, height=20, relwidth=0.2
                , bordermode='ignore')
        self.Automatic_initial_angle.configure(background="white")
        self.Automatic_initial_angle.configure(disabledforeground="#a3a3a3")
        self.Automatic_initial_angle.configure(font="TkFixedFont")
        self.Automatic_initial_angle.configure(foreground="#000000")
        self.Automatic_initial_angle.configure(highlightbackground="#d9d9d9")
        self.Automatic_initial_angle.configure(highlightcolor="black")
        self.Automatic_initial_angle.configure(insertbackground="black")
        self.Automatic_initial_angle.configure(selectbackground="blue")
        self.Automatic_initial_angle.configure(selectforeground="white")
        self.Automatic_initial_angle.configure(textvariable=control.initial_angle)

        self.Label1 = tk.Label(self.Labelframe2)
        self.Label1.place(relx=0.19, rely=0.168, height=21, width=124
                , bordermode='ignore')
        self.Label1.configure(activebackground="#f9f9f9")
        self.Label1.configure(activeforeground="black")
        self.Label1.configure(background="#d9d9d9")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(highlightbackground="#d9d9d9")
        self.Label1.configure(highlightcolor="black")
        self.Label1.configure(text='''Initial angle(deg)''')

        self.Label2 = tk.Label(self.Labelframe2)
        self.Label2.place(relx=0.214, rely=0.305, height=21, width=104
                , bordermode='ignore')
        self.Label2.configure(activebackground="#f9f9f9")
        self.Label2.configure(activeforeground="black")
        self.Label2.configure(background="#d9d9d9")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(foreground="#000000")
        self.Label2.configure(highlightbackground="#d9d9d9")
        self.Label2.configure(highlightcolor="black")
        self.Label2.configure(text='''Final Angle(deg)''')

        self.Automatic_final_angle = tk.Entry(self.Labelframe2)
        self.Automatic_final_angle.place(relx=0.595, rely=0.305, height=20, relwidth=0.2
                , bordermode='ignore')
        self.Automatic_final_angle.configure(background="white")
        self.Automatic_final_angle.configure(disabledforeground="#a3a3a3")
        self.Automatic_final_angle.configure(font="TkFixedFont")
        self.Automatic_final_angle.configure(foreground="#000000")
        self.Automatic_final_angle.configure(highlightbackground="#d9d9d9")
        self.Automatic_final_angle.configure(highlightcolor="black")
        self.Automatic_final_angle.configure(insertbackground="black")
        self.Automatic_final_angle.configure(selectbackground="blue")
        self.Automatic_final_angle.configure(selectforeground="white")
        self.Automatic_final_angle.configure(textvariable=control.final_angle)
        self.Label3 = tk.Label(self.Labelframe2)
        self.Label3.place(relx=0.23, rely=0.442, height=21, width=84
                , bordermode='ignore')
        self.Label3.configure(activebackground="#f9f9f9")
        self.Label3.configure(activeforeground="black")
        self.Label3.configure(background="#d9d9d9")
        self.Label3.configure(disabledforeground="#a3a3a3")
        self.Label3.configure(foreground="#000000")
        self.Label3.configure(highlightbackground="#d9d9d9")
        self.Label3.configure(highlightcolor="black")
        self.Label3.configure(text='''Angle step(deg)''')

        self.Automatic_steps = tk.Entry(self.Labelframe2)
        self.Automatic_steps.place(relx=0.595, rely=0.442, height=20, relwidth=0.2
                , bordermode='ignore')
        self.Automatic_steps.configure(background="white")
        self.Automatic_steps.configure(disabledforeground="#a3a3a3")
        self.Automatic_steps.configure(font="TkFixedFont")
        self.Automatic_steps.configure(foreground="#000000")
        self.Automatic_steps.configure(highlightbackground="#d9d9d9")
        self.Automatic_steps.configure(highlightcolor="black")
        self.Automatic_steps.configure(insertbackground="black")
        self.Automatic_steps.configure(selectbackground="blue")
        self.Automatic_steps.configure(selectforeground="white")
        self.Automatic_steps.configure(textvariable=control.steps)

        self.Label4 = tk.Label(self.Labelframe2)
        self.Label4.place(relx=0.238, rely=0.575, height=21, width=124
                , bordermode='ignore')
        self.Label4.configure(activebackground="#f9f9f9")
        self.Label4.configure(activeforeground="black")
        self.Label4.configure(background="#d9d9d9")
        self.Label4.configure(disabledforeground="#a3a3a3")
        self.Label4.configure(foreground="#000000")
        self.Label4.configure(highlightbackground="#d9d9d9")
        self.Label4.configure(highlightcolor="black")
        self.Label4.configure(text='''Measurement time(seg)''')

        self.Entry4 = tk.Entry(self.Labelframe2)
        self.Entry4.place(relx=0.595, rely=0.575, height=20, relwidth=0.2
                , bordermode='ignore')
        self.Entry4.configure(background="white")
        self.Entry4.configure(disabledforeground="#a3a3a3")
        self.Entry4.configure(font="TkFixedFont")
        self.Entry4.configure(foreground="#000000")
        self.Entry4.configure(highlightbackground="#d9d9d9")
        self.Entry4.configure(highlightcolor="black")
        self.Entry4.configure(insertbackground="black")
        self.Entry4.configure(selectbackground="blue")
        self.Entry4.configure(selectforeground="white")
        self.Entry4.configure(textvariable=control.measurement_time)

        self.Button_Start = tk.Button(self.Labelframe2)
        self.Button_Start.place(relx=0.071, rely=0.719, height=54, width=77
                , bordermode='ignore')
        self.Button_Start.configure(activebackground="#ececec")
        self.Button_Start.configure(activeforeground="#000000")
        self.Button_Start.configure(background="#d9d9d9")
        self.Button_Start.configure(command=Motor_pronto_actions.actionStart)
        self.Button_Start.configure(disabledforeground="#a3a3a3")
        self.Button_Start.configure(foreground="#000000")
        self.Button_Start.configure(highlightbackground="#d9d9d9")
        self.Button_Start.configure(highlightcolor="black")
        self.Button_Start.configure(pady="0")
        self.Button_Start.configure(text='''Start''')

        self.Button_Stop = tk.Button(self.Labelframe2)
        self.Button_Stop.place(relx=0.738, rely=0.719, height=54, width=77
                , bordermode='ignore')
        self.Button_Stop.configure(activebackground="#ececec")
        self.Button_Stop.configure(activeforeground="#000000")
        self.Button_Stop.configure(background="#d9d9d9")
        self.Button_Stop.configure(command=Motor_pronto_actions.actionStop)
        self.Button_Stop.configure(disabledforeground="#a3a3a3")
        self.Button_Stop.configure(foreground="#000000")
        self.Button_Stop.configure(highlightbackground="#d9d9d9")
        self.Button_Stop.configure(highlightcolor="black")
        self.Button_Stop.configure(pady="0")
        self.Button_Stop.configure(text='''Stop''')

        self.Button_Pausa = tk.Button(self.Labelframe2)
        self.Button_Pausa.place(relx=0.405, rely=0.719, height=54, width=77
                , bordermode='ignore')
        self.Button_Pausa.configure(activebackground="#ececec")
        self.Button_Pausa.configure(activeforeground="#000000")
        self.Button_Pausa.configure(background="#d9d9d9")
        self.Button_Pausa.configure(command=Motor_pronto_actions.actionPause)
        self.Button_Pausa.configure(disabledforeground="#a3a3a3")
        self.Button_Pausa.configure(foreground="#000000")
        self.Button_Pausa.configure(highlightbackground="#d9d9d9")
        self.Button_Pausa.configure(highlightcolor="black")
        self.Button_Pausa.configure(pady="0")
        self.Button_Pausa.configure(text='''Pausa''')
        #####################################################################
        #                                                                   #
        #Manual                                                             #
        #                                                                   #
        #####################################################################
        
        self.Labelframe3 = tk.LabelFrame(top)
        self.Labelframe3.place(relx=0.283, rely=0.717, relheight=0.256
                , relwidth=0.7)
        self.Labelframe3.configure(relief='groove')
        self.Labelframe3.configure(foreground="black")
        self.Labelframe3.configure(text='''Manual''')
        self.Labelframe3.configure(background="#d9d9d9")
        self.Labelframe3.configure(highlightbackground="#d9d9d9")
        self.Labelframe3.configure(highlightcolor="black")

        self.Manual_angle_step = tk.Entry(self.Labelframe3)
        self.Manual_angle_step.place(relx=0.048, rely=0.565, height=20, relwidth=0.2
                , bordermode='ignore')
        self.Manual_angle_step.configure(background="white")
        self.Manual_angle_step.configure(disabledforeground="#a3a3a3")
        self.Manual_angle_step.configure(font="TkFixedFont")
        self.Manual_angle_step.configure(foreground="#000000")
        self.Manual_angle_step.configure(highlightbackground="#d9d9d9")
        self.Manual_angle_step.configure(highlightcolor="black")
        self.Manual_angle_step.configure(insertbackground="black")
        self.Manual_angle_step.configure(selectbackground="blue")
        self.Manual_angle_step.configure(selectforeground="white")
        self.Manual_angle_step.configure(textvariable=control.angle_phantom
                                         )

        self.Label7 = tk.Label(self.Labelframe3)
        self.Label7.place(relx=0.024, rely=0.298, height=20, width=114
                , bordermode='ignore')
        self.Label7.configure(activebackground="#f9f9f9")
        self.Label7.configure(activeforeground="black")
        self.Label7.configure(background="#d9d9d9")
        self.Label7.configure(disabledforeground="#a3a3a3")
        self.Label7.configure(foreground="#000000")
        self.Label7.configure(highlightbackground="#d9d9d9")
        self.Label7.configure(highlightcolor="black")
        self.Label7.configure(text='''Angle by step(deg)''')

        self.Button_StepForward = tk.Button(self.Labelframe3)
        self.Button_StepForward.place(relx=0.286, rely=0.323, height=64, width=97
                , bordermode='ignore')
        self.Button_StepForward.configure(activebackground="#ececec")
        self.Button_StepForward.configure(activeforeground="#000000")
        self.Button_StepForward.configure(background="#d9d9d9")
        self.Button_StepForward.configure(command=Motor_pronto_actions.actionForward_step)
        self.Button_StepForward.configure(disabledforeground="#a3a3a3")
        self.Button_StepForward.configure(foreground="#000000")
        self.Button_StepForward.configure(highlightbackground="#d9d9d9")
        self.Button_StepForward.configure(highlightcolor="black")
        self.Button_StepForward.configure(pady="0")
        self.Button_StepForward.configure(text='''1 Step Forward''')

        self.Button_StepBackward = tk.Button(self.Labelframe3)
        self.Button_StepBackward.place(relx=0.524, rely=0.323, height=64
                , width=97, bordermode='ignore')
        self.Button_StepBackward.configure(activebackground="#ececec")
        self.Button_StepBackward.configure(activeforeground="#000000")
        self.Button_StepBackward.configure(background="#d9d9d9")
        self.Button_StepBackward.configure(command=Motor_pronto_actions.actionBackward_step)
        self.Button_StepBackward.configure(disabledforeground="#a3a3a3")
        self.Button_StepBackward.configure(foreground="#000000")
        self.Button_StepBackward.configure(highlightbackground="#d9d9d9")
        self.Button_StepBackward.configure(highlightcolor="black")
        self.Button_StepBackward.configure(pady="0")
        self.Button_StepBackward.configure(text='''1 Step Backward''')

        self.Button_Home = tk.Button(self.Labelframe3)
        self.Button_Home.place(relx=0.762, rely=0.323, height=64, width=97
                , bordermode='ignore')
        self.Button_Home.configure(activebackground="#ececec")
        self.Button_Home.configure(activeforeground="#000000")
        self.Button_Home.configure(background="#d9d9d9")
        self.Button_Home.configure(command=Motor_pronto_actions.actionHome)
        self.Button_Home.configure(disabledforeground="#a3a3a3")
        self.Button_Home.configure(foreground="#000000")
        self.Button_Home.configure(highlightbackground="#d9d9d9")
        self.Button_Home.configure(highlightcolor="black")
        self.Button_Home.configure(pady="0")
        self.Button_Home.configure(text='''Home''')
        
        #####################################################################
        #                                                                   #
        #Angle_phantom                                                      #
        #                                                                   #
        #####################################################################
        self.TLabelframe1 = ttk.Labelframe(top)
        self.TLabelframe1.place(relx=0.017, rely=0.717, relheight=0.256
                , relwidth=0.25)
        self.TLabelframe1.configure(relief='')
        self.TLabelframe1.configure(text='''Angle Phantom(deg)''')

        self.Angle_phantom = tk.Label(self.TLabelframe1)
        self.Angle_phantom.place(relx=0.133, rely=0.263, height=71, width=94
                , bordermode='ignore')
        self.Angle_phantom.configure(activebackground="#f9f9f9")
        self.Angle_phantom.configure(activeforeground="black")
        self.Angle_phantom.configure(background="#d9d9d9")
        self.Angle_phantom.configure(disabledforeground="#a3a3a3")
        self.Angle_phantom.configure(font="-family {Segoe UI} -size 20 -weight bold")
        self.Angle_phantom.configure(foreground="#000000")
        self.Angle_phantom.configure(highlightbackground="#d9d9d9")
        self.Angle_phantom.configure(highlightcolor="black")
        self.Angle_phantom.configure(textvariable=control.angle_phantom)

if __name__ == '__main__':
    vp_start_gui()





