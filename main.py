from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.graphics import Color, Rectangle


# ====== FONCTION LECTURE FICHIERS TXT ======
def lire_fichier(nom):
    try:
        with open(nom, "r", encoding="utf-8") as f:
            return f.read()
    except:
        return "Contenu indisponible"


# ====== FONCTION WHATSAPP VIP (ANDROID) ======
def ouvrir_vip(instance):
    try:
        from jnius import autoclass
        Intent = autoclass('android.content.Intent')
        Uri = autoclass('android.net.Uri')
        PythonActivity = autoclass('org.kivy.android.PythonActivity')

        numero = "261345704202"
        message = "Bonjour, je veux activer le VIP Réaliste"
        url = f"https://wa.me/{numero}?text={Uri.encode(message)}"

        intent = Intent(Intent.ACTION_VIEW)
        intent.setData(Uri.parse(url))
        currentActivity = PythonActivity.mActivity
        currentActivity.startActivity(intent)

    except Exception as e:
        print("Erreur WhatsApp :", e)


# ====== CLASSE PRINCIPALE ======
class MatchDuJour(App):

    def build(self):
        root = BoxLayout(orientation="vertical", padding=10, spacing=10)

        # FOND VERT
        with root.canvas.before:
            Color(0, 0.6, 0, 1)
            self.rect = Rectangle(size=root.size, pos=root.pos)
        root.bind(size=self._update_rect, pos=self._update_rect)

        # TITRE
        titre = Label(
            text="🔥 MATCHS GRATUITS DU JOUR 🔥",
            size_hint=(1, None),
            height=60,
            bold=True
        )
        root.add_widget(titre)

        # ZONE TEXTE
        self.texte = Label(
            text=lire_fichier("coupon.txt"),
            size_hint_y=None,
            valign="top"
        )
        self.texte.bind(texture_size=self._update_text_height)

        scroll = ScrollView()
        scroll.add_widget(self.texte)
        root.add_widget(scroll)

        # BOUTONS
        root.add_widget(self.bouton("📌 Coupon du jour", "coupon.txt"))
        root.add_widget(self.bouton("🎉 Fun (20+)", "fun.txt"))
        root.add_widget(self.bouton("🛡 Safe", "safe.txt"))
        root.add_widget(self.bouton("⚽ Simple", "simple.txt"))

        # BOUTON VIP VERROUILLÉ
        vip = Button(
            text="🔒 VIP Réaliste",
            size_hint=(1, None),
            height=80,
            background_color=(0.4, 0.3, 0, 1)
        )
        vip.bind(on_press=ouvrir_vip)
        root.add_widget(vip)

        return root

    # ====== BOUTON STANDARD ======
    def bouton(self, texte, fichier):
        btn = Button(
            text=texte,
            size_hint=(1, None),
            height=70,
            background_color=(0.3, 0.3, 0.3, 1)
        )
        btn.bind(on_press=lambda x: self.afficher(fichier))
        return btn

    # ====== AFFICHER CONTENU ======
    def afficher(self, fichier):
        self.texte.text = lire_fichier(fichier)

    # ====== AJUSTEMENTS ======
    def _update_rect(self, instance, value):
        self.rect.size = instance.size
        self.rect.pos = instance.pos

    def _update_text_height(self, instance, value):
        instance.height = instance.texture_size[1]
        instance.text_size = (instance.width, None)


# ====== LANCEMENT ======
if __name__ == "__main__":
    MatchDuJour().run()
