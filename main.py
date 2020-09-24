from kivymd.app import MDApp
# from kivymd.uix.label import MDLabel, MDIcon
from kivymd.uix.screen import MDScreen
from kivymd.uix.button import MDFlatButton, MDRectangleFlatButton, MDRaisedButton
from kivy.lang import Builder
from helper import username_helper, password_helper
from kivy.core.window import Window


Window.size = (500, 800)


class DemoApp(MDApp):

    # def build(self):
    #     self.theme_cls.primary_palette = "Yellow"
    #     self.theme_cls.primary_hue = "700"
    #     self.theme_cls.theme_style = "Dark"
    #     # label = MDLabel(text="Password Manager", halign='center', theme_text_color='Custom',
    #     #                 text_color=(108 / 255.0, 14 / 255.0, 232 / 255.0, 1),
    #     #                 font_style='H3')
    #     # icon_label = MDIcon(icon='language-python', halign="center")
    #     screen = MDScreen()
    #     btn_flat = MDRectangleFlatButton(text='Sign Up', pos_hint={'center_x':0.5, 'center_y':0.5})
    #     # icon_btn = MDFloatingActionButton(icon="android", pos_hint={'center_x':0.5, 'center_y':0.5})
    #     # float_btn = MDFloatingActionButton()
    #     screen.add_widget(btn_flat)
    #     return screen

    def build(self):
        self.theme_cls.primary_palette = "Indigo"
        self.theme_cls.primary_hue = "A700"
        self.theme_cls.theme_style = "Light"
        screen = MDScreen()
        # username = MDTextField(text="Enter Username", pos_hint={"center_x": 0.5, "center_y": 0.5}, size_hint_x=None, width=400)
        user_button = MDRaisedButton(text="Search", pos_hint={'center_x':0.5, 'center_y':0.3},
                                       on_release=self.show_data)
        self.username = Builder.load_string(username_helper)
        self.password = Builder.load_string(password_helper)
        screen.add_widget(self.username)
        screen.add_widget(self.password)
        screen.add_widget(user_button)
        return screen

    def show_data(self, obj):
        print(self.username.text)


if __name__ == '__main__':
    DemoApp().run()
