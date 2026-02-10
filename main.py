from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
import webbrowser
import requests

# ---------- LIENS GITHUB (RAW) ----------
BASE_URL = "https://raw.githubusercontent.com/finaz12/Match-du-jour/main/"

def lire_fichier(nom):
    try:
        url = BASE_URL + nom
        r = requests.get(url, timeout=5)
        if r.status_code == 200:
            return r.text
        else:
            return "Aucun match disponible"
    except:
        return "Aucun match disponible"

# ---------- FONCTIONS BOUTONS ----------
def ouvrir_coupon(instance):
    app.label.text = lire_fichier("coupon.txt")

def ouvrir_fun(instance):
    app.label.text = lire_fichier("fun.txt")

def ouvrir_safe(instance):
    app.label.text = lire_fichier("safe.txt")

def ouvrir_simple(instance):
    app.label.text = lire_fichier("simple.txt")

def ouvrir_vip(instance):
    webbrowser.open(
        "https://wa.me/261345704202?text=Bonjour%2C%20je%20veux%20activer%20le%20VIP%20Réaliste"
    )

# ---------- APPLICATION ----------
class RealisteVIP(App):
    def build(self):
        global app
        app = self

        layout = BoxLayout(orientation="vertical", padding=10, spacing=10)

        titre = Label(
            text="RÉALISTE VIP ⚽",
            size_hint=(1, 0.15),
            font_size="24sp",
            bold=True
        )

        self.label = Label(
            text="MATCHS GRATUITS DU JOUR\n\nChoisis un bouton",
            size_hint=(1, 0.45),
            halign="center",
            valign="middle"
        )
        self.label.bind(size=self.label.setter("text_size"))

        btn_coupon = Button(text="🎟 Coupon du jour", on_press=ouvrir_coupon)
        btn_fun = Button(text="🔥 Fun (20+)", on_press=ouvrir_fun)
        btn_safe = Button(text="🛡 Safe", on_press=ouvrir_safe)
        btn_simple = Button(text="⚽ Simple", on_press=ouvrir_simple)

        btn_vip = Button(
            text="VIP 🔒",
            size_hint=(1, 0.15),
            background_color=(0, 0.8, 0, 1)
        )
        btn_vip.bind(on_press=ouvrir_vip)

        layout.add_widget(titre)
        layout.add_widget(self.label)
        layout.add_widget(btn_coupon)
        layout.add_widget(btn_fun)
        layout.add_widget(btn_safe)
        layout.add_widget(btn_simple)
        layout.add_widget(btn_vip)

        return layout

if __name__ == "__main__":
    RealisteVIP().run()
