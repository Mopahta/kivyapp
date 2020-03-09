from random import random
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.graphics import Color, Ellipse, Line


class MyPaintWidget(Widget):
	def on_touch_down(self, touch):
		color = (random(), random(), random())
		with self.canvas:
			Color(*color)
			d = 20
			Ellipse(pos=(touch.x - d/2, touch.y - d/2), size=(d, d))
			touch.ud['line'] = Line(points=(touch.x, touch.y))

	def on_touch_move(self, touch):
		touch.ud['line'].points += [touch.x, touch.y]

	def on_touch_up(self, touch):
		with self.canvas:

			d = 20
			Ellipse(pos=(touch.x - d / 2, touch.y - d / 2), size=(d, d))


class MyPaintApp(App):
	def build(self):
		self.title = 'Testing trying'
		self.icon = 'app.png'
		parent = Widget()
		self.painter = MyPaintWidget()
		clearbtn = Button(text='Clear', size_hint=(.1, .1), pos=(0,0))
		clearbtn.bind(on_release=self.clear_canvas)
		parent.add_widget(self.painter)
		brushbtn = Button(text='Brush', size_hint=(1, .1), pos=(0, 60))
		brushbtn.bind(on_release=self.clear_canvas)
		layout = FloatLayout(size=(60, 120))
		layout.add_widget(clearbtn)
		layout.add_widget(brushbtn)
		return layout

	def clear_canvas(self, obj):
		self.painter.canvas.clear()


if __name__ == '__main__':
	MyPaintApp().run()
