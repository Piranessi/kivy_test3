from kivy.app import App
from kivy.uix.button import Button
from jnius import autoclass

def insert_newlines(string, every=32):
    lines = []
    for i in range(0, len(string), every):
        lines.append(string[i:i+every])
    return '\n'.join(lines)

class MainApp(App):
    def build(self):
        str_var = "all ok2"
        bt = autoclass('android.bluetooth.BluetoothAdapter')
        try:
            bt_adapter = bt.getDefaultAdapter()

            # This one works with SDL2
            PythonActivity = autoclass('org.kivy.android.PythonActivity')

            activity = PythonActivity.mActivity

            Context = autoclass('android.content.Context')
            vibrator = activity.getSystemService(Context.VIBRATOR_SERVICE)

            vibrator.vibrate(10000)  # the argument is in milliseconds


        except Exception as e:
            str_var = str(e)



        button = Button(text=insert_newlines(str_var),
                      size_hint=(.5, .5),
                      pos_hint={'center_x': .5, 'center_y': .5})

        return button

if __name__ == '__main__':
    app = MainApp()
    app.run()

