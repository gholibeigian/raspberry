# RPi.GPIO
import RPi.GPIO as gpio
from time import sleep
import sys
from rpi_lcd import LCD


class Iot_raspberry:
    # str(self.user_in_yellow_bool),str(self.user_in_red_bool), str(count), str(current_min_distance),  str(int(self.distance_measurer.distance_datetime[0][3])),str(buzzer),str(red_on_off)

    def __init__(self, user_in_yellow_bool, user_in_red_bool, count, current_min_distance, direction, degree, buzzer,
                 blink):  # TODO: Add direction!
        gpio.setmode(gpio.BOARD)  # gpio.BCM

        # setup - INPUT or OUTPUT
        # LED BLINK
        gpio.setup(7, gpio.OUT)  # gpio.IN
        self.blink_bool = blink  # to control the blink led

        # RGB-LED
        gpio.setup(33, gpio.OUT)  # set GPIO 17 as output for white led
        gpio.setup(31, gpio.OUT)  # set GPIO 27 as output for red led
        gpio.setup(29, gpio.OUT)  # set GPIO 22 as output for red led
        self.yellow_area_bool = user_in_yellow_bool
        self.violet_area_bool = user_in_red_bool
        self.green_area_bool = False

        # Buzzer
        # buzzer_pin = 37
        gpio.setup(37, gpio.OUT)  # gpio.IN
        self.buzzer_bool = buzzer

        # LCD
        self.count = count
        self.min_distance = current_min_distance
        self.degree = degree
        self.direction = direction
        self.lcd = LCD()

        # Program:
        try:
            while True:

                # RGB-LED
                if self.yellow_area_bool == False and self.violet_area_bool == False:
                    green_area_bool = True
                if self.green_area_bool == True:
                    gpio.output(29, 1)
                    gpio.output(33, 1)
                    gpio.output(31, 0)
                if self.violet_area_bool == True:
                    gpio.output(31, 1)
                    gpio.output(33, 0)
                    gpio.output(29, 0)
                if self.yellow_area_bool == True:
                    gpio.output(33, 1)
                    gpio.output(29, 0)
                    gpio.output(31, 0)

                # BLINK LED
                if self.blink_bool == True:
                    gpio.output(7, True)
                    sleep(0.5)
                    gpio.output(7, False)
                    sleep(0.5)
                else:
                    gpio.output(7, False)

                # BUZZER
                if self.buzzer_bool == True:
                    self.buzzer = gpio.PWM(37, 1000)  # set frequece 1000
                    for i in range(0, 5):
                        self.buzzer.start(50)
                        sleep(0.4)
                        self.buzzer.stop()
                        sleep(0.7)
                    self.buzzer_bool = False  # just one time!

                # I2C_LCD:
                if (self.count != 0):
                    self.lcd.text("Count:" + str(self.count) + " Next in", 1)
                    self.lcd.text(
                        str(self.min_distance) + "m '" + str(self.direction) + "' " + str(self.degree) + " deg", 2)
                    # print(message1)
                    # pause()
                else:
                    self.lcd.text("No one detected!", 1)
                    self.lcd.text("Have a nice day!", 2)

        except KeyboardInterrupt:
            # gpio.output(31, 0)
            # gpio.output(29, 0)
            # gpio.output(33, 0)
            # gpio.output(7, False)
            # gpio.cleanup()
            # sys.exit()
            print("Goodbye from Kazem:)")
            pass
        finally:
            sleep(0.5)
            self.lcd.clear()
            gpio.output(31, 0)
            gpio.output(29, 0)
            gpio.output(33, 0)
            gpio.output(7, False)
            gpio.cleanup()
            sys.exit()
    # def perform(self):


if __name__ == "__main__":
    # user_in_yellow_bool,user_in_red_bool,count,current_min_distance,direction,degree,buzzer,blink):# TODO: Add direction!
    test_iot = Iot_raspberry(True, False, 23, 20, 'NW', 278, True, False)
