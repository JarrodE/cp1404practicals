"""
CP1404 - GUI program to convert miles to kilometres
Jarrod Eaton
12/11/2023
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty


MILES_TO_KM_FACTOR = 1.60934  # Constant for miles to kilometers conversion


class ConvertMilesKmApp(App):
    """Kivy App for converting miles to kilometres."""
    output_km = StringProperty('0.0')  # StringProperty for the output label

    def build(self):
        """ build the Kivy app from the kv file."""
        self.title = "Convert Miles to Kilometres"
        return Builder.load_file('convert_miles_km.kv')

    def convert_miles_to_km(self):
        """Calculate output result to widget."""
        miles = self.get_validated_miles()
        self.output_km = str(miles * MILES_TO_KM_FACTOR)

    def handle_increment(self, increment):
        """handle up/down button press, update the text input with new value, call calculation function."""
        miles = self.get_validated_miles() + increment
        self.root.ids.input_miles.text = str(miles)
        self.convert_miles_to_km()

    def get_validated_miles(self):
        """get text input from text entry widget."""
        try:
            return float(self.root.ids.input_miles.text)
        except ValueError:
            return 0.0


ConvertMilesKmApp().run()
