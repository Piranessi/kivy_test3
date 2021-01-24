import traceback
from kivy.network.urlrequest import UrlRequest
from kivy.app import App
from kivy.uix.button import Button
import socket


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
        msg = 'test msg\n'
        encoded_msg = bytes(msg, "utf-8")
        s = socket.socket()
        ip = '192.168.4.1'
        port = 3000
        try:
            s.connect((ip,port))
            s.send(msg)
            s.close()
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
