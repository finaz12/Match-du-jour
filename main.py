from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.core.window import Window
import os

Window.clearcolor = (0, 0.6, 0, 1)  # fond vert

class MatchApp(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        self.label = Label(
            text="Choisis un bouton",
            size_hint=(1, 0.3),
            color=(1, 1, 1, 1),
            halign="center",
            valign="middle"
        )
        self.label.bind(size=self.label.setter("text_size"))

        self.layout.add_widget(self.label)

        self.add_btn("Coupon du jour", "coupon.txt")
        self.add_btn("Le Fun (20+)", "fun.txt")
        self.add_btn("Le Safe", "safe.txt")
        self.add_btn("Simple", "simple.txt")
        self.add_btn("VIP 🔒", "vip.txt")

        return self.layout

    def add_btn(self, text, file):
        btn = Button(
            text=text,
            size_hint=(1, 0.15),
            background_color=(0.3, 0.3, 0.3, 1),
            color=(1, 1, 1, 1)
        )
        btn.bind(on_press=lambda x: self.load_match(file))
        self.layout.add_widget(btn)

    def load_match(self, file):
        if os.path.exists(file):
            with open(file, "r", encoding="utf-8") as f:
                self.label.text = f.read()
        else:
            self.label.text = "Fichier introuvable"

if __name__ == "__main__":
    MatchApp().run()