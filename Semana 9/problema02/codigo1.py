from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.image import Image

class SayHello(App):
    def build(self):
        self.window = GridLayout()

        return self.window

if __name__ == "__main__":
    SayHello().run()