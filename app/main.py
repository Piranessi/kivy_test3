# from jnius import autoclass
from kivy.app import App
from kivy.uix.button import Button
from plyer import battery
from plyer import vibrator

class MainApp(App):
    def build(self):
        time = 2
        vibrator.vibrate(time=time)
        button = Button(text='Hello from Kivy',
                      size_hint=(.5, .5),
                      pos_hint={'center_x': .5, 'center_y': .5})

        return button

if __name__ == '__main__':
    app = MainApp()
    app.run()