from kivymd.app import MDApp
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import Screen, ScreenManager


screen_helper = """
ScreenManager:
    LogInScreen:
    CreateAccountScreen:
    PWManagerScreen:

<LogInScreen>:
    name: 'login'
    username: login_username
    password: login_pw


    AsyncImage:
        source: 'blackgrey.jpg'
        size: self.texture_size
        # pos_hint: {'center_x': 0.5, 'center_y': 0.5}

    AsyncImage:
        source: 'pm.png'
        width: 10
        pos_hint: {'center_x': 0.5, 'center_y': 0.8}

    MDRaisedButton:
        text:'Login'
        pos_hint: {'center_x': 0.5, 'center_y': 0.3}
        on_press: root.check_login()
        # size_hint: 0.35, 0.08

    MDTextField:
        id: login_username
        hint_text: "Username"
        helper_text: "Forgot username? Reset"
        helper_text_mode: "on_focus"
        icon_right: "account"
        icon_right_color: app.theme_cls.primary_color
        pos_hint: {'center_x':0.5, 'center_y':0.6}
        size_hint_x: None
        width: 600
        write_tab: False
        line_color_normal: app.theme_cls.primary_color
        current_hint_text_color: app.theme_cls.primary_color
        padding: 1,1
        padding_x: 20,20


    MDTextField:
        id: login_pw
        hint_text: "Password"
        icon_right: "lock"
        icon_right_color: app.theme_cls.primary_color
        pos_hint: {'center_x':0.5, 'center_y':0.5}
        size_hint_x: None
        width: 600
        write_tab: False
        password: True
        current_hint_text_color: app.theme_cls.primary_color
        line_color_normal: app.theme_cls.primary_color


    MDLabel:   
        text: "[color=ffffff]Don't have an account?[/color] [ref=Create Account][color=00ccff][b]Create Account[/b][/color][/ref]"
        on_ref_press: root.manager.current = 'create_account'
        markup: True
        halign: 'center'
        pos_hint: {'center_x':0.5, 'center_y':0.2}


<CreateAccountScreen>:
    name: 'create_account'
    new_username: create_user
    password1: create_pw_1
    password2: create_pw_2

    # MDLabel:
    #     text:'Welcome to PM'
    #     halign: 'center'
    #     valign: 'top'

    AsyncImage:
        source: 'blackgrey.jpg'
        size: self.texture_size
        # pos_hint: {'center_x': 0.5, 'center_y': 0.5}

    AsyncImage:
        source: 'pm.png'
        width: 10
        pos_hint: {'center_x': 0.5, 'center_y': 0.8}

    MDRaisedButton:
        text:'Create Account'
        pos_hint: {'center_x': 0.5, 'center_y': 0.3}
        on_press: root.check_creation()   

    MDTextField:
        id: create_user
        hint_text: "Enter Username"
        helper_text: "Forgot username? Reset"
        helper_text_mode: "on_focus"
        icon_right: "account"
        icon_right_color: app.theme_cls.primary_color
        pos_hint: {'center_x':0.5, 'center_y':0.6}
        size_hint_x: None
        width: 600
        write_tab: False
        current_hint_text_color: app.theme_cls.primary_color
        line_color_normal: app.theme_cls.primary_color


    MDTextField:
        id: create_pw_1
        hint_text: "Enter Password"
        icon_right: "lock"
        icon_right_color: app.theme_cls.primary_color
        pos_hint: {'center_x':0.5, 'center_y':0.5}
        size_hint_x: None
        width: 600
        password: True
        write_tab: False
        current_hint_text_color: app.theme_cls.primary_color
        line_color_normal: app.theme_cls.primary_color

    MDTextField:
        id: create_pw_2
        hint_text: "Confirm Password"
        icon_right: "lock"
        icon_right_color: app.theme_cls.primary_color
        pos_hint: {'center_x':0.5, 'center_y':0.4}
        size_hint_x: None
        width: 600
        password: True
        write_tab: False
        current_hint_text_color: app.theme_cls.primary_color
        line_color_normal: app.theme_cls.primary_color

    MDLabel:   
        text: '[color=ffffff]Already have an account?[/color] [ref=Log In][color=00ccff][b]Log in[/b][/color][/ref]'
        on_ref_press: root.manager.current = 'login'
        markup: True
        halign: 'center'
        pos_hint: {'center_x':0.5, 'center_y':0.2}

<PWManagerScreen>:
    name: 'pw_manager'
    MDLabel:
        text:'Welcome to PM'
        halign: 'center'


    MDRaisedButton:
        text: 'Logout'
        pos_hint: {'center_x':0.5, 'center_y':0.2}
        on_press: root.manager.current = 'login'

"""


class LogInScreen(Screen):
    scr = Screen()

    def check_login(self):
        if self.username.text == "KivyMD" and self.password.text == "kivy":
            self.change_screen("pw_manager")

    def change_screen(self, screen, *args):
        self.parent.current = screen


class CreateAccountScreen(Screen):
    scr = Screen()

    def check_creation(self):
        user = self.new_username.text
        pw1 = self.password1.text
        pw2 = self.password2.text

        if user == '':
            print("No user name")

        if pw1 != pw2:
            print('Passwords do not match')
        print(user, pw1, pw2)
        # if self.username.text == "KivyMD" and self.password.text == "kivy":
        #     self.change_screen("pw_manager")


class PWManagerScreen(Screen):
    pass


class DemoApp(MDApp):
    sm = ScreenManager()

    def build(self):
        # Colors
        # self.theme_cls.primary_hue = "A700"
        self.theme_cls.theme_style = "Light"

        self.sm.add_widget(LogInScreen(name='login'))
        self.sm.add_widget(CreateAccountScreen(name='create_account'))
        self.sm.add_widget(CreateAccountScreen(name='pw_manager'))
        screen = Builder.load_string(screen_helper)

        return screen


if __name__ == '__main__':
    DemoApp().run()
