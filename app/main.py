import traceback
from kivy.network.urlrequest import UrlRequest
from kivy.app import App
from kivy.uix.button import Button
import socket
import json
import struct

########### related to sending/receiving over socket
#BLOB = Binary Large OBject
#msg has to be serialized JSON
def read_blob(sock, size):
    buf = b''
    while len(buf) != size:
        ret = sock.recv(size - len(buf))
        if not ret:
            raise ConnectionError("Socket closed")
        buf += ret
    return buf


def read_long(sock):
    size = struct.calcsize("L")
    data = read_blob(sock, size)
    return struct.unpack("L", data)[0] #struct.unpack() returns tuple even one element inside


def read_from_socket(sock):
    buffer_size = read_long(sock)
    data = read_blob(sock, buffer_size)
    return json.loads(data)
####################################################


def insert_newlines(string, every=32):
    if len(string) > 32:
        lines = []
        for i in range(0, len(string), every):
            lines.append(string[i:i+every])
        return '\n'.join(lines)
    else:
        return string


class MainApp(App):
    debug_str = 'init'
    button = None
    result = None

    def button_on_error(self,*args):
        self.button.text = 'connection error'

    def setup_device(self, *args):
        self.button.text = 'setup: init'


        cfg_dict = {
            'wifi_ssid': 'Zyku',
            'wifi_password': 'jarecki1!'
        }
        cfg_dict_json = json.dumps(cfg_dict)
        print('len:', len(cfg_dict_json))

        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        ip = '192.168.4.1'
        port = 3000

        try:
            sock.connect((ip,port))
            sock.sendall(struct.pack("L", len(cfg_dict_json)))
            sock.sendall(bytes(cfg_dict_json,encoding='utf-8'))
            sock.close()
            self.button.text = 'msg sent, connection closed'
        except Exception as e:
            self.button.text = insert_newlines(traceback.format_exc())

    def build(self):
        self.button = Button(text="start",
                             on_release=self.setup_device,
                             size_hint=(.5, .5),
                             pos_hint={'center_x': .5, 'center_y': .5})
        return self.button


if __name__ == '__main__':
    app = MainApp()
    app.run()
