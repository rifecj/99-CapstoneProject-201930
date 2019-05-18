"""
  Capstone Project.  Code to run on the EV3 robot (NOT on a laptop).
  Author:  Your professors (for the framework)
    and Sam C Alvares.
  Spring term, 2018-2019.
"""
# DONE 1:  Put your name in the above.

import mqtt_remote_method_calls as mqtt
import rosebot
import m1_robot_code as m1
import m2_robot_code as m2


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

    def set_mqtt_sender(self, mqtt_sender):
        self.mqtt_sender = mqtt_sender

    # TODO: Add methods here as needed.
    def arm_up(self, speed):
        real_speed = int(speed)
        touch = self.robot.sensor_system.touch_sensor
        self.robot.arm_and_claw.motor.turn_on(real_speed)
        while True:
            test_touch = touch.is_pressed()
            if test_touch:
                print('Sensor touched :)')
                self.robot.arm_and_claw.motor.turn_off()
                break

    def arm_to(self, x, speed):
        print('Arm to', x, speed)
        if self.cal != 1:
            self.arm_calibrate(speed)
        if x == self.robot.arm_and_claw.motor.get_position():
            return
        elif x < self.robot.arm_and_claw.motor.get_position():
            self.robot.arm_and_claw.motor.turn_on(-speed)
            while self.robot.arm_and_claw.motor.get_position() >= x:
                pass
            self.robot.arm_and_claw.motor.turn_off()
        else:
            self.robot.arm_and_claw.motor.turn_on(speed)
            while self.robot.arm_and_claw.motor.get_position() <= x:
                pass
            self.robot.arm_and_claw.motor.turn_off()

    def arm_down(self, speed):
        self.arm_to(0, speed)

    def color_go(self, color, speed):
        print(color, speed)
        number = self.robot.sensor_system.color_sensor.get_color_number_from_color_name(color)
        self.robot.drive_system.go(speed, speed)
        while True:
            current_num = self.robot.sensor_system.color_sensor.get_color()
            if current_num == number:
                self.robot.drive_system.stop()
                break

    def arm_calibrate(self, speed):
        self.cal = 1
        print('Arm Cal', speed)
        self.arm_up(speed)
        self.robot.arm_and_claw.motor.reset_position()
        self.robot.arm_and_claw.motor.turn_on(-speed)
        while abs(self.robot.arm_and_claw.motor.get_position()) <= 14.2*360:
            pass
        self.robot.arm_and_claw.motor.turn_off()
        self.robot.arm_and_claw.motor.reset_position()


def print_message_received(method_name, arguments=None):
    print()
    print("The robot's delegate has received a message")
    print("for the  ", method_name, "  method, with arguments", arguments)


# DONE: Add functions here as needed.

