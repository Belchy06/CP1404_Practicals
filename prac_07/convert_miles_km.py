"""
CP1404/CP5632 Practical
Kivy GUI program to convert miles to KM
William Belcher, Engineering @ JCU
Started 19/04/2020
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window

__author__ = 'William Belcher'

from kivy.properties import StringProperty

CONVERSION_RATIO = 1.60934


class ConvertMilesKmApp(App):
    """ ConvertMilesKmApp is a Kivy App for converting miles to km """

    result = StringProperty()

    def build(self):
        """ build the Kivy app from the kv file """
        Window.size = (800, 600)
        self.title = "Convert Miles to Kilometeres"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_increment(self, increment):
        if self.root.ids.input_miles.text == "":
            new_value = 0.0 + increment
        else:
            new_value = float(self.root.ids.input_miles.text) + increment

        self.root.ids.input_miles.text = str(new_value)

    def handle_convert(self, miles_string):
        try:
            # Check if input is a number by trying to convert miles_string to a float
            miles = float(miles_string)
            self.result = str(miles * CONVERSION_RATIO)
        except ValueError:
            self.root.ids.input_miles.text = str(0)


ConvertMilesKmApp().run()
