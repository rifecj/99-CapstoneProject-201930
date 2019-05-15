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
        current_position = self.robot.drive_system.left_motor.reset_position()
        final_spot = distance + current_position
        while True:
            if self.robot.drive_system.left_motor.get_position() >= final_spot:
                self.robot.drive_system.stop()
                break

        # current_position = self.robot.drive_system.left_motor.get_position()
        # final_spot = current_position + distance
        #
        # while True:
        #     if self.robot.drive_system.left_motor.get_position() <= final_spot:
        #         self.robot.drive_system.stop()
        #         break









    def Right_Spin(self,Right_speed, Right_distance):
        print_message_received("Right_Spin", [Right_speed, Right_distance])
        speed = int(Right_speed)
        distance = int(Right_distance*5.5)
        self.robot.drive_system.right_motor.turn_on(speed)
        self.robot.drive_system.left_motor.turn_on(-speed)
        current_position = self.robot.drive_system.right_motor.reset_position()
        final_spot = distance + current_position
        while True:
            if self.robot.drive_system.right_motor.get_position() >= final_spot:
                self.robot.drive_system.stop()
                break









    # TODO: Add methods here as needed.


def print_message_received(method_name, arguments=None):
    print()
    print("The robot's delegate has received a message")
    print("for the  ", method_name, "  method, with arguments", arguments)


# TODO: Add functions here as needed.

