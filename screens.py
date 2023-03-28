from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty

class MainWindow(Screen):
    
    passw = ObjectProperty(None)

    def check_pass(self):
        if self.passw.text == "pass":
            print(self.passw.text)
            self.manager.current = "second"


class SecondWindow(Screen):
    pass


class WindowManager(ScreenManager):
    pass

kv = Builder.load_file("main.kv")

class MainApp(App):
    def build(self):
        return kv



if __name__ == "__main__":
    MainApp().run()