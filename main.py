from kivy.lang import Builder

from kivymd.app import MDApp
from kivymd.uix.label import MDLabel

import config
import requests
import json


class ManateeApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "BlueGray"
        self.theme_cls.accent_palette = "LightBlue"
        self.theme_cls.material_style = "M3"

        return Builder.load_file("manatee.kv")

    def jokes(self):
        """Access Manatee Jokes API and display joke"""
        self.root.ids.man_jokes.text = ""
        url = config.api_url
        headers = {"X-RapidAPI-Key": config.api_key, "X-RapidAPI-Host": config.api_host}
        response = requests.request("GET", url, headers=headers)
        jokes = response.json()
        setup = jokes["setup"]
        joke = jokes["punchline"]
        self.root.ids.man_jokes.add_widget(
            MDLabel(text=f"Setup: {setup}\nJoke: {joke}")
        )


if __name__ == "__main__":
    ManateeApp().run()
