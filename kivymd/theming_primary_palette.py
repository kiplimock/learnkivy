from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.button import MDRectangleFlatButton

class Example(MDApp):
    '''
    The primary palette is the name of color scheme that the application use
    and all the major material components will have the color of the specified 
    color theme
    '''

    def build(self):
        self.theme_cls.theme_style = "Dark" # "Light"
        self.theme_cls.primary_palette = "Orange" # "Purple", "Red"
        self.theme_cls.primary_hue = "500" # "200"

        return (
            MDScreen(
                MDRectangleFlatButton(
                    text = "Hello World",
                    pos_hint = {"center_x": .5, "center_y": .5}
                )
            )
        )

if __name__ == '__main__':
    Example().run()