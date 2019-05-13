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
import m2_laptop_code as m2
import m3_laptop_code as m3


def get_my_frame(root, window, mqtt_sender):
    # Construct your frame:
    frame = ttk.Frame(window, padding=10, borderwidth=5, relief="ridge")
    frame_label = ttk.Label(frame, text="Chloe Rife")
    frame_label.grid()
    # done 2: Put your name in the above.

    # Add the rest of your GUI to your frame:
    # TODO: Put your GUI onto your frame (using sub-frames if you wish).
    r=1
    forward_speed_label = ttk.Label(frame, text="Speed")
    forward_speed_label.grid(row=r, column=0)
    forward_speed_entry = ttk.Entry(frame, width=8)
    forward_speed_entry.insert(0, "100")
    forward_speed_entry.grid(row=r, column=1)

    forward_inches_label = ttk.Label(frame, text="Inches")
    forward_inches_label.grid(row=r+1, column=0)
    forward_inches_entry = ttk.Entry(frame, width=8)
    forward_inches_entry.insert(0, "100")
    forward_inches_entry.grid(row=r+1, column=1)

    forward_button = ttk.Button(frame, text="Forward")
    forward_button.grid(row=r+2, column=0)
    forward_button['command'] = lambda: handle_forward(forward_speed_entry,forward_inches_entry,mqtt_sender)
    root.bind('<Up>', lambda: print("Forward key"))

    forward_button
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

    # TODO: Add methods here as needed.
def handle_forward(speed,len_inches,mqtt_sender):
    print('go forward {} inches at {}% speed'.format(speed,len_inches))
    mqtt_sender.send_message("forward",[speed,len_inches])


# TODO: Add functions here as needed.
