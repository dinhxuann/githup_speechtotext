import threading

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.screenmanager import Screen
from kivy.uix.popup import Popup
class Popup_screen(FloatLayout):
    pass
class HomeScreen(Screen):
    pass
class SettingScreen(Screen):
    def create_press_on(self):
        self.ids.my_image1.source = 'icon/button_create_press.PNG'

    def create_press_off(self):
        self.ids.my_image1.source = 'icon/button_create.png'
    def open_press_on(self):
        self.ids.my_image.source = 'icon/button_open_press.PNG'
    def open_press_off(self):
        self.ids.my_image.source = 'icon/button_open.png'
        show_popup()

GUI=Builder.load_file("main.kv")

class MainApp(App):
    def build(self):
        return GUI
    def change_screen(self,screen_name):
        screen_manager = self.root.ids['screen_manager']
        screen_manager.current = screen_name
        if screen_name == 'home_screen':
            screen_manager.transition.direction = "left"
        else:
            screen_manager.transition.direction = "right"
def show_popup():
        show = Popup_screen()
        popupWindow =Popup(title="Choose your file",content=show,size_hint=(None,None),size=(800,400))
        popupWindow.open()
if __name__ == '__main__':
    MainApp().run()

