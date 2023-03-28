from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.graphics import (Rectangle, Color, Line)

class Draw(Widget):

    def __init__(self, **kwargs):
        super(Draw, self).__init__(**kwargs)

        with self.canvas:
            # a rectangle
            Color(1, 0, 0, 0.5, mode='rgba')
            self.rect = Rectangle(pos=(0,0), size=(50,50))
            # a line
            Color(1, 0, 1, 0.5, mode='rgba')
            Line(points=(0,0,20,50,100,30,200,200))

    btn = ObjectProperty(None)

    def on_touch_down(self, touch):
        # move rectangle on click
        self.rect.pos = touch.pos
        print("Mouse Down", touch)

    def on_touch_move(self, touch):
        # move reactangle using mouse
        self.rect.pos = touch.pos
        print("Mouse Move", touch)

class DrawApp(App):
    def build(self):
        return Draw()
    

if __name__ == "__main__":
    DrawApp().run()