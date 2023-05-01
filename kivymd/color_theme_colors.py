from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.button import MDRaisedButton

class MainApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Orange"

        return (
            MDScreen(
                MDRaisedButton(
                    text = "Primary Light",
                    pos_hint = {"center_x": .5, "center_y": .7},
                    md_bg_color = self.theme_cls.primary_light
                ),
                MDRaisedButton(
                    text = "Primary Color",
                    pos_hint = {"center_x": .5, "center_y": .5}
                ),
                MDRaisedButton(
                    text = "Primary Dark",
                    pos_hint = {"center_x": .5, "center_y": .3},
                    md_bg_color = self.theme_cls.primary_dark
                )
            )
        )
    

if __name__ == '__main__':
    MainApp().run()