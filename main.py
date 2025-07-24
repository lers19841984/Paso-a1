from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy_garden.matplotlib.backend_kivyagg import FigureCanvasKivyAgg
from matplotlib.figure import Figure

class MyLayout(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        fig = Figure(figsize=(5, 3))
        ax = fig.add_subplot(111)
        ax.plot([1, 2, 3, 4], [10, 5, 3, 7])

        canvas = FigureCanvasKivyAgg(fig)
        self.add_widget(canvas)

class MyApp(App):
    def build(self):
        return MyLayout()

if __name__ == '__main__':
    MyApp().run()
