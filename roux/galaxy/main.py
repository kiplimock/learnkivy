from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty
from kivy.graphics import Color
from kivy.graphics import Line

class MainWidget(Widget):
    perspective_point_x = NumericProperty(0)
    perspective_point_y = NumericProperty(0)
    vertical_lines = []
    V_NB_LINES = 8
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

    def init_vertical_lines(self):
        with self.canvas:
            Color(1,1,1)
            for i in range(self.V_NB_LINES):
                self.vertical_lines.append(Line())

    def update_vertical_lines(self):
        central_line_x = int(self.width/2)
        spacing = self.V_LINES_SPACING * self.width
        offset = -int(self.V_NB_LINES/2) + 0.5
        for i in range(self.V_NB_LINES):
            other_line_x = int(central_line_x + offset * spacing)
            x1, y1 = self.transform(other_line_x, 0)
            x2, y2 = self.transform(other_line_x, self.height)

            self.vertical_lines[i].points = [x1, y1, x2, y2]
            offset += 1

    def transform(self, x, y):
        # return self.transform_2D(x, y)
        return self.transform_perspective(x, y)

    def transform_2D(self, x, y):
        return int(x), int(y)

    def transform_perspective(self, x, y):
        tr_y = (y / self.height) * self.perspective_point_y
        if tr_y > self.perspective_point_y:
            tr_y = self.perspective_point_y
        
        diff_x = x - self.perspective_point_x
        diff_y = self.perspective_point_y - tr_y
        proportion_y = diff_y / self.perspective_point_y

        tr_x = self.perspective_point_x + diff_x * proportion_y
        
        return int(tr_x), int(tr_y)

class GalaxyApp(App):
    pass

if __name__ == "__main__":
    GalaxyApp().run()