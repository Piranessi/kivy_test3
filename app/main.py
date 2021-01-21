import traceback
from kivy.app import App
from kivy.uix.button import Button
from jnius import autoclass

BluetoothAdapter = autoclass('android.bluetooth.BluetoothAdapter')
BluetoothDevice = autoclass('android.bluetooth.BluetoothDevice')
BluetoothSocket = autoclass('android.bluetooth.BluetoothSocket')
UUID = autoclass('java.util.UUID')


def insert_newlines(string, every=32):
    if len(string) > 32:
        lines = []
        for i in range(0, len(string), every):
            lines.append(string[i:i+every])
        return '\n'.join(lines)
    else:
        return string


def get_socket_stream():
    paired_devices = BluetoothAdapter.getDefaultAdapter().getBondedDevices().toArray()
    res = ''
    socket = None

    if paired_devices is not None:
        for device in paired_devices:
            res += str(device.getName())
            if device.getName() == 'Mi True Wireless EBs Basic_R':
                socket = device.createRfcommSocketToServiceRecord(UUID.fromString('00001101-0000-1000-8000-00805F9B34FB'))

                recv_stream = socket.getInputStream()
                send_stream = socket.getOutputStream()

                socket.connect()

    else:
        res = 'empty'

    return res

    #socket = None
    # for device in paired_devices:
    #     if device.getName() == name:
    #         socket = device.createRfcommSocketToServiceRecord(UUID.randomUUID())
    #             fromString("00001101-0000-1000-8000-00805F9B34FB"))
    #         recv_stream = socket.getInputStream()
    #         send_stream = socket.getOutputStream()
    #         break
    # socket.connect()
    # return recv_stream, send_stream
    #pass

# def callback(instance):
#     print('test', instance.text)

class MainApp(App):
    def build(self):
        str_var = "all g"

        try:
            str_var = get_socket_stream()
        except Exception as e:
            str_var = traceback.format_exc()

        str_var = insert_newlines(str_var)
        button = Button(text=str_var,
                      size_hint=(.5, .5),
                      pos_hint={'center_x': .5, 'center_y': .5})

        #button.bind(on_press=callback)

        return button

if __name__ == '__main__':
    app = MainApp()
    app.run()
