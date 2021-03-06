"""
  Capstone Project.  Code to run on the EV3 robot (NOT on a laptop).
  Author:  Your professors (for the framework)
    and PUT_YOUR_NAME_HERE.
  Spring term, 2018-2019.
"""
# TODO 1:  Put your name in the above.

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
        self.cal=0

    def set_mqtt_sender(self, mqtt_sender):
        self.mqtt_sender = mqtt_sender

    def go(self, left_motor_speed, right_motor_speed):
        """ Tells the robot to go (i.e. move) using the given motor speeds. """
        print_message_received("go", [left_motor_speed, right_motor_speed])
        self.robot.drive_system.go(left_motor_speed, right_motor_speed)

    # # TODO: Add methods here as needed.
    # def forward(self,speed,inches):
    #     self.robot.drive_system.go(speed,speed)
    #     while True:
    #         if self.robot.drive_system.left_motor.get_position() >

    def forward(self,speed,len_inches):
        self.robot.drive_system.left_motor.reset_position()
        len_deg=len_inches*(360/(3.14*1.5))
        self.robot.drive_system.go(speed,speed)
        while True:
            print_message_received("forward", [speed, len_inches])
            print(self.robot.drive_system.left_motor.get_position())
            if self.robot.drive_system.left_motor.get_position() >= len_deg:
                self.robot.drive_system.stop()
                break

    def backward(self,speed,len_inches):
        self.robot.drive_system.left_motor.reset_position()
        len_deg=len_inches*(360/(3.14*1.5))
        self.robot.drive_system.go(-speed,-speed)
        while True:
            print(self.robot.drive_system.left_motor.get_position())
            if self.robot.drive_system.left_motor.get_position() <= -len_deg:
                self.robot.drive_system.stop()
                break

    def forward_until(self,speed, dist):
        self.robot.drive_system.go(speed,speed)
        while True:
            print_message_received("forward_until",[speed,dist])
            dist_away_in=self.robot.sensor_system.ir_proximity_sensor.get_distance_in_inches()
            print(dist_away_in)
            if dist_away_in < dist:
                self.robot.drive_system.stop()
                break



# TODO: Add functions here as needed.

def print_message_received(method_name, arguments):
    print()
    print("The robot's delegate has received a message")
    print("for the  ", method_name, "  method, with arguments", arguments)