import traceback
from kivy.app import App
from kivy.uix.button import Button
from jnius import autoclass

BluetoothAdapter = autoclass('android.bluetooth.BluetoothAdapter')
BluetoothDevice = autoclass('android.bluetooth.BluetoothDevice')
BluetoothSocket = autoclass('android.bluetooth.BluetoothSocket')
InputStreamReader = autoclass('java.io.InputStreamReader')
BufferedReader = autoclass('java.io.BufferedReader')
UUID = autoclass('java.util.UUID')
defaultCharBufferSize = 8192  # default Oracle value


def insert_newlines(string, every=32):
    if len(string) > 32:
        lines = []
        for i in range(0, len(string), every):
            lines.append(string[i:i+every])
        return '\n'.join(lines)
    else:
        return string


def get_socket_stream():
    res = ''
    device_name = 'Mi True Wireless EBs Basic_R'
    bt_adapter = BluetoothAdapter.getDefaultAdapter()

    if bt_adapter is not None:
        if bt_adapter.isEnabled():
            paired_devices = bt_adapter.getBondedDevices().toArray()
            rfcomm_socket = None
            if paired_devices is not None:
                for device in paired_devices:
                    res += str(device.getName()) #debug line
                    if device.getName() == device_name:
                        if device.bluetoothEnabled:
                            rfcomm_socket = device.createRfcommSocketToServiceRecord(UUID.fromString('0000112f-0000-1000-8000-00805f9b34fb'))
                            if rfcomm_socket is not None:
                                try:
                                    if rfcomm_socket.port <= 0:
                                        rfcomm_socket = device.createRfcommSocket(1)  # set the port explicitly
                                        if not rfcomm_socket.connected:
                                            rfcomm_socket.connect()
                                    else:
                                        if not rfcomm_socket.connected:
                                            rfcomm_socket.connect()
                                    if rfcomm_socket.connected:
                                        res = '[b]Connected[/b]'
                                except Exception as e:
                                    res = traceback.format_exc()
                                if rfcomm_socket.connected:
                                    reader = InputStreamReader(rfcomm_socket.getInputStream(), 'utf8')
                                    recv_stream = BufferedReader(reader, defaultCharBufferSize)
                                    send_stream = rfcomm_socket.getOutputStream()
            else:
                res = 'empty'
    return res



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
