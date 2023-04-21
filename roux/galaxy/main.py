from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty
from kivy.graphics import Color
from kivy.graphics import Line

class MainWidget(Widget):
    perspective_point_x = NumericProperty(0)
    perspective_point_y = NumericProperty(0)
    vertical_lines = []
    V_NB_LINES = 11
    V_LINES_SPACING = 0.1

    def __init__(self, **kwargs):
        super(MainWidget, self).__init__(**kwargs)
        # print(f"INIT W: {self.width} H: {self.height}")
        self.init_vertical_lines()
    
    def on_parent(self, widget, parent):
        # print(f"ON PARENT W: {self.width} H: {self.height}")
        pass
    
    def on_size(self, *args):
        # print(f"ON SIZE W: {self.width} H: {self.height}")
        # self.perspective_point_x = self.width/2
        # self.perspective_point_y = self.height * 3/4
        self.update_vertical_lines()
    
    def on_perspective_point_x(self, widget, value):
        # print(f"PX: {value}")
        pass
    
    def on_perspective_point_y(self, widget, value):
        # print(f"PY: {value}")
        pass

    # initiate vertical grid lines
    def init_vertical_lines(self):
        with self.canvas:
            Color(1,1,1)
            # self.line = Line()
            for i in range(self.V_NB_LINES):
                self.vertical_lines.append(Line())

    # initiate horizontal grid lines
    def update_vertical_lines(self):
        central_line_x = int(self.width/2)
        spacing = self.V_LINES_SPACING * self.width
        offset = -int(self.V_NB_LINES/2)
        for i in range(self.V_NB_LINES):
            other_line_x = int(central_line_x + offset * spacing)
            self.vertical_lines[i].points = [other_line_x, 0, other_line_x, self.height]
            print(self.vertical_lines[i].points)
            offset += 1

class GalaxyApp(App):
    pass

if __name__ == "__main__":
    GalaxyApp().run()