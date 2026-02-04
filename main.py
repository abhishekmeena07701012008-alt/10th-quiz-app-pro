import random
import json
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.clock import Clock

class HomeScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)
        layout.add_widget(Label(text="10th Board Quiz Pro", font_size=32, size_hint_y=0.2))
        
        subjects = ["Science", "Math", "Social_Science", "Hindi", "English"]
        for sub in subjects:
            btn = Button(text=sub, size_hint_y=0.15, background_color=(0.2, 0.6, 1, 1))
            btn.bind(on_release=self.select_subject)
            layout.add_widget(btn)
        self.add_widget(layout)

    def select_subject(self, instance):
        self.manager.get_screen('quiz').current_subject = instance.text
        self.manager.current = 'quiz'

class QuizScreen(Screen):
    current_subject = ""
    
    def on_enter(self):
        with open('questions.json', 'r') as f:
            data = json.load(f)
        
        # सब्जेक्ट के अनुसार सवाल उठाना और 30 रैंडम चुनना
        all_ques = data[self.current_subject]
        self.questions = random.sample(all_ques, min(len(all_ques), 30))
        
        self.score = 0
        self.q_index = 0
        self.time_left = 3600 # 60 मिनट
        self.start_quiz()
        Clock.schedule_interval(self.update_timer, 1)

    def start_quiz(self):
        self.show_question()

    def show_question(self):
        self.clear_widgets()
        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)
        
        q_data = self.questions[self.q_index]
        
        # टाइमर और स्कोर लेबल
        layout.add_widget(Label(text=f"Time: {self.time_left//60:02}:{self.time_left%60:02} | Score: {self.score}", size_hint_y=0.1))
        
        # सवाल दिखाना
        layout.add_widget(Label(text=f"Q.{self.q_index+1}: {q_data['q']}", font_size=20, text_size=(500, None), size_hint_y=0.3))
        
        # ऑप्शन शफलिंग (उत्तरों का क्रम बदलना)
        options = q_data['options']
        random.shuffle(options)
        
        for opt in options:
            btn = Button(text=opt, size_hint_y=0.15)
            btn.bind(on_release=lambda x: self.check_answer(x.text, q_data['a']))
            layout.add_widget(btn)
            
        self.add_widget(layout)

    def check_answer(self, selected, correct):
        if selected == correct:
            self.score += 1
        
        self.q_index += 1
        if self.q_index < len(self.questions):
            self.show_question()
        else:
            self.end_quiz()

    def update_timer(self, dt):
        self.time_left -= 1
        if self.time_left <= 0:
            self.end_quiz()

    def end_quiz(self):
        Clock.unschedule(self.update_timer)
        self.clear_widgets()
        layout = BoxLayout(orientation='vertical', padding=20)
        layout.add_widget(Label(text="Test Finished!", font_size=30))
        layout.add_widget(Label(text=f"Final Score: {self.score}/30"))
        btn = Button(text="Go Home", size_hint_y=0.2)
        btn.bind(on_release=lambda x: setattr(self.manager, 'current', 'home'))
        layout.add_widget(btn)
        self.add_widget(layout)

class QuizApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(HomeScreen(name='home'))
        sm.add_widget(QuizScreen(name='quiz'))
        return sm

if __name__ == '__main__':
    QuizApp().run()
