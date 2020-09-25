username_helper = """
MDTextField:
    hint_text: "Enter Username"
    helper_text: "Forgot username? Reset"
    helper_text_mode: "on_focus"
    icon_right: "chevron-right"
    icon_right_color: app.theme_cls.primary_color
    pos_hint: {'center_x':0.5, 'center_y':0.5}
    size_hint_x: None
    width: 600
"""

password_helper = """
MDTextField:
    hint_text: "Enter Password"
    helper_text: "Forgot password? Reset"
    helper_text_mode: "on_focus"
    icon_right: "chevron-right"
    icon_right_color: app.theme_cls.primary_color
    pos_hint: {'center_x':0.5, 'center_y':0.4}
    size_hint_x: None
    width: 600
"""

logged = """
Screen:
name: 'logged'

            Toolbar:
                id: toolbar
                title: "Welcome ! "
                pos_hint: {'center_x': 0.5, 'center_y': 0.97}
                md_bg_color: app.theme_cls.primary_color
                background_palette: 'DeepPurple'
                background_hue: 'A400'
                left_action_items: [['arrow-left', partial(root.change_screen, 'screen1') ]]
                right_action_items: [['animation', lambda x: MDThemePicker().open()]]

            MDLabel:
                font_style: 'Title'
                theme_text_color: 'Primary'
                text: "Data :"
                height: self.texture_size[1] + dp(3)
                halign: 'center'
                pos_hint: {'center_x': 0.5, 'center_y': 0.85}
    
"""
