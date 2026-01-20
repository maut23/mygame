from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager,Screen
from kivy.animation import Animation

# 🧩 MENU SCREEN
class MenuScreen(Screen):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        layout=BoxLayout(orientation='vertical',spacing=15,padding=20)
        title=Label(text="Counter Game",font_size=40)
        play_btn=Button(text="Play",font_size=24)
        play_btn.bind(on_press=self.start_game)
        exit_btn=Button(text="Exit",font_size=20)
        exit_btn.bind(on_press=self.exit_app)
        layout.add_widget(title)
        layout.add_widget(play_btn)
        layout.add_widget(exit_btn)
        self.add_widget(layout)
    def start_game(self,instance):
        self.manager.current="game"
    def exit_app(self,instance):
        App.get_running_app().stop()

# 🎮 GAME SCREEN
class GameScreen(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        self.point=10
        self.max_point=20
        layout=BoxLayout(orientation='vertical',spacing=15,padding=20)
        self.point_label=Label(text="Point:10",font_size=24)
        play_btn=Button(text="Tap",font_size=24)
        play_btn.bind(on_press=self.increase_point)
        reset_btn=Button(text="Restart",font_size=20)
        reset_btn.bind(on_press=self.reset_game)
        layout.add_widget(self.point_label)
        layout.add_widget(play_btn)
        layout.add_widget(reset_btn)
        self.add_widget(layout)
    def increase_point(self,instance):
        # 🎬 animation
        anim=Animation(opacity=0.5,duration=0.05)+Animation(opacity=1,duration=0.05)
        anim.start(instance)
        if self.point<self.max_point:
            self.point+=1
            self.point_label.text=f"Point:{self.point}"
            if self.point==self.max_point:
                self.manager.current="win"
    def reset_game(self,instance):
        self.point=10
        self.point_label.text="Point:10"

# 🏆 WIN SCREEN

class WinScreen(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        layout=BoxLayout(orientation='vertical',spacing=20,padding=30)
        win_label=Label(text="You Win",font_size=30)
        restart_btn=Button(text="Restart",font_size=30)
        restart_btn.bind(on_press=self.restart_game)
        layout.add_widget(win_label)
        layout.add_widget(restart_btn)
        self.add_widget(layout)
    def restart_game(self,instance):
        game=self.manager.get_screen("game")
        game.point=10
        game.point_label.text="Point:10"
        self.manager.current="menu"

# 🧠 APP

class CounterGame(App):
    def build(self):
        sm=ScreenManager()
        sm.add_widget(MenuScreen(name="menu"))
        sm.add_widget(GameScreen(name="game"))
        sm.add_widget(WinScreen(name="win"))
        return sm

CounterGame().run()
