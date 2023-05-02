from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.button import MDRectangleFlatButton

class MainApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.set_colors(
            "Blue", "600", "50", "800", "Teal", "600", "100", "800"
        )
        
        return (
            MDScreen(
                MDRectangleFlatButton(
                    text = "Hello World",
                    pos_hint = {"center_x": .5, "center_y": .5}
                )
            )
        )


if __name__ == "__main__":
    MainApp().run()