from __future__ import absolute_import, division, print_function, unicode_literals
__metaclass__ = type

from kivy.app import App
from kivy.base import runTouchApp
from kivy.lang import Builder
from kivy.properties import ListProperty
from kivy.uix.boxlayout import BoxLayout

from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition


from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button






from kivy.animation import Animation



import time
import random

class HomeScreen(Screen):
    pass

class FirstScreen(Screen):
    pass

class SecondScreen(Screen):
    pass
class ThirdScreen(Screen):
    pass

class ZeroScreen(Screen):
    pass

class ColourScreen(Screen):
    colour = ListProperty([1., 2., 0., 1.])





class Root(FloatLayout):

    def load_content(self, content):
        for but in range(20):
            content.add_widget(Button(
                                text=str(but)))
class MyScreenManager(ScreenManager):
    def new_colour_screen(self):
        name = str(time.time())
        print (name)
        s = ColourScreen(name=name,
                         colour=[random.random() for _ in range(3)] + [1])
        self.add_widget(s)
        self.current = name




class RootWidget(Screen):
    def __init__(self, **kwargs):
        super(RootWidget, self).__init__(**kwargs)
        self.animate()

    def animate(self):
        anim = Animation(opacity=0, duration=3)
        #anim.start(self.name)


class TestApp(App):
    def build(self):
        return RootWidget()



root_widget = Builder.load_string('''
#:kivy 1.6

#:import FadeTransition kivy.uix.screenmanager.FadeTransition

MyScreenManager:
    transition: FadeTransition()
    HomeScreen:
    FirstScreen:
    SecondScreen:
    ThirdScreen:
    ZeroScreen:
    

        


    
<Root>:
    Button:
        center_x: root.center_x
        text: 'press to add_widgets'
        size_hint: .2, .2
        on_press:
            # what comes after `:` is basically normal python code
            sb.content.clear_widgets()
            # however using a callback that you can control in python
            # gives you more control
            root.load_content(sb.content)
    SideBar:
        id: sb
        size_hint: .2, 1
        image: 'data/images/image-loading.gif'


<HomeScreen>:
    name: 'Home'
    BoxLayout:
        orientation: 'vertical'
        Label:
            text: 'Home Page'
            font_size: 30
        Image:
            source: 'natureza.jpg'
            allow_stretch: True
            keep_ratio: False
        BoxLayout:
            Button:
                text: 'goto first screen'
                font_size: 30
                on_release: app.root.current = 'first'
            Button:
                text: 'get second screen'
                font_size: 30
                on_release: app.root.current = 'second'

<FirstScreen>:
    name: 'first'
    BoxLayout:
        orientation: 'vertical'
        Label:
            text: 'first screen!'
            font_size: 30
        Image:
            source: 'colours.png'
            allow_stretch: True
            keep_ratio: True 
        BoxLayout:
            Button:
                text: 'goto second screen'
                font_size: 30
                on_release: app.root.current = 'second'
            Button:
                text: 'get random colour screen'
                font_size: 20
                on_release: app.root.new_colour_screen()
<SecondScreen>:
    name: 'second'
    BoxLayout:
        orientation: 'vertical'
        Label:
            text: 'second screen!'
            font_size: 30
        Image:
            source: 'colours2.png'
            allow_stretch: True
            keep_ratio: True
        BoxLayout:
            Button:
                text: 'goto third screen'
                font_size: 30
                on_release: app.root.current = 'third'
                
            Button:
                text: 'get random colour screen'
                font_size: 20
                on_release: app.root.new_colour_screen()

<ThirdScreen>:
    name: 'third'
    BoxLayout:
        orientation: 'vertical'
        Label:
            text: 'Third screen!'
            font_size: 20
        Image:
            source: 'ferias.jpg'
            allow_stretch: True
            keep_ratio: True
        BoxLayout:
            Button:
                text: 'goto Home screen'
                font_size: 20
                on_release: app.root.current = 'Home'
            Button:
                text: 'get random colour screen'
                font_size: 15
                on_release: app.root.new_colour_screen()
<zeroScreen>:
    name: 'zero'
    
    Label
        id: label
        text: "Welcome"
        font_size: 20
    
        BoxLayout:
            orientation: 'vertical'
            Button:
                text: 'goto Home screen'
                font_size: 10
                on_release: app.root.current = 'Home'
            Button:
                text: 'get random colour screen'
                font_size: 10
                on_release: app.root.new_colour_screen()
            



<ColourScreen>:
    BoxLayout:
        orientation: 'vertical'
        Label:
            text: 'colour {:.2},{:.2},{:.2} screen'.format(*root.colour[:3])
            font_size: 30
        Widget:
            canvas:
                Color:
                    rgba: root.colour
                Ellipse:
                    pos: self.pos
                    size: self.size
        BoxLayout:
            Button:
                text: 'goto first screen'
                font_size: 30
                on_release: app.root.current = 'first'
            Button:
                text: 'get random colour screen'
                font_size: 30
                on_release: app.root.new_colour_screen()
            Button:
                text: 'goto zero screen'
                font_size: 30
                on_release: app.root.current = 'zero'




''')


"""<RootWidget>:


        """

class ScreenManagerApp(App):
    def build(self):
        return root_widget




            
ScreenManagerApp().run()
