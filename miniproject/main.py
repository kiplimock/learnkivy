from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.label  import Label
from kivy.uix.popup import Popup
from kivy.properties import ObjectProperty


class WindowManager(ScreenManager):
    pass

sm = WindowManager()

def invalidForm():
    pop = Popup(
        title = "Invalid Form",
        content = Label(text="Invalid username or password."),
        size_hint = (None, None),
        size = (400, 400),
    )
    pop.open()

class CreateAccountWindow(Screen):
    # object properties
    username = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)

    def submit(self):
        # check for empty forms
        if self.username.text == "" or self.email.text == "" or self.password.text == "":
            invalidForm()
        elif "@" in self.email.text and "." in self.email.text:
            print("Cool")
            # self.login()
            
    # switch to the login screen
    def login(self):
        self.reset()
        sm.current = "login"

    # reset create account screen
    def reset(self):
        self.username.text = ""
        self.email.text = ""
        self.password.text = ""

kv = Builder.load_file("main.kv")

screens = [CreateAccountWindow(name="create")]
for screen in screens:
    sm.add_widget(screen)

sm.current = "create"

class MainApp(App):
    def build(self):
        return sm

if __name__ == "__main__":
    MainApp().run()