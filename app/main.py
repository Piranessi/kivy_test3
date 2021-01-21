import traceback
from kivy.app import App
from kivy.uix.button import Button
from jnius import autoclass

BluetoothAdapter = autoclass('android.bluetooth.BluetoothAdapter')
BluetoothDevice = autoclass('android.bluetooth.BluetoothDevice')
BluetoothSocket = autoclass('android.bluetooth.BluetoothSocket')
UUID = autoclass('java.util.UUID')

str_var = "all ok"

def insert_newlines(string, every=32):
    lines = []
    for i in range(0, len(string), every):
        lines.append(string[i:i+every])
    return '\n'.join(lines)

def get_socket_stream(name):
    paired_devices = BluetoothAdapter.getDefaultAdapter().getBondedDevices().toArray()
    str_var = str(paired_devices)
    #socket = None
    # for device in paired_devices:
    #     if device.getName() == name:
    #         socket = device.createRfcommSocketToServiceRecord(
    #             UUID.fromString("00001101-0000-1000-8000-00805F9B34FB"))
    #         recv_stream = socket.getInputStream()
    #         send_stream = socket.getOutputStream()
    #         break
    # socket.connect()
    # return recv_stream, send_stream

class MainApp(App):
    def build(self):

        try:
            get_socket_stream()
        except Exception as e:
            str_var = traceback.format_exc()

        button = Button(text=insert_newlines(str_var),
                      size_hint=(.5, .5),
                      pos_hint={'center_x': .5, 'center_y': .5})

        return button

if __name__ == '__main__':
    app = MainApp()
    app.run()
