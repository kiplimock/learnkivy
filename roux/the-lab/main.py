from kivy.app import App
from kivy.metrics import dp
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.stacklayout import StackLayout
from kivy.properties import StringProperty, ObjectProperty, BooleanProperty
from kivy.graphics import Line, Ellipse, Rectangle, Color
from kivy.metrics import dp
from kivy.properties import Clock


class WidgetsExample(GridLayout):
    my_text = StringProperty("1")
    count_enabled = BooleanProperty(False)
    slider_label_text = StringProperty("50")
    text_input = StringProperty("foo")
    count = 1
    def on_button_click(self):
        if self.count_enabled:
            self.count += 1
    
        self.my_text = str(self.count)

    def on_toggle_button_state(self, widget):
        if widget.state == "normal":
            widget.text = "OFF"
            self.count_enabled = False
        else:
            widget.text = "ON"
            self.count_enabled = True
    
    def on_switch_active(self, widget):
        print(f"Switch: {str(widget.active)}")
    
    def on_slider_value(self, widget):
        self.slider_label_text = str(int(widget.value))

    def on_text_validate(self, widget):
        self.text_input = widget.text


class StackLayoutExample(StackLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = "lr-tb"
        for i in range(100):
            size = dp(100)
            b = Button(text=str(i+1), size_hint=(None, None), size=(size, size))
            self.add_widget(b)

# class GridLayoutExample(GridLayout):
#     pass

class AnchorLayoutExample(AnchorLayout):
    pass

class BoxLayoutExample(BoxLayout):
    pass
    # def __init__(self, **kwargs):
    #     super().__init__(**kwargs)
    #     b1 = Button(text="A")
    #     b2 = Button(text="B")
    #     b3 = Button(text="C")
    #     self.add_widget(b1)
    #     self.add_widget(b2)
    #     self.add_widget(b3)



class MainWidget(Widget):
    pass

class TheLabApp(App):
    pass

class CanvasExample1(Widget):
    pass

class CanvasExample2(Widget):
    pass

class CanvasExample3(Widget):
    pass

class CanvasExample4(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        with self.canvas:
            Line(points=(10,10,100,100,110,90,200,200,300,320), width=2)
            Color(0,1,0)
            Line(circle=(400,200,100), width=2)
            Line(rectangle=(400,400,150,100), width=3)
            self.rect = Rectangle(pos=(10,200), size=(100,100))
    
    def on_button_a_click(self):
        x, y = self.rect.pos
        w, h = self.rect.size
        inc = dp(10)
        diff = self.width - (x + w)

        if diff < inc:
            inc = diff
        x += inc
        # y += dp(10)
        self.rect.pos = (x, y)

class CanvasExample5(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.s = dp(50)
        self.vx = dp(3)
        self.vy = dp(4)
        with self.canvas:
            self.ball = Ellipse(pos=(100,100), size=(self.s, self.s))
        Clock.schedule_interval(self.update, 1)

    def on_size(self, *args):
        # print("On size: " + str(self.width) + ", " + str(self.height))
        self.ball.pos = (self.center_x-self.s/2, self.center_y-self.s/2)
    
    def update(self, dt):
        x, y = self.ball.pos
        x += self.vx
        y += self.vy
        
        if (x + self.s) > self.width or x < 0:
            self.vx = -self.vx
        if (y + self.s) > self.height or y < 0:
            self.vy = -self.vy
        
        self.ball.pos = (x, y)

class CanvasExample6(Widget):
    pass
 
if __name__ == "__main__":
    TheLabApp().run()