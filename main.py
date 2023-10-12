from kivy.app import App
from kivy.uix.screenmanager import Screen



class PhotoGalleryApp(App):
    pass


class Display(Screen):
    images = ["download.jpg", "download2.jfif"]
    index = 0
    def display_image(self):
        return self.images[self.index]
        self.ids.image.source = self.images[self.index]

    def advance(self):
        self.index += 1
        print(self.index)
        if self.index > len(self.images):
            self.index = 0
        self.display_image()

    def go_back(self):
        self.index -= 1
        print(self.index)
        if self.index < 0:
            self.index = 1
        self.display_image()




PhotoGalleryApp().run()