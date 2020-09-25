from kivy.uix.screenmanager import ScreenManager
from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.button import MDRaisedButton
from kivy.lang import Builder
from helper import username_helper, password_helper, logged

import csv
from kivy.properties import ObjectProperty


class Logged(MDScreen):
    pass

class DemoApp(MDApp):

    scr_mngr = ObjectProperty(None)

    # def change_screen(self, screen, *args):
    #     self.scr_mngr.current = screen

    def build(self):
        self.theme_cls.primary_palette = "Indigo"
        self.theme_cls.primary_hue = "A700"
        self.theme_cls.theme_style = "Light"
        screen = MDScreen()
        logged = MDScreen()

        user_button = MDRaisedButton(text="Login", pos_hint={'center_x':0.5, 'center_y':0.3},
                                       on_release=self.add_data)

        # change_button = MDRaisedButton(text="Change", pos_hint={'center_x':0.5, 'center_y':0.1},
        #                                on_release=self.change_screen("logged"))


        self.username = Builder.load_string(username_helper)
        self.password = Builder.load_string(password_helper)
        screen.add_widget(self.username)
        screen.add_widget(self.password)
        screen.add_widget(user_button)
        # screen.add_widget(change_button)
        screen.add_widget(logged)

        return screen

    def add_data(self, obj):

        with open("user_data.csv", 'a')  as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow([self.username.text, self.password.text])


if __name__ == '__main__':
    DemoApp().run()
