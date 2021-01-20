from kivy.app import App
from kivy.uix.button import Button
from jnius import autoclass


class MainApp(App):
    def build(self):
        bt = autoclass('android.bluetooth.BluetoothManager')
        bt_adapter = bt.BluetoothAdapter.getDefaultAdapter

        button = Button(text='test2',
                      size_hint=(.5, .5),
                      pos_hint={'center_x': .5, 'center_y': .5})

        return button

if __name__ == '__main__':
    app = MainApp()
    app.run()

