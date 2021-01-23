import traceback
from kivy.network.urlrequest import UrlRequest
from bs4 import BeautifulSoup
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

    def update_global_str_var(self, str_val):
        self.debug_str = str_val

    def build(self):
        try:
            req = UrlRequest(url="https://www.olx.pl")
            # soup = BeautifulSoup()
            # str_var = soup.title.string

            # self.debug_str = req.result
        except Exception as e:
            self.debug_str = traceback.format_exc()

        self.debug_str = insert_newlines(self.debug_str)

        # on_release=UrlRequest(url="https://www.olx.pl"),
        button = Button(text=self.debug_str,
                        size_hint=(.5, .5),
                        pos_hint={'center_x': .5, 'center_y': .5})
        return button


if __name__ == '__main__':
    app = MainApp()
    app.run()
