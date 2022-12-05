from kivy.lang import Builder

from kivymd.app import MDApp
from kivymd.uix.label import MDLabel

import config
import requests


class ManateeApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "BlueGray"
        self.theme_cls.accent_palette = "LightBlue"
        self.theme_cls.material_style = "M3"

        return Builder.load_file("manatee.kv")
