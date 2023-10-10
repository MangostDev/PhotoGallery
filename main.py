from kivy.app import App
from kivy.uix.screenmanager import Screen


class PhotoGalleryApp(App):
    pass


class Display(Screen):
    def display_image(self):
        return images[index]

images = ["download.jpg"]
index = 0


PhotoGalleryApp().run()