from kivy.app import App
from kivy.uix.button import Button
from jnius import autoclass

where_err = 0

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
            where_err = 1
            PythonActivity = autoclass('org.kivy.android.PythonActivity')

            where_err = 2
            activity = PythonActivity.mActivity

            where_err = 3
            Context = autoclass('android.content.Context')

            where_err = 4
            vibrator = activity.getSystemService(Context.VIBRATOR_SERVICE)

            where_err = 5
            vibrator.vibrate(10000)  # the argument is in milliseconds


        except Exception as e:
            str_var = str(where_err) + str(e)



        button = Button(text=insert_newlines(str_var),
                      size_hint=(.5, .5),
                      pos_hint={'center_x': .5, 'center_y': .5})

        return button

if __name__ == '__main__':
    app = MainApp()
    app.run()

