from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty

class MainWidget(Widget):
    perspective_point_x = NumericProperty(0)
    perspective_point_y = NumericProperty(0)

    def __init__(self, **kwargs):
        super(MainWidget, self).__init__(**kwargs)
        # print(f"INIT W: {self.width} H: {self.height}")
    
    def on_parent(self, widget, parent):
        # print(f"ON PARENT W: {self.width} H: {self.height}")
        pass
    
    def on_size(self, *args):
        # print(f"ON SIZE W: {self.width} H: {self.height}")
        # self.perspective_point_x = self.width/2
        # self.perspective_point_y = self.height * 3/4
        pass
    
    def on_perspective_point_x(self, widget, value):
        # print(f"PX: {value}")
        pass
    
    def on_perspective_point_y(self, widget, value):
        # print(f"PY: {value}")
        pass

class GalaxyApp(App):
    pass

if __name__ == "__main__":
    GalaxyApp().run()