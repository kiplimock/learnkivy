from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.label  import Label
from kivy.uix.popup import Popup
from kivy.properties import ObjectProperty
from database import Database


class WindowManager(ScreenManager):
    pass

sm = WindowManager()
db = Database("miniproject/users.txt")

def invalidForm():
    pop = Popup(
        title = "Invalid Form",
        content = Label(text="Please fill in all inputs with valid information."),
        size_hint = (None, None),
        size = (400, 400),
    )
    pop.open()

def invalidLogin():
    pop = Popup(
        title = "Invalid Login",
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
            self.login()
            
    # switch to the login screen
    def login(self):
        self.reset()
        sm.current = "login"

    # reset create account screen
    def reset(self):
        self.username.text = ""
        self.email.text = ""
        self.password.text = ""


class LoginWindow(Screen):
    email = ObjectProperty(None)
    password = ObjectProperty(None)

    def loginBtn(self):
        if db.validate(self.email.text, self.password.text):
            MainWindow.current = self.email.text
            self.reset()
            sm.current = "main"
        else:
            invalidLogin()
    
    def createBtn(self):
        self.reset()
        sm.current = "create"

    def reset(self):
        self.email.text = ""
        self.password.text = ""

class MainWindow(Screen):
    n = ObjectProperty(None)
    created = ObjectProperty(None)
    email = ObjectProperty(None)
    current = ""

    def logOut(self):
        sm.current = "login"

    def on_enter(self, *args):
        password, name, created = db.get_user(self.current)
        self.n.text = "Account Name: " + name
        self.email.text = "Email: " + self.current
        self.created.text = "Created On: " + created

kv = Builder.load_file("main.kv")

screens = [LoginWindow(name="login"), CreateAccountWindow(name="create"),MainWindow(name="main")]
for screen in screens:
    sm.add_widget(screen)

sm.current = "create"

class MainApp(App):
    def build(self):
        return sm

if __name__ == "__main__":
    MainApp().run()