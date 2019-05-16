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
    # DONE: Put your GUI onto your frame (using sub-frames if you wish).

    spin_left_button = ttk.Button(frame, text="Spin Left")
    spin_right_button = ttk.Button(frame, text="Spin Right")
    spin_until = ttk.Button(frame, text = "Sprint2")
    speed_left = ttk.Entry(frame)
    distance_left = ttk.Entry(frame)
    speed_right = ttk.Entry(frame)
    distance_right = ttk.Entry(frame)

    left_spin_speed = ttk.Label(frame, text="Left wheel spin speed (0 to 100)")
    right_spin_speed = ttk.Label(frame, text="Right wheel spin speed (0 to 100)")

    left_spin_distance = ttk.Label(frame, text="Left wheel distance")
    right_spin_distance = ttk.Label(frame, text="Right wheel distance")

    frame_label.grid(row=0, column=1)
    spin_left_button.grid(row=1, column=0)
    spin_right_button.grid(row=1, column=2)
    left_spin_speed.grid(row = 2, column = 0)
    right_spin_speed.grid(row = 2, column = 2)
    left_spin_distance.grid(row = 4, column = 0)
    right_spin_distance.grid(row = 4, column = 2)
    speed_left.grid(row = 3, column = 0)
    distance_left.grid(row = 5, column = 0)
    speed_right.grid(row = 3, column = 2)
    distance_right.grid(row = 5, column = 2)
    spin_until.grid(row = 3, column = 1)

    spin_left_button['command'] = lambda: Spin_Left(speed_left, distance_left, mqtt_sender)
    spin_right_button['command'] = lambda: Spin_Right(speed_right, distance_right, mqtt_sender)
    # X = abs(speed_left)

    # spin_until['command'] = lambda: Spin_Until( X, delta, speed_right, speed_left, big_enough)


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

def Spin_Left(speed_left, distance_left, mqtt_sender):
    print("Speed of Left Spin:", speed_left.get())
    print("Distance of Left Spin:", distance_left.get())
    mqtt_sender.send_message("Left_Spin", [int(speed_left.get()), int(distance_left.get())])

def Spin_Right(speed_right, distance_right, mqtt_sender):
    print("Speed of Right Spin:", speed_right.get())
    print("Distance of Right Spin:", distance_right.get())
    mqtt_sender.send_message("Right_Spin", [int(speed_right.get()),int(distance_right.get())])

