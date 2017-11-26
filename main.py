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

##
from kivy.app import App
from kivy.properties import StringProperty
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition
import os

from connected import Connected

 


###
class LoginScreen(Screen):
    pass

class Connected(Screen):
    pass

class Disconnected(Screen):
    pass

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





class LoginApp(App):
    username = StringProperty(None)
    password = StringProperty(None)

    def build(self):
        manager = ScreenManager()

        manager.add_widget(Login(name='login'))
        manager.add_widget(Connected(name='connected'))

        return manager

    def get_application_config(self):
        if(not self.username):
            return super(LoginApp, self).get_application_config()

        conf_directory = self.user_data_dir + '/' + self.username

        if(not os.path.exists(conf_directory)):
            os.makedirs(conf_directory)

        return super(LoginApp, self).get_application_config(
            '%s/config.cfg' % (conf_directory))
#
class Login(Screen):
    def do_login(self, loginText, passwordText):
        app = App.get_running_app()

        app.username = loginText
        app.password = passwordText

        self.manager.transition = SlideTransition(direction="left")
        self.manager.current = 'connected'

        app.config.read(app.get_application_config())
        app.config.write()

    def resetForm(self):
        self.ids['login'].text = ""
        self.ids['password'].text = ""

#



class MyScreenManager(ScreenManager):
    username = StringProperty(None)
    password = StringProperty(None)

    manager = ScreenManager()
    manager.add_widget(Login(name='login'))
    manager.add_widget(Connected(name='connected'))
    manager.add_widget(Connected(name='disconnected')) 
    manager.add_widget(HomeScreen(name='home')) 
   

    def new_colour_screen(self):
        name = str(time.time())
        print (name)
        s = ColourScreen(name=name,
                         colour=[random.random() for _ in range(3)] + [1])
        self.add_widget(s)
        self.current = name
    
    def do_login(self, loginText, passwordText):
        app = App.get_running_app()

        app.username = loginText
        app.password = passwordText

        self.manager.transition = SlideTransition(direction="left")
        self.manager.current = 'home'

        app.config.read(app.get_application_config())
        app.config.write()

    def resetForm(self):
        self.ids['login'].text = ""
        self.ids['password'].text = ""


    
    

    def get_application_config(self):
        if(not self.username):
            return super(LoginApp, self).get_application_config()

        conf_directory = self.user_data_dir + '/' + self.username

        if(not os.path.exists(conf_directory)):
            os.makedirs(conf_directory)

        return super(LoginApp, self).get_application_config(
            '%s/config.cfg' % (conf_directory))

    def connecting(self):
        self.manager.transition = SlideTransition(direction="right")
        self.root.current = 'home'

    def disconnected(self):
        self.manager.transition = SlideTransition(direction="left")
        self.root.current = 'login'
        self.root.get_screen('login').resetForm()
<<<<<<< HEAD
    


    
#sm = ScreenManager()
#sm.switch_to(screen1)
# later
#sm.switch_to(screen2, direction='left')
# later
#sm.switch_to(screen3, direction='right', duration=1.)
=======
        


    

>>>>>>> d3f3c7facbc3ecb3cda18b9356bb9cc4fb59bfb3
    








class Connected(Screen):
    def disconnected(self):
        self.manager.transition = SlideTransition(direction="left")
        self.manager.current = 'login'
        self.manager.get_screen('login').resetForm()
    
    def connecting(self):
        self.manager.transition = SlideTransition (direction="right")
        self.manager.current = 'home'
        

##


root_widget = Builder.load_string('''
#:kivy 1.6

#:import FadeTransition kivy.uix.screenmanager.FadeTransition

MyScreenManager:
    transition: FadeTransition()
    ZeroScreen:
    HomeScreen:
    SecondScreen:
    FirstScreen:
    ThirdScreen:
    LoginScreen:
    Connected:
    
<<<<<<< HEAD
    
=======
>>>>>>> d3f3c7facbc3ecb3cda18b9356bb9cc4fb59bfb3


<Connected>:
    name :'connected'
    BoxLayout:
        orientation: 'vertical'

        Label:
            text: "You are now connected " 
            font_size: 32
        Button:
            text: "Get in to Home Page"
            font_size: 24
            on_release: app.root.current = 'home'
        Button:
            text: "Disconnect"
            font_size: 24
            on_release: app.root.current = 'login'
            


<LoginScreen>:
    name: 'login'	
    BoxLayout
	
        id: login_layout
        orientation: 'vertical'
        padding: [10,50,10,50]
        spacing: 50

        Label:
            text: 'Welcome to ABCReal'
            font_size: 32

        BoxLayout:
            orientation: 'vertical'

            Label:
                text: 'Username'
                font_size: 20
                halign: 'left'
                text_size: root.width-25, 25

            TextInput:
                id: login
                multiline:False
                font_size: 15

        BoxLayout:
            orientation: 'vertical'
            Label:
                text: 'Password'
                halign: 'left'
                font_size: 20
                text_size: root.width-20, 20

            TextInput:
                id: password
                multiline:False
                password:True
                font_size: 15

        Button:
            text: 'Login'
            font_size: 20
            on_release: app.root.current = 'connected'
	    


<HomeScreen>:
    name: 'home'
    BoxLayout:
        orientation: 'vertical'
<<<<<<< HEAD

        Label:
            text: 'Home Page'
            font_size: 30
		BoxLayout:
			Button:
				text: 'Exit'
				halign: 'right'
				font_size: 15
				on_release: exit()
=======
        Label:
            text: 'Home Page'
            font_size: 30
>>>>>>> d3f3c7facbc3ecb3cda18b9356bb9cc4fb59bfb3
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
                on_release: app.root.current = 'home'
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
                text: 'go to Login'
                font_size: 10
                on_release: app.root.current = 'login'
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

class TerapiAbaApp(App):
    def build(self):
        return root_widget




if __name__ == '__main__':
    TerapiAbaApp().run()
