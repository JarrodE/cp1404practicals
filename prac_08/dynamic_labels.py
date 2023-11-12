from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label


class DynamicLabelsApp(App):
    """A Kivy application that dynamically creates a label for each name in a predefined list."""
    def __init__(self, **kwargs):
        """Initialise the app with a list of names."""
        super().__init__(**kwargs)
        self.names_list = ["Alice", "Bob", "Charlie", "Diana"]

    def build(self):
        """Build the app's GUI by loading the Kivy layout file and creating label widgets
        for each name in the list."""
        self.root = Builder.load_file('dynamic_labels.kv')
        for name in self.names_list:
            label = Label(text=name)
            self.root.ids.main.add_widget(label)
        return self.root


DynamicLabelsApp().run()
