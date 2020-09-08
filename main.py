from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from kivy.utils import get_color_from_hex
from kivy.properties import StringProperty
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout

Window.clearcolor = get_color_from_hex('#454343')


class WelcomeWindow(Screen):
    pass


class Rootwi(BoxLayout, Screen):
    the_text = StringProperty()

    def __init__(self, **kwargs):
        super(Rootwi, self).__init__(**kwargs)
        self.the_text = ''

    def calculation(self):
        try:
            self.the_text = str(eval(self.the_text))
        except:
            self.the_text = 'error'

    def check_error(self):
        if self.the_text == 'error':
            self.the_text = ''

    def percentage(self):
        try:
            self.the_text = str(float(self.the_text)/100)
        except:
            self.the_text = 'error'


class WindowManager(ScreenManager):
    pass


builder = Builder.load_file('calculator.kv')


class CalculatorApp(App):
    def build(self):
        return builder


if __name__ == '__main__':
    CalculatorApp().run()
