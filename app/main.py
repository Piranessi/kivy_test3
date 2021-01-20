# from jnius import autoclass
from kivy.app import App
from kivy.uix.button import Button
from plyer import battery
from plyer import vibrator
from plyer import bluetooth

class MainApp(App):
    def build(self):
        str_bluetooth_info = str(bluetooth.info)
        vibrator.vibrate(time=2)
        button = Button(text=str_bluetooth_info,
                      size_hint=(.5, .5),
                      pos_hint={'center_x': .5, 'center_y': .5})

        return button

if __name__ == '__main__':
    app = MainApp()
    app.run()

