from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class MyGrid(GridLayout):
    def __init__(self, **kwargs):
        # main grid layout
        super(MyGrid, self).__init__(**kwargs)
        self.cols = 1

        # inner grid layout within the main grid
        self.inside = GridLayout()
        self.inside.cols = 2

        # adding widgets to the inner grid 
        self.inside.add_widget(Label(text="First Name: "))
        self.first_name = TextInput(multiline=False)
        self.inside.add_widget(self.first_name)

        self.inside.add_widget(Label(text="Last Name: "))
        self.last_name = TextInput(multiline=False)
        self.inside.add_widget(self.last_name)

        self.inside.add_widget(Label(text="Email: "))
        self.email = TextInput(multiline=False)
        self.inside.add_widget(self.email)

        # adding the inner grid to the main grid as a widget
        self.add_widget(self.inside)

        # the button is part of the main grid, not the inner grid
        self.submit = Button(text="Submit", font_size=40)
        self.submit.bind(on_press=self.pressed)
        self.add_widget(self.submit)
    
    def pressed(self, instance):
        first_name = self.first_name.text
        last_name = self.last_name.text
        email = self.email.text
        print(f"First Name: {first_name}, Last Name: {last_name}, Email: {email}")
        self.first_name.text = ""
        self.last_name.text = ""
        self.email.text = ""

class MyApp(App):
    def build(self):
        return MyGrid()
    
if __name__ == '__main__':
    MyApp().run()