"""
  Capstone Project.  Code to run on a LAPTOP (NOT the robot).
  Displays the Graphical User Interface (GUI) and communicates with the robot.

  Authors:  Your professors (for the framework)
    and Sam C Alvares.
  Spring term, 2018-2019.
"""
# TODO 1:  Put your name in the above.

import tkinter
from tkinter import ttk

import mqtt_remote_method_calls as mqtt
import m1_laptop_code as m1
import m2_laptop_code as m2


def get_my_frame(root, window, mqtt_sender):
    # Construct your frame:
    frame = ttk.Frame(window, padding=10, borderwidth=5, relief="ridge")
    frame_label = ttk.Label(frame, text="Sam Alvares")
    frame_label.grid()
    # DONE 2: Put your name in the above.

    # Add the rest of your GUI to your frame:
    # TODO: Put your GUI onto your frame (using sub-frames if you wish).
    arm_up_button = ttk.Button(frame, text="Arm up")
    arm_calibrate_button = ttk.Button(frame, text="Calibrate arm")
    arm_to_entry = ttk.Entry(frame)
    arm_to_button = ttk.Button(frame, text="Arm to:")
    speed_entry = ttk.Entry(frame)
    label2 = ttk.Label(frame, text="Speed:")
    arm_down_button = ttk.Button(frame, text="Arm down")

    arm_up_button['command'] = lambda: handle_arm_up(speed_entry, mqtt_sender)
    arm_down_button['command'] = lambda: handle_arm_down(speed_entry, mqtt_sender)
    arm_calibrate_button['command'] = lambda: handle_calibrate(speed_entry, mqtt_sender)
    arm_to_button['command'] = lambda: handle_arm_to(speed_entry, mqtt_sender)

    speed_entry.insert(0, '100')

    arm_up_button.grid(row=1, column=0)
    arm_calibrate_button.grid(row=5, column=0)
    arm_to_button.grid(row=2, column=0)
    arm_to_entry.grid(row=2, column=1)
    arm_down_button.grid(row=3, column=0)
    label2.grid(row=4, column=0)
    speed_entry.grid(row=4, column=1)

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
def handle_arm_up(speed_entry, mqqt_sender):
    print('Arm up message:', speed_entry.get())
    mqqt_sender.send_message("arm_up", [speed_entry.get()])


def handle_arm_down(speed_entry, mqqt_sender):
    print('Arm down message:', speed_entry.get())
    mqqt_sender.send_message("arm_down", [speed_entry.get()])


def handle_calibrate(speed_entry, mqqt_sender):
    print('Arm calibrate message:', speed_entry.get())
    mqqt_sender.send_message("arm_calibrate", [speed_entry.get()])


def handle_arm_to(speed_entry, mqqt_sender):
    print('Arm to message:', speed_entry.get())
    mqqt_sender.send_message("arm_to", [speed_entry.get()])