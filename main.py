from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition
from kivy.clock import Clock
from kivy.core.audio import SoundLoader
from kivy.graphics import Color, Ellipse
from kivy.animation import Animation
from kivy.uix.widget import Widget
from kivymd.app import MDApp
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton
import random
import wave
import struct
import os
import math
from kivymd.uix.dialog.md_dialog import MDDialog
from kivymd.uix.button.md_button import MDFlatButton
from kivy.core.window import Window
from kivy.config import Config

Config.set('graphics', 'multisamples', '0')
Config.set('kivy', 'keyboard_mode', 'system')

Window.softinput_mode = "below_target"

# Exemple de questions - remplace par tes 30 questions
questions_original = {
    "niveau_1": [
        {"question": "Comment appellet-t-on l'éléphant en langue mbo Sanzo?", "options": ["Nzock", "Keup", "Mbié"], "answer": "Nzock"},
        {"question": "Comment appelle-t-on le liquide extrait du datier?", "options": ["Anak", "Ndeup", "Miim"], "answer": "Anak"},
        {"question": "Comment appelle-t-on le liquide extrait du palmier a huile?", "options": ["Elédé", "Nzon", "Bié"], "answer": "Elédé"},
        {"question": "Comment appelle-t-on le tam-tam en langue mbo Sanzo?", "options": ["Eleum", "ngon", "kankang"], "answer": "Eleum"},
        {"question": "Combien de village faut-il traversé pour arriver a Ngwatta?", "options": ["2", "3", "4"], "answer": "2"},
        {"question": "Le Nkam prend sa source dans quel village?", "options": ["Mbokambo", "Mboukok", "Michimia"], "answer": "Mbokambo"},
        {"question": "Quelle fleuve se jete dans le Nkam ?", "options":["Nkam", "Anoue", "Magam"], "answer": "Magam"},
        {"question": "Quelle fleuve travers la rive gauche et la rive droit?", "options": ["Nkam", "Anoue", "Magam"], "answer": "Nkam"},
        {"question": "Commment appelle-t-on la lune en langue Mbo Sanzo?", "options": ["Ngon", "Ekak", "Ebuk"], "answer": "Ngon"},
        {"question": "Comment dit-on bonne année en langue Mbo Sanzo?", "options": ["Ebonguet esseup", "Mbu", "Ban"], "answer": "Ebonguet esseup"},
    ],
    "niveau_2": [
        {"question": "Quelle est la capital du groupe Mbo Sanzo?", "options": ["Balé", "Ngwatta", "Nteingue"], "answer": "Ngwatta"},
        {"question": "Qui est le pere fondateur du groupement Mbo Sanzo?", "options": ["Milat pius", "Sanzo mikwelle", "Esselem camille"], "answer": "Sanzo mikwelle"},
        {"question": "Qui est Mila assoute?", "options": ["Chef du village", "Un planteur", "Chef superieur"], "answer": "Chef superieur"},
        {"question": "Quelle village est sur le site de Nkong?", "options": ["Bebong", "Nfonbap", "Ntawan"], "answer": "Nfonbap"},
        {"question": "Comment s'appelle le maire de la commune de Sanzo / Santchou ?","options": ["Ngoubene francois", "Milat hervé", "Ewane Donald"], "answer": "Ngoubene Francois"},
        {"question": "Qui est le fondateur du parti politique RDMC ?","options": ["Pr Mila assoute", "Mbah arnquld", "Presi"], "answer": "Pr Mila assoute"},
        {"question": "Nfon signifie quoi en langue Mbo?","options": ["Chef", "Vendeur", "Commercant"], "answer": "Chef"},
        {"question": "Comment appelle t-on la chefferie du groupement Sanzo ?", "options": ["King palace", "Palais", "Case"], "answer": "King palace"},
        {"question": "Quelle est la seule ville du groupement Sanzo ?", "options": ["Sanzo/Santchou", "Mokot", "Mboukok"], "answer": "Sanzo/Santchou"},
        {"question": "Comment dit-on Bonjour en langue Mbo Sanzo?", "options": ["Emagrem", "Yan", "Ewan"], "answer": "Emagrem"},
    ],
    "niveau_3": [
        {"question": "A Ngwatta, qui s'est sacrifier pour liberer le village contre les voleurs de recoltes ?","options": ["Esselem mekom", "Milat pius", "Milat polycarpe"], "answer": "Esselem mekom"},
        {"question": "Dans la mitologie Mbo qu'elle grotte parlait autre fois ?", "options": ["Ala ngoue", "Ala mbou", "Ala mott"], "answer": "Ala ngoue"},
        {"question": "Le groupement Mbo Sanzo est limitrophe au sud par quel canton?", "options": ["Canton Mbo", "Nkam", "Magam"], "answer": "Canton Mbo"},
        {"question": "Le groupement Mbo Sanzo est limitrophe au nord par quel Groupement ?", "options": ["Nfondenera", "Canton Mbo", "Anoue"], "answer": "Nfondera"},
        {"question": "Le groupement Mbo Sanzo est limitrophe a l'est par quel Groupement ?", "options": ["Nfondenera", "Canton Mbo", "Mbeta"], "answer": "Mbeta"},
        {"question": "Le groupement Mbo Sanzo est limitrophe a L'ouest par quel Groupement ?", "options": ["Nfondenera", "kekem", "Anoue"], "answer": "Kekem"},
        {"question": "Qui est Emabot brigette?", "options": ["Depute", "commercante", "Avocat"], "answer": "Deputé"},
        {"question": "Tout premier Mbo Sanzo a ministre sous etait Amadou ahidjo s'appellait comment?", "options": ["Efon vincent", "Ewane dieudonné", "Milat "], "answer": "Efon vincent"},
        {"question": "Dr Nkam maurice était le DG de quelle etablissement hospitalier ?","options": ["CHU", "CHRACER", "Laquintini"], "answer": "CHU"},
        {"question": "Que signifie Sanzo en langue Mbo Sanzo?", "options": ["Le pere des éléphants", "La mere des éléphants", "La fille des éléphant"], "answer": "Le pere des éléphants"},
    ]

}

KV = '''
ScreenManager:
    MainScreen:
    QuizScreen:
    TransitionScreen:
    WinScreen:

<MainScreen>:
    name: 'main'
    BoxLayout:
        orientation: 'vertical'
        MDTopAppBar:
            title: 'Sanzo Quiz Sans Faute'
            elevation: 2
        MDLabel:
            text: '30s par question. 1 erreur = Match terminé'
            halign: 'center'
            font_style: 'H6'
        MDIconButton:
            icon: 'play'
            icon_size: '64sp'
            pos_hint: {"center_x":.5}
            on_release: app.play_click(); app.start_quiz()
        MDLabel:
            text: 'Developper par LWCode'
            halign: 'center'
            
            font_style: 'H6'
            pos_hint: {'center_x': 0.5,'center_y': 0.1}
        Widget:

<QuizScreen>:
    name: 'quiz'
    BoxLayout:
        orientation: 'vertical'
        MDTopAppBar:
            id: toolbar
            title: 'Niveau 1'
            left_action_items: [["arrow-left", lambda x: app.confirm_quit()]]
            elevation: 2
        MDBoxLayout:
            adaptive_height: True
            padding: 10
            MDLabel:
                id: score_label
                text: 'Score: 0/10'
                halign: 'left'
            MDLabel:
                id: timer_label
                text: 'Temps: 30s'
                halign: 'right'
                theme_text_color: "Custom"
                text_color: 0, 0.6, 0, 1
        MDLabel:
            id: question_label
            text: ''
            halign: 'center'
            font_style: 'H6'
            padding: 20
        MDBoxLayout:
            id: options_box
            orientation: 'vertical'
            spacing: 10
            padding: 20
            adaptive_height: True
        Widget:

<TransitionScreen>:
    name: 'transition'
    BoxLayout:
        orientation: 'vertical'
        MDLabel:
            id: transition_label
            text: ''
            halign: 'center'
            font_style: 'H4'
        MDRaisedButton:
            text: "CONTINUER"
            pos_hint: {"center_x":.5}
            on_release: app.play_click(); app.continue_next_level()

<WinScreen>:
    name: 'win'
    FloatLayout:
        id: confetti_layer
        MDLabel:
            text: 'VICTOIRE!\\nScore parfait: 30/30'
            halign: 'center'
            font_style: 'H3'
            pos_hint: {"center_y":.6}
        MDRaisedButton:
            text: "REJOUER"
            pos_hint: {"center_x":.3, "center_y":.3}
            on_release: app.play_click(); app.start_quiz()
        MDRaisedButton:
            text: "MENU"
            pos_hint: {"center_x":.7, "center_y":.3}
            on_release: app.play_click(); app.go_home()
'''

class MainScreen(Screen):
    pass

class QuizScreen(Screen):
    def display_question(self):
        app = MDApp.get_running_app()
        niveau = f"niveau_{app.current_level}"

        if app.current_question >= len(app.questions[niveau]):
            app.level_complete()
            return

        question = app.questions[niveau][app.current_question]
        self.ids.question_label.text = f"Question {app.current_question + 1}: {question['question']}"
        self.ids.score_label.text = f'Score: {app.score}/10'
        self.ids.toolbar.title = f'Niveau {app.current_level}'

        self.ids.options_box.clear_widgets()
        options_shuffled = question["options"][:]
        random.shuffle(options_shuffled)
        for option in options_shuffled:
            btn = MDRaisedButton(
                text=option,
                size_hint_x=1,
                pos_hint={"center_x":0.5,"center_y":0.5},
                on_release=lambda x, opt=option: (app.play_click(), app.check_answer(opt))
            )
            self.ids.options_box.add_widget(btn)

        app.start_timer()

class TransitionScreen(Screen):
    pass

class Confetti(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.size_hint = (None, None)
        self.size = (random.randint(8, 15), random.randint(8, 15))
        self.velocity_y = random.uniform(-400, -200)
        self.bounces = 0
        self.max_bounces = random.randint(2, 4)

    def update(self, dt):
        self.velocity_y += 800 * dt
        self.y -= self.velocity_y * dt

        if self.y <= 0 and self.bounces < self.max_bounces:
            self.y = 0
            self.velocity_y = -self.velocity_y * 0.6
            self.bounces += 1
        elif self.y <= -50:
            if self.parent:
                self.parent.remove_widget(self)

class WinScreen(Screen):
    def on_enter(self):
        self.ids.confetti_layer.clear_widgets()
        self.confetti_event = Clock.schedule_interval(self.create_confetti, 0.1)
        Clock.schedule_once(lambda dt: Clock.unschedule(self.confetti_event), 3)

    def on_leave(self):
        if hasattr(self, 'confetti_event'):
            Clock.unschedule(self.confetti_event)

    def create_confetti(self, dt):
        confetti = Confetti()
        confetti.x = random.randint(0, self.width)
        confetti.y = self.height + random.randint(0, 100)
        with confetti.canvas:
            Color(random.random(), random.random(), random.random(), 1)
            Ellipse(size=confetti.size, pos=confetti.pos)

        self.ids.confetti_layer.add_widget(confetti)
        Clock.schedule_interval(lambda dt: self.update_confetti(confetti, dt), 1/60)

    def update_confetti(self, confetti, dt):
        if confetti.parent:
            confetti.update(dt)
            confetti.canvas.clear()
            with confetti.canvas:
                Color(random.random(), random.random(), random.random(), 1)
                Ellipse(size=confetti.size, pos=(confetti.x, confetti.y))
        else:
            return False

class QuizApp(MDApp):
    current_level = 1
    current_question = 0
    score = 0
    time_left = 30
    timer_event = None
    questions = {}
    dialog = None

    def build(self):
        self.theme_cls.primary_palette = "Blue"
        self.theme_cls.theme_style = "Light"
        self.create_sounds()
        sm = Builder.load_string(KV)
        sm.transition = SlideTransition(direction='left')
        return sm

    def generate_wav(self, filename, freq, duration, end_freq=None, melody=None, volume=0.3):
        if os.path.exists(filename):
            return
        sample_rate = 44100
        if melody:
            audio = b''
            for f in melody:
                for i in range(int(sample_rate * 0.2)):
                    value = int(volume * 32767 * math.sin(2 * math.pi * f * i / sample_rate))
                    audio += struct.pack('<h', value)
        else:
            audio = b''
            total_samples = int(sample_rate * duration)
            for i in range(total_samples):
                if end_freq:
                    current_freq = freq + (end_freq - freq) * i / total_samples
                else:
                    current_freq = freq
                envelope = math.exp(-i / sample_rate * 5) if duration < 0.1 else 1
                value = int(volume * 32767 * envelope * math.sin(2 * math.pi * current_freq * i / sample_rate))
                audio += struct.pack('<h', value)

        with wave.open(filename, 'w') as f:
            f.setnchannels(1)
            f.setsampwidth(2)
            f.setframerate(sample_rate)
            f.writeframes(audio)

    def create_sounds(self):
        # Génère les fichiers.wav une seule fois
        self.generate_wav('click.wav', 800, 0.05, volume=0.2)
        self.generate_wav('tick.wav', 440, 0.1, volume=0.3)
        self.generate_wav('correct.wav', 600, 0.15, end_freq=900, volume=0.4)
        self.generate_wav('error.wav', 200, 0.4, end_freq=100, volume=0.5)
        self.generate_wav('win.wav', 261, 0.8, melody=[261, 329, 392, 523], volume=0.5)

        self.sound_click = SoundLoader.load('click.wav')
        self.sound_tick = SoundLoader.load('tick.wav')
        self.sound_correct = SoundLoader.load('correct.wav')
        self.sound_error = SoundLoader.load('error.wav')
        self.sound_win = SoundLoader.load('win.wav')

    def play_click(self):
        if self.sound_click:
            self.sound_click.play()

    def start_quiz(self):
        self.close_dialog()
        self.current_level = 1
        self.current_question = 0
        self.score = 0
        self.shuffle_questions()
        self.root.current = 'quiz'
        self.root.get_screen('quiz').display_question()

    def shuffle_questions(self):
        self.questions = {}
        for niveau, q_list in questions_original.items():
            self.questions[niveau] = q_list[:]
            random.shuffle(self.questions[niveau])

    def start_timer(self):
        self.cancel_timer()
        self.time_left = 30
        self.update_timer_label()
        self.timer_event = Clock.schedule_interval(self.countdown, 1)

    def countdown(self, dt):
        self.time_left -= 1
        self.update_timer_label()
        if self.time_left > 0 and self.sound_tick:
            self.sound_tick.play()
        if self.time_left <= 0:
            self.cancel_timer()
            if self.sound_error:
                self.sound_error.play()
            self.game_over("Temps écoulé!")

    def update_timer_label(self):
        if self.root.current == 'quiz':
            timer_label = self.root.get_screen('quiz').ids.timer_label
            timer_label.text = f'Temps: {self.time_left}s'
            if self.time_left <= 10:
                timer_label.text_color = [1, 0, 0, 1]
            else:
                timer_label.text_color = [0, 0.6, 0, 1]

    def cancel_timer(self):
        if self.timer_event:
            self.timer_event.cancel()
            self.timer_event = None

    def check_answer(self, selected_option):
        self.cancel_timer()
        niveau = f"niveau_{self.current_level}"
        correct_answer = self.questions[niveau][self.current_question]["answer"]

        if selected_option == correct_answer:
            if self.sound_correct:
                self.sound_correct.play()
            self.score += 1
            Clock.schedule_once(lambda dt: self.next_question(), 0.3)
        else:
            if self.sound_error:
                self.sound_error.play()
            self.game_over(f"Mauvaise réponse! La bonne réponse: {correct_answer}")

    def next_question(self):
        self.current_question += 1
        self.root.get_screen('quiz').display_question()

    def level_complete(self):
        self.cancel_timer()
        if self.current_level < 3:
            self.root.current = 'transition'
            trans_screen = self.root.get_screen('transition')
            trans_screen.ids.transition_label.text = f"Niveau {self.current_level} terminé!\nScore: {self.score}/10\n\nPrêt pour le niveau {self.current_level + 1}?"
        else:
            self.win_game()

    def continue_next_level(self):
        self.current_level += 1
        self.current_question = 0
        self.root.current = 'quiz'
        self.root.get_screen('quiz').display_question()

    def game_over(self, reason):
        self.cancel_timer()
        self.close_dialog()
        self.dialog = MDDialog(
            title="Game Over",
            text=f"{reason}\n\nTu as atteint le niveau {self.current_level}, question {self.current_question + 1}\nScore final: {self.score}",
            buttons=[
                MDFlatButton(text="REJOUER", on_release=lambda x: (self.play_click(), self.start_quiz())),
                MDFlatButton(text="MENU", on_release=lambda x: (self.play_click(), self.go_home())),
            ],
        )
        self.dialog.open()

    def win_game(self):
        if self.sound_win:
            self.sound_win.play()
        self.root.current = 'win'

    def confirm_quit(self):
        self.cancel_timer()
        self.close_dialog()
        self.dialog = MDDialog(
            title="Quitter?",
            text="Ta partie sera perdue. Continuer?",
            buttons=[
                MDFlatButton(text="NON", on_release=lambda x: (self.play_click(), self.close_dialog(), self.start_timer())),
                MDFlatButton(text="OUI", on_release=lambda x: (self.play_click(), self.go_home())),
            ],
        )
        self.dialog.open()

    def close_dialog(self):
        if self.dialog:
            self.dialog.dismiss()
            self.dialog = None

    def go_home(self):
        self.close_dialog()
        self.cancel_timer()
        self.root.current = 'main'

if __name__ == '__main__':
    QuizApp().run()