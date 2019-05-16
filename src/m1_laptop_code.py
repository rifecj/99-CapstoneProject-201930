"""
  Capstone Project.  Code to run on a LAPTOP (NOT the robot).
  Displays the Graphical User Interface (GUI) and communicates with the robot.

  Authors:  Your professors (for the framework)
    and Chloe Rife.
  Spring term, 2018-2019.
"""
# done 1:  Put your name in the above.

import tkinter
from tkinter import ttk
import mqtt_remote_method_calls as mqtt
#import m2_laptop_code as m2
#import m3_laptop_code as m3



def get_my_frame(root, window, mqtt_sender):
    # Construct your frame:
    frame = ttk.Frame(window, padding=10, borderwidth=5, relief="ridge")
    frame_label = ttk.Label(frame, text="Chloe Rife")
    frame_label.grid()
    # done 2: Put your name in the above.

    # Add the rest of your GUI to your frame:
    # TODO: Put your GUI onto your frame (using sub-frames if you wish).
    #----------------------------------------------------------------
    #Forward GUI
    # ----------------------------------------------------------------
    r=2
    forward_speed_label = ttk.Label(frame, text="Speed")
    forward_speed_label.grid(row=r, column=0)
    forward_speed_entry = ttk.Entry(frame, width=10)
    forward_speed_entry.insert(0, "100")
    forward_speed_entry.grid(row=r, column=1)

    forward_inches_label = ttk.Label(frame, text="Inches")
    forward_inches_label.grid(row=r+1, column=0)
    forward_inches_entry = ttk.Entry(frame, width=10)
    forward_inches_entry.insert(0, "5")
    forward_inches_entry.grid(row=r+1, column=1)

    forward_button = ttk.Button(frame, text="Forward", width=10)
    forward_button.grid(row=r-1, column=1)
    forward_button['command'] = lambda: handle_forward(int(forward_speed_entry.get()),int(forward_inches_entry.get()),mqtt_sender)
    # ----------------------------------------------------------------
    # Backward GUI
    # ----------------------------------------------------------------
    c=2
    backward_speed_label = ttk.Label(frame, text="Speed")
    backward_speed_label.grid(row=r, column=c)
    backward_speed_entry = ttk.Entry(frame, width=10)
    backward_speed_entry.insert(0, "100")
    backward_speed_entry.grid(row=r, column=c)

    backward_inches_label = ttk.Label(frame, text="Inches")
    backward_inches_label.grid(row=r+1, column=c)
    backward_inches_entry = ttk.Entry(frame, width=10)
    backward_inches_entry.insert(0, "5")
    backward_inches_entry.grid(row=r+1, column=c)

    backward_button = ttk.Button(frame, text="Backward", width=10)
    backward_button.grid(row=r-1, column=c)
    backward_button['command'] = lambda: handle_backward(int(forward_speed_entry.get()),int(forward_inches_entry.get()),mqtt_sender)

    # ----------------------------------------------------------------
    # Forward Until GUI
    # ----------------------------------------------------------------
    c = 4
    forward_until_speed_label = ttk.Label(frame, text="Speed")
    forward_until_speed_label.grid(row=r, column=c)
    forward_until_speed_entry = ttk.Entry(frame, width=10)
    forward_until_speed_entry.insert(0, "100")
    forward_until_speed_entry.grid(row=r, column=c+1)

    forward_until_dist_label = ttk.Label(frame, text="Distance")
    forward_until_dist_label.grid(row=r + 1, column=c)
    forward_until_dist_entry = ttk.Entry(frame, width=10)
    forward_until_dist_entry.insert(0, "5")
    forward_until_dist_entry.grid(row=r+1, column=c+1)

    forward_until_delta_label = ttk.Label(frame, text="Leeway")
    forward_until_delta_label.grid(row=r + 2, column=c)
    forward_until_delta_entry = ttk.Entry(frame, width=10)
    forward_until_delta_entry.insert(0, "5")
    forward_until_delta_entry.grid(row=r+2, column=c+1)

    forward_until_button = ttk.Button(frame, text="Forward Until", width=10)
    forward_until_button.grid(row=r - 1, column=c)
    forward_until_button['command'] = lambda: handle_forward_until(int(forward_until_speed_entry.get()),
                                                                   int(forward_until_dist_entry.get()),
                                                                   int(forward_until_delta_entry.get()),
                                                                   mqtt_sender)
    # Return your frame:
    return frame


class MyLaptopDelegate(object):
    """
    Defines methods that are called by the MQTT listener when that listener
    gets a message (name of the method, plus its arguments)
    from the ROBOT via MQTT.
    """
    def __init__(self, root):
        self.root = root  # type: tkinter.Tk
        self.mqtt_sender = None  # type: mqtt.MqttClient

    def set_mqtt_sender(self, mqtt_sender):
        self.mqtt_sender = mqtt_sender

    # todo: Add methods here as needed.



# TODO: Add functions here as needed.

def handle_forward(speed,len_inches,mqtt_sender):
    print('go forward {} inches at {}% speed'.format(len_inches,speed))
    mqtt_sender.send_message("forward",[speed,len_inches])

def handle_backward(speed,len_inches,mqtt_sender):
    print('go backward {} inches at {}% speed'.format(len_inches,speed))
    mqtt_sender.send_message("backward",[speed,len_inches])
def handle_forward_until(speed, dist, delta, mqtt_sender):
    print('go forward at {}% speed until {} +/- {}')
    mqtt_sender.send_message("forward_until", [speed, dist, delta])