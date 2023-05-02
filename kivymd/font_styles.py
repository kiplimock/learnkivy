from kivy.core.text import LabelBase
from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.label import MDLabel
from kivymd.font_definitions import theme_font_styles

class MainApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"

        # register the font
        LabelBase.register(
            name = "Sackers Gothic",
            fn_regular = "Sackers-Gothic-Std-Light.ttf"
        )

        # append the font to the list of theme font styles
        theme_font_styles.append("Sackers Gothic")

        # configure the font
        self.theme_cls.font_styles["Sackers Gothic"] = [
            "Sackers Gothic",
            32,
            True,
            0.15
        ]

        return (
            MDScreen(
                MDLabel(
                    text = "Sample Text",
                    halign = "center",
                    font_style = "Sackers Gothic"
                )
            )
        )
    

if __name__ == '__main__':
    MainApp().run()