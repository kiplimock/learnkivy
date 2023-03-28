from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty

class Touch(Widget):

    btn = ObjectProperty(None)

    def on_touch_down(self, touch):
        self.btn.opacity = 0.5
        print("Mouse Down", touch)

    def on_touch_move(self, touch):
        print("Mouse Move", touch)

    def on_touch_up(self, touch):
        self.btn.opacity = 1
        print("Mouse Up", touch)

class TouchApp(App):
    def build(self):
        return Touch()
    

if __name__ == "__main__":
    TouchApp().run()