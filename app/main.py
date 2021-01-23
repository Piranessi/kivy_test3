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
            req = UrlRequest(url="https://www.olx.pl",on_success=self.update_global_str_var("success"))
            # soup = BeautifulSoup()
            # str_var = soup.title.string
        except Exception as e:
            str_var = traceback.format_exc()

        str_var = insert_newlines(str_var)
        button = Button(text=str_var,
                      size_hint=(.5, .5),
                      pos_hint={'center_x': .5, 'center_y': .5})
        return button


if __name__ == '__main__':
    app = MainApp()
    app.run()
