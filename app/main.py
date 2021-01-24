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

    def run_url_request_setup_device(self, *args):
        self.button.text = 'run_url_request_setup_device: init'
        try:
            msg='test msg'
            encoded_msg = bytes(msg, "utf-8")
            s = socket.socket()
            ip = '192.168.4.1'
            port = 80
            s.connect((ip,port))
            s.send(encoded_msg)
            s.close()

            wifi_name = r'test_wifi'
            wifi_password = r"test_password"
            device_address = r'http://192.168.4.1:80/'
            url_str = device_address + '?wifi_name=' + wifi_name + r"&wifi_password=" + wifi_password
            self.result = UrlRequest(url=url_str,
                                     on_success=print('on_success.'),
                                     req_body='test-req_body',
                                     on_error=self.button_on_error)
            self.button.text = 'run_url_request_setup_device: UrlRequest done'
        except Exception as e:
            self.button.text = insert_newlines(traceback.format_exc())

    def build(self):
        self.button = Button(text="start",
                             on_release=self.run_url_request_setup_device,
                             size_hint=(.5, .5),
                             pos_hint={'center_x': .5, 'center_y': .5})
        return self.button


if __name__ == '__main__':
    app = MainApp()
    app.run()
