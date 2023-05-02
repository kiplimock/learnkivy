from kivymd.app import MDApp
from kivymd.uix.widget import MDWidget
from kivymd.uix.boxlayout import MDBoxLayout

class MainApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Light" # "Dark"
        return (
            MDBoxLayout(
                MDWidget(md_bg_color = self.theme_cls.bg_light),
                MDBoxLayout(md_bg_color = self.theme_cls.bg_normal),
                MDBoxLayout(md_bg_color = self.theme_cls.bg_dark),
                MDBoxLayout(md_bg_color = self.theme_cls.bg_darkest)
            )
        )


if __name__ == "__main__":
    MainApp().run()