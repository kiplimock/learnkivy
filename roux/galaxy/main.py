from kivy.config import Config
Config.set('graphics', 'width', '900')
Config.set('graphics', 'height', '400')

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, Clock
from kivy.graphics import Color
from kivy.graphics import Line

class MainWidget(Widget):
    perspective_point_x = NumericProperty(0)
    perspective_point_y = NumericProperty(0)

    vertical_lines = []
    V_NB_LINES = 10
    V_LINES_SPACING = 0.25 # percentage of screen width

    horizontal_lines = []
    H_NB_LINES = 15
    H_LINES_SPACING = 0.1 # percentage of screen height

    SPEED = 4
    current_offset = 0

    SPEED_X = 12
    current_speed_x = 0
    current_offset_x = 0

    def __init__(self, **kwargs):
        super(MainWidget, self).__init__(**kwargs)
        # print(f"INIT W: {self.width} H: {self.height}")
        self.init_vertical_lines()
        self.init_horizontal_lines()
        Clock.schedule_interval(self.update, 1.0 / 60.0)
    
    def on_parent(self, widget, parent):
        # print(f"ON PARENT W: {self.width} H: {self.height}")
        pass
    
    def on_size(self, *args):
        # print(f"ON SIZE W: {self.width} H: {self.height}")
        # self.perspective_point_x = self.width/2
        # self.perspective_point_y = self.height * 3/4
        # self.update_vertical_lines()
        # self.update_horizontal_lines()
        pass
    
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
            other_line_x = int(central_line_x + offset * spacing + self.current_offset_x)
            x1, y1 = self.transform(other_line_x, 0)
            x2, y2 = self.transform(other_line_x, self.height)

            self.vertical_lines[i].points = [x1, y1, x2, y2]
            offset += 1
    
    def init_horizontal_lines(self):
        with self.canvas:
            Color(1,1,1)
            for i in range(self.H_NB_LINES):
                self.horizontal_lines.append(Line())

    def update_horizontal_lines(self):
        central_line_x = int(self.width/2)
        spacing = self.V_LINES_SPACING * self.width
        offset = -int(self.V_NB_LINES/2) + 0.5

        xmin = central_line_x + offset * spacing + self.current_offset_x
        xmax = central_line_x - offset * spacing + self.current_offset_x
        spacing_y = self.H_LINES_SPACING * self.height

        for i in range(self.H_NB_LINES):
            other_line_y = i * spacing_y - self.current_offset
            x1, y1 = self.transform(xmin, other_line_y)
            x2, y2 = self.transform(xmax, other_line_y)

            self.horizontal_lines[i].points = [x1, y1, x2, y2]

    def transform(self, x, y):
        # return self.transform_2D(x, y)
        return self.transform_perspective(x, y)

    def transform_2D(self, x, y):
        return int(x), int(y)

    def transform_perspective(self, x, y):
        lin_y = (y / self.height) * self.perspective_point_y
        if lin_y > self.perspective_point_y:
            lin_y = self.perspective_point_y
        
        diff_x = x - self.perspective_point_x
        diff_y = self.perspective_point_y - lin_y
        factor_y = (diff_y / self.perspective_point_y) ** 4

        tr_x = self.perspective_point_x + diff_x * factor_y
        tr_y = self.perspective_point_y * (1 - factor_y)
        
        return int(tr_x), int(tr_y)

    def on_touch_down(self, touch):
        if touch.x < self.width/2:
            self.current_speed_x = self.SPEED_X
        else:
            self.current_speed_x = -self.SPEED_X
    
    def on_touch_up(self, touch):
        self.current_speed_x = 0


    def update(self, dt):
        # print(f"dt: {dt}, 1/60: {1/60}")
        time_factor = dt * 60
        self.update_vertical_lines()
        self.update_horizontal_lines()
        self.current_offset += self.SPEED * time_factor
        self.current_offset_x += self.current_speed_x * time_factor

        spacing_y = self.H_LINES_SPACING * self.height
        if self.current_offset >= spacing_y:
            self.current_offset -= spacing_y

class GalaxyApp(App):
    pass

if __name__ == "__main__":
    GalaxyApp().run()