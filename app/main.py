import traceback
from kivy.network.urlrequest import UrlRequest
from kivy.app import App
from kivy.uix.button import Button


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
    result = None

    # parse in wifiname, wifipassword (with space atm crash), add encryption
    def run_url_request_setup_device(self, *args):
        wifi_name = r'test_wifi'
        wifi_password = r"test_password"
        device_address = r'http://192.168.4.1:80/'
        url_str = device_address + '?wifi_name=' + wifi_name  + r"&wifi_password=" + wifi_password
        self.result = UrlRequest(url=url_str,
                                 on_success=print('Instalacja urzadzenia zakonczona.'),
                                 req_body='test-req_body',
                                 on_error='Sprawdz polaczenie wifi z urzadzeniem.')

    def build(self):
        # try:
        #     self.run_url_request()
        #     self.debug_str = str(self.result)
        # except Exception as e:
        #     self.debug_str = traceback.format_exc()

        self.debug_str = insert_newlines(self.debug_str)
        button = Button(text=self.debug_str,
                        on_release=self.run_url_request_setup_device,
                        size_hint=(.5, .5),
                        pos_hint={'center_x': .5, 'center_y': .5})
        return button


if __name__ == '__main__':
    app = MainApp()
    app.run()
