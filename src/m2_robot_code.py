"""
  Capstone Project.  Code to run on the EV3 robot (NOT on a laptop).
  Author:  Your professors (for the framework)
    and Jake Powell.
  Spring term, 2018-2019.
"""
# DONE 1:  Put your name in the above.

import mqtt_remote_method_calls as mqtt
import rosebot
import m2_robot_code as m2
import m3_robot_code as m3


class MyRobotDelegate(object):
    """
    Defines methods that are called by the MQTT listener when that listener
    gets a message (name of the method, plus its arguments)
    from a LAPTOP via MQTT.
    """
    def __init__(self, robot):
        self.robot = robot  # type: rosebot.RoseBot
        self.mqtt_sender = None  # type: mqtt.MqttClient
        self.is_time_to_quit = False  # Set this to True to exit the robot code
        self.cal = 0
        Blob = self.robot.sensor_system.camera.get_biggest_blob()
        X = Blob.center
        Area = Blob.get_area()
        Area2 = Area




    def set_mqtt_sender(self, mqtt_sender):
        self.mqtt_sender = mqtt_sender

    def stop(self):
        """ Tells the robot to stop moving. """
        print_message_received("stop")
        self.robot.drive_system.stop()


    def Left_Spin(self,Left_speed,Left_distance):
        print_message_received("Left_Spin", [Left_speed, Left_distance])
        speed = -int(Left_speed)
        distance = -int(Left_distance*5.5)
        self.robot.drive_system.left_motor.turn_on(speed)
        self.robot.drive_system.right_motor.turn_on(-speed)
        self.robot.drive_system.left_motor.reset_position()
        final_spot = distance
        while True:
            if abs(self.robot.drive_system.left_motor.get_position()) >= abs(final_spot):
                self.robot.drive_system.stop()
                break

    def Right_Spin(self,Right_speed, Right_distance):
        print_message_received("Right_Spin", [Right_speed, Right_distance])
        speed = -int(Right_speed)
        distance = -int(Right_distance*5.5)
        self.robot.drive_system.right_motor.turn_on(speed)
        self.robot.drive_system.left_motor.turn_on(-speed)
        self.robot.drive_system.left_motor.reset_position()
        final_spot = distance
        while True:
            if abs(self.robot.drive_system.left_motor.get_position()) >= abs(final_spot):
                self.robot.drive_system.stop()
                break


    def Spin_until(self, X, delta, speed, big_enough):

        print_message_received("Spin_until", [X, delta, speed, big_enough])
        Speed = -int(speed)
        Big_enough = int(big_enough)
        Delta = int(delta)
        self.robot.drive_system.right_motor.turn_on(Speed)
        self.robot.drive_system.left_motor.turn_on(-Speed)
        while True:
            Blob = self.robot.sensor_system.camera.get_biggest_blob()
            if Blob.get_area() >= abs(Delta + Big_enough):
                break




        if Blob.get_area() >= abs(Big_enough + Delta):
            Current = Blob.center.x
        else:

        self.robot.drive_system.left_motor.reset_position()
        Current = Blob.center.x
        Final_spot = Delta + Current
        while True:



        # Current = Blob.center.x
        # self.robot.drive_system.left_motor.reset_position()

        # final_spot = Current




























    # TODO: Add methods here as needed.


def print_message_received(method_name, arguments=None):
    print()
    print("The robot's delegate has received a message")
    print("for the  ", method_name, "  method, with arguments", arguments)


# TODO: Add functions here as needed.

