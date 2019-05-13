"""
  Capstone Project.  Code to run on a LAPTOP (NOT the robot).
  Displays the Graphical User Interface (GUI) and communicates with the robot.

  Authors:  Your professors (for the framework)
    and Jake B Powell.
  Spring term, 2018-2019.
"""
# DONE: Put your name in the above.

import tkinter
from tkinter import ttk

import mqtt_remote_method_calls as mqtt
import m1_laptop_code as m1
import m3_laptop_code as m3


def get_my_frame(root, window, mqtt_sender):
    # Construct your frame:
    frame = ttk.Frame(window, padding=10, borderwidth=5, relief="ridge")
    frame_label = ttk.Label(frame, text="Jake Powell")
    frame_label.grid()
    # DONE 2: Put your name in the above.

    # Add the rest of your GUI to your frame:
    # TODO: Put your GUI onto your frame (using sub-frames if you wish).

    spin_left_button = ttk.Button(frame, text="Spin Left")
    spin_right_button = ttk.Button(frame, text="Spin Right")
    speed = ttk.Entry(frame)
    distance = ttk.Entry(frame)
    speed2 = ttk.Entry(frame)
    distance2 = ttk.Entry(frame)

    frame_label.grid(row=0, column=1)
    spin_left_button.grid(row=1, column=0)
    spin_right_button.grid(row=1, column=2)
    speed2.grid(row = 2, column = 0)
    distance2.grid(row = 3, column = 0)
    speed.grid(row = 2, column = 2)
    distance.grid(row = 3, column = 2)


# def spin_left(speed, distance):
#     Spin_left = ttk.Button(frame, text = "Spin Left")
#     Spin_left.grid(row = 1, column = 1)

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


# TODO: Add functions here as needed.
