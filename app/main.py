# from jnius import autoclass
from kivy.app import App
from kivy.uix.button import Button
from plyer import bluetooth
from jnius import autoclass
import android

PythonActivity = autoclass('org.renpy.android.PythonActivity')
activity = PythonActivity.mActivity
Context = autoclass('android.content.Context')
vibrator = activity.getSystemService(Context.VIBRATOR_SERVICE)


class MainApp(App):
    def build(self):
        str_bluetooth_info = str(bluetooth.info)
        vibrator.vibrate(10000)
        button = Button(text=str_bluetooth_info,
                      size_hint=(.5, .5),
                      pos_hint={'center_x': .5, 'center_y': .5})

        return button

if __name__ == '__main__':
    app = MainApp()
    app.run()

