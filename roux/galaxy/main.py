from kivy.config import Config
Config.set('graphics', 'width', '900')
Config.set('graphics', 'height', '400')

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, Clock
from kivy.graphics import Color
from kivy.graphics import Line
from kivy.core.window import Window
from kivy import platform

class MainWidget(Widget):
    from transforms import transform, transform_2D, transform_perspective
    from user_actions import keyboard_closed, on_keyboard_down, on_keyboard_up, on_touch_down, on_touch_up

    perspective_point_x = NumericProperty(0)
    perspective_point_y = NumericProperty(0)

    vertical_lines = []
    V_NB_LINES = 4
    V_LINES_SPACING = 0.1 # percentage of screen width

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
        self.init_vertical_lines()
        self.init_horizontal_lines()

        if self.is_desktop():
            self._keyboard = Window.request_keyboard(self.keyboard_closed, self)
            self._keyboard.bind(on_key_down=self.on_keyboard_down)
            self._keyboard.bind(on_key_up=self.on_keyboard_up)

        Clock.schedule_interval(self.update, 1.0 / 60.0)
    
    def is_desktop(self):
        if platform in ('linux', 'win', 'macosx'):
            return True
        return False

    def init_vertical_lines(self):
        with self.canvas:
            Color(1,1,1)
            for i in range(self.V_NB_LINES):
                self.vertical_lines.append(Line())

    def get_line_x_from_index(self, index):
        central_line_x = self.perspective_point_x
        spacing = self.V_LINES_SPACING * self.width
        offset = index - 0.5

        other_line_x = central_line_x + offset * spacing + self.current_offset_x
        return other_line_x

    def get_line_y_from_index(self, index):
        spacing_y = self.H_LINES_SPACING * self.height
        other_line_y = index * spacing_y - self.current_offset
        return other_line_y


    def update_vertical_lines(self):
        start_index = -int(self.V_NB_LINES / 2) + 1
        for i in range(start_index, start_index + self.V_NB_LINES):
            other_line_x = self.get_line_x_from_index(i)

            x1, y1 = self.transform(other_line_x, 0)
            x2, y2 = self.transform(other_line_x, self.height)
            self.vertical_lines[i].points = [x1, y1, x2, y2]
    
    def init_horizontal_lines(self):
        with self.canvas:
            Color(1,1,1)
            for i in range(self.H_NB_LINES):
                self.horizontal_lines.append(Line())

    def update_horizontal_lines(self):
        start_index = -int(self.V_NB_LINES / 2) + 1
        end_index = start_index + self.V_NB_LINES - 1

        xmin = self.get_line_x_from_index(start_index)
        xmax = self.get_line_x_from_index(end_index)

        for i in range(self.H_NB_LINES):
            other_line_y = self.get_line_y_from_index(i)
            x1, y1 = self.transform(xmin, other_line_y)
            x2, y2 = self.transform(xmax, other_line_y)

            self.horizontal_lines[i].points = [x1, y1, x2, y2]

    def update(self, dt):
        time_factor = dt * 60
        self.update_vertical_lines()
        self.update_horizontal_lines()
        # self.current_offset += self.SPEED * time_factor

        spacing_y = self.H_LINES_SPACING * self.height
        if self.current_offset >= spacing_y:
            self.current_offset -= spacing_y
        
        # self.current_offset_x += self.current_speed_x * time_factor

class GalaxyApp(App):
    pass

if __name__ == "__main__":
    GalaxyApp().run()