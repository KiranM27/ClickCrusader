from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.button import Button
from kivy.core.window import Window
import time
import random

sm = ScreenManager()


class w1(Screen):

    def quit_app(self):
        App.get_running_app().stop()
        Window.close()
        
    def __init__(self, **kwargs):
        super(w1, self).__init__(**kwargs)
        l1 = FloatLayout()
        self.add_widget(l1)
        
        b1 = Button(text = "Start", font_size = 20, size_hint = (0.3, 0.2), 
                    pos_hint = {"x": 0.35, "top": 0.9}, background_color = [0,1,0,0.5],
                    color = [0.929, 0.961, 0.882, 1], bold = True, 
                    on_press = self.change_to_gs
                    )
        b2 = Button(text = "Instructions", font_size = 20, size_hint = (0.3, 0.2), 
                    pos_hint = {"x": 0.35, "top": 0.6}, background_color = [0,0,1,0.7]
                    , color = [0.929, 0.961, 0.882, 1], bold = True,
                    on_press = self.change_to_ins)
        b3 = Button(text = "Quit", font_size = 20, size_hint = (0.3, 0.2), 
                    pos_hint = {"x": 0.35, "top": 0.3}, background_color = [255,0,0,0.7],
                    on_press = w1.quit_app, color = [0.929, 0.961, 0.882, 1], bold = True)
        l1.add_widget(b1)
        l1.add_widget(b2)
        l1.add_widget(b3)
    
    def change_to_gs(self, value):
        self.manager.current = "ds"
        
    def change_to_ins(self, value):
        self.manager.current = "ins"
#        
sm.add_widget(w1(name = "ui"))      
            

class w2(Screen):
    # Trackpad Screen
    
    def __init__(self, **kwargs):
        super(w2, self).__init__(**kwargs)
        self.l2 = FloatLayout()
        self.add_widget(self.l2)
        self.count = 0
        
        
        self.Lab1 = Label(text = "Score", font_size = 20, 
                          size_hint = (0.15,0.1), pos_hint = {"right": 1, "top": 1}, 
                          color = [0,0,0,1])
        self.l2.add_widget(self.Lab1)
        
        self.Lab2 = Label(text = str(self.count), font_size = 40,
                          size_hint = (0.15, 0.1), pos_hint = {"right": 1, "top": 0.925},
                          color = [0,0,0,1])
        self.l2.add_widget(self.Lab2)
        
        val1 = random.random() * 0.9
        val2 = random.random() * 0.9        
        self.b1 = Button(size_hint = (0.08,0.08), pos_hint = {"x": val1, "top": 1 - val2},
                    background_color = [0,0,0,0.9])
        self.b1.on_press = self.change1
        self.l2.add_widget(self.b1)
        
        val1 = random.random() * 0.9
        val2 = random.random() * 0.9        
        self.b2 = Button(size_hint = (0.08,0.08), pos_hint = {"x": val1, "top": 1 - val2},
                    background_color = [0,0,0,0.9])
        self.b2.on_press = self.change2
        self.l2.add_widget(self.b2)
        
        val1 = random.random() * 0.9
        val2 = random.random() * 0.9        
        self.b3 = Button(size_hint = (0.08,0.08), pos_hint = {"x": val1, "top": 1 - val2},
                    background_color = [0,0,0,0.9])
        self.b3.on_press = self.change3
        self.l2.add_widget(self.b3)
        
        val1 = random.random() * 0.9
        val2 = random.random() * 0.9        
        self.b4 = Button(size_hint = (0.08,0.08), pos_hint = {"x": val1, "top": 1 - val2},
                    background_color = [0,0,0,0.9])
        self.b4.on_press = self.change4
        self.l2.add_widget(self.b4)
        
        val1 = random.random() * 0.9
        val2 = random.random() * 0.9        
        self.b5 = Button(size_hint = (0.08,0.08), pos_hint = {"x": val1, "top": 1 - val2},
                    background_color = [0,0,0,0.9])
        self.b5.on_press = self.change5
        self.l2.add_widget(self.b5)
        
        self.comments= [("Bruh, What",'Winners never Quit, Not that you would know'),
                        ("Noob",'A new born could do better'),
                        ("Internediate",'Not bad for a beginner you know'),
                        ("Adept",'Oh, Looks like we have a natural over here'),
                        ("Hot Shot", "You should try out for professional esports"),
                        ('Legendary', "You must be flash in disguise")]
        
    def pop(self):
        if self.fscore < 5:
            t = self.comments[0][0]
            content = self.comments[0][1]
        elif self.fscore <= 25:
             t = self.comments[1][0]
             content = self.comments[1][1]
        elif self.fscore <= 40:
             t = self.comments[2][0]
             content = self.comments[2][1]
        elif self.fscore <= 50:
             t = self.comments[3][0]
             content = self.comments[3][1]
        elif self.fscore <= 70:
             t = self.comments[4][0]
             content = self.comments[4][1]
        else:
             t = self.comments[5][0]
             content = self.comments[5][1]
            
        popup = Popup(title = str(t), size_hint = (None, None),
                      size = (400, 200), auto_dismiss = True, content = Label(text = content))
        popup.open()
        
        
    def change1(self, *args):
        
        self.count = self.count + 1
        
        self.l2.remove_widget(self.Lab2)
        self.Lab2 = Label(text = str(self.count), font_size = 40,
                          size_hint = (0.15, 0.1), pos_hint = {"right": 1, "top": 0.925},
                          color = [0,0,0,1])
        self.l2.add_widget(self.Lab2)
        
        if self.count == 1:
            self.a = time.time()
        
        if (time.time() - self.a) > (10 ^ 17):
            self.fscore = self.count
            self.manager.current = "ui"
            self.count = 0
            self.pop()
        
        self.l2.remove_widget(self.b1)
        val1 = random.random() * 0.9
        val2 = random.random() * 0.9
        self.b1 = Button(size_hint = (0.08,0.08), pos_hint = {"x": val1, "top": 1 - val2},
                    background_color = [0,0,0,0.9])
        self.b1.on_press = self.change1
        self.l2.add_widget(self.b1)
        
    def change2(self, *args):
        
        self.count = self.count + 1
        self.l2.remove_widget(self.Lab2)
        self.Lab2 = Label(text = str(self.count), font_size = 40,
                          size_hint = (0.15, 0.1), pos_hint = {"right": 1, "top": 0.925},
                          color = [0,0,0,1])
        self.l2.add_widget(self.Lab2)
        
        if self.count == 1:
            self.a = time.time()
        
        if (time.time() - self.a) > (10 ^ 17):
            self.fscore = self.count
            self.manager.current = "ui"
            self.count = 0
            self.pop()
        
        self.l2.remove_widget(self.b2)
        val1 = random.random() * 0.9
        val2 = random.random() * 0.9
        self.b2 = Button(size_hint = (0.08,0.08), pos_hint = {"x": val1, "top": 1 - val2},
                    background_color = [0,0,0,0.9])
        self.b2.on_press = self.change2
        self.l2.add_widget(self.b2)
    
    def change3(self, *args):
        
        self.count = self.count + 1
        self.l2.remove_widget(self.Lab2)
        self.Lab2 = Label(text = str(self.count), font_size = 40,
                          size_hint = (0.15, 0.1), pos_hint = {"right": 1, "top": 0.925},
                          color = [0,0,0,1])
        self.l2.add_widget(self.Lab2)
        
        if self.count == 1:
            self.a = time.time()
        
        if (time.time() - self.a) > (10 ^ 17):
            self.fscore = self.count
            self.manager.current = "ui"
            self.count = 0
            self.pop()
        
        self.l2.remove_widget(self.b3)
        val1 = random.random() * 0.9
        val2 = random.random() * 0.9
        self.b3 = Button(size_hint = (0.08,0.08), pos_hint = {"x": val1, "top": 1 - val2},
                    background_color = [0,0,0,0.9])
        self.b3.on_press = self.change3
        self.l2.add_widget(self.b3)
        
    def change4(self, *args):
        
        self.count = self.count + 1
        self.l2.remove_widget(self.Lab2)
        self.Lab2 = Label(text = str(self.count), font_size = 40,
                          size_hint = (0.15, 0.1), pos_hint = {"right": 1, "top": 0.925},
                          color = [0,0,0,1])
        self.l2.add_widget(self.Lab2)
        
        if self.count == 1:
            self.a = time.time()
        
        if (time.time() - self.a) > (10 ^ 17):
            self.fscore = self.count
            self.manager.current = "ui"
            self.count = 0
            self.pop()
        
        self.l2.remove_widget(self.b4)
        val1 = random.random() * 0.9
        val2 = random.random() * 0.9
        self.b4 = Button(size_hint = (0.08,0.08), pos_hint = {"x": val1, "top": 1 - val2},
                    background_color = [0,0,0,0.9])
        self.b4.on_press = self.change4
        self.l2.add_widget(self.b4)
        
    def change5(self, *args):
        
        self.count = self.count + 1
        self.l2.remove_widget(self.Lab2)
        self.Lab2 = Label(text = str(self.count), font_size = 40,
                          size_hint = (0.15, 0.1), pos_hint = {"right": 1, "top": 0.925},
                          color = [0,0,0,1])
        self.l2.add_widget(self.Lab2)
        
        if self.count == 1:
            self.a = time.time()
        
        if (time.time() - self.a) > (10 ^ 17):
            self.fscore = self.count
            self.manager.current = "ui"
            self.count = 0
            self.pop()

        self.l2.remove_widget(self.b5)
        val1 = random.random() * 0.9
        val2 = random.random() * 0.9
        self.b5 = Button(size_hint = (0.08,0.08), pos_hint = {"x": val1, "top": 1 - val2},
                    background_color = [0,0,0,0.9])
        self.b5.on_press = self.change5
        self.l2.add_widget(self.b5)
        
sm.add_widget(w2(name = "gs_tpad"))

class w5(Screen):
    # Mouse Screen
    
    def __init__(self, **kwargs):
#        with self.canvas:
#            pass
        super(w5, self).__init__(**kwargs)
        self.l2 = FloatLayout()
        self.add_widget(self.l2)
        self.count = 0
        
        
        self.Lab1 = Label(text = "Score", font_size = 20, 
                          size_hint = (0.15,0.1), pos_hint = {"right": 1, "top": 1}, 
                          color = [0,0,0,1])
        self.l2.add_widget(self.Lab1)
        
        self.Lab2 = Label(text = str(self.count), font_size = 40,
                          size_hint = (0.15, 0.1), pos_hint = {"right": 1, "top": 0.925},
                          color = [0,0,0,1])
        self.l2.add_widget(self.Lab2)
        
        val1 = random.random() * 0.9
        val2 = random.random() * 0.9        
        self.b1 = Button(size_hint = (0.08,0.08), pos_hint = {"x": val1, "top": 1 - val2},
                    background_color = [0,0,0,0.9])
        self.b1.on_press = self.change1
        self.l2.add_widget(self.b1)
        
        val1 = random.random() * 0.9
        val2 = random.random() * 0.9        
        self.b2 = Button(size_hint = (0.08,0.08), pos_hint = {"x": val1, "top": 1 - val2},
                    background_color = [0,0,0,0.9])
        self.b2.on_press = self.change2
        self.l2.add_widget(self.b2)
        
        val1 = random.random() * 0.9
        val2 = random.random() * 0.9        
        self.b3 = Button(size_hint = (0.08,0.08), pos_hint = {"x": val1, "top": 1 - val2},
                    background_color = [0,0,0,0.9])
        self.b3.on_press = self.change3
        self.l2.add_widget(self.b3)
        
        val1 = random.random() * 0.9
        val2 = random.random() * 0.9        
        self.b4 = Button(size_hint = (0.08,0.08), pos_hint = {"x": val1, "top": 1 - val2},
                    background_color = [0,0,0,0.9])
        self.b4.on_press = self.change4
        self.l2.add_widget(self.b4)
        
        self.comments= [("Bruh, What",'Winners never Quit, Not that you would know'),
                        ("Noob",'A new born could do better'),
                        ("Internediate",'Not bad for a beginner you know'),
                        ("Adept",'Oh, Looks like we have a natural over here'),
                        ("Hot Shot", "You should try out for professional esports"),
                        ('Legendary', "You must be flash in disguise")]
        
    def pop(self):
        if self.fscore < 5:
            t = self.comments[0][0]
            content = self.comments[0][1]
        elif self.fscore <= 25:
             t = self.comments[1][0]
             content = self.comments[1][1]
        elif self.fscore <= 40:
             t = self.comments[2][0]
             content = self.comments[2][1]
        elif self.fscore <= 50:
             t = self.comments[3][0]
             content = self.comments[3][1]
        elif self.fscore <= 70:
             t = self.comments[4][0]
             content = self.comments[4][1]
        else:
             t = self.comments[5][0]
             content = self.comments[5][1]
            
        popup = Popup(title = str(t), size_hint = (None, None),
                      size = (400, 200), auto_dismiss = True, content = Label(text = content))
        popup.open()
        
        
    def change1(self, *args):
        
        self.count = self.count + 1
        
        self.l2.remove_widget(self.Lab2)
        self.Lab2 = Label(text = str(self.count), font_size = 40,
                          size_hint = (0.15, 0.1), pos_hint = {"right": 1, "top": 0.925},
                          color = [0,0,0,1])
        self.l2.add_widget(self.Lab2)
        
        if self.count == 1:
            self.a = time.time()
        
        if (time.time() - self.a) > (10 ^ 17):
            self.fscore = self.count
            self.manager.current = "ui"
            self.count = 0
            self.pop()
        
        self.l2.remove_widget(self.b1)
        val1 = random.random() * 0.9
        val2 = random.random() * 0.9
        self.b1 = Button(size_hint = (0.08,0.08), pos_hint = {"x": val1, "top": 1 - val2},
                    background_color = [0,0,0,0.9])
        self.b1.on_press = self.change1
        self.l2.add_widget(self.b1)
        
    def change2(self, *args):
        
        self.count = self.count + 1
        self.l2.remove_widget(self.Lab2)
        self.Lab2 = Label(text = str(self.count), font_size = 40,
                          size_hint = (0.15, 0.1), pos_hint = {"right": 1, "top": 0.925},
                          color = [0,0,0,1])
        self.l2.add_widget(self.Lab2)
        
        if self.count == 1:
            self.a = time.time()
        
        if (time.time() - self.a) > (10 ^ 17):
            self.fscore = self.count
            self.manager.current = "ui"
            self.count = 0
            self.pop()
        
        self.l2.remove_widget(self.b2)
        val1 = random.random() * 0.9
        val2 = random.random() * 0.9
        self.b2 = Button(size_hint = (0.08,0.08), pos_hint = {"x": val1, "top": 1 - val2},
                    background_color = [0,0,0,0.9])
        self.b2.on_press = self.change2
        self.l2.add_widget(self.b2)
    
    def change3(self, *args):
        
        self.count = self.count + 1
        self.l2.remove_widget(self.Lab2)
        self.Lab2 = Label(text = str(self.count), font_size = 40,
                          size_hint = (0.15, 0.1), pos_hint = {"right": 1, "top": 0.925},
                          color = [0,0,0,1])
        self.l2.add_widget(self.Lab2)
        
        if self.count == 1:
            self.a = time.time()
        
        if (time.time() - self.a) > (10 ^ 17):
            self.fscore = self.count
            self.manager.current = "ui"
            self.count = 0
            self.pop()
        
        self.l2.remove_widget(self.b3)
        val1 = random.random() * 0.9
        val2 = random.random() * 0.9
        self.b3 = Button(size_hint = (0.08,0.08), pos_hint = {"x": val1, "top": 1 - val2},
                    background_color = [0,0,0,0.9])
        self.b3.on_press = self.change3
        self.l2.add_widget(self.b3)
        
    def change4(self, *args):
        
        self.count = self.count + 1
        self.l2.remove_widget(self.Lab2)
        self.Lab2 = Label(text = str(self.count), font_size = 40,
                          size_hint = (0.15, 0.1), pos_hint = {"right": 1, "top": 0.925},
                          color = [0,0,0,1])
        self.l2.add_widget(self.Lab2)
        
        if self.count == 1:
            self.a = time.time()
        
        if (time.time() - self.a) > (10 ^ 17):
            self.fscore = self.count
            self.manager.current = "ui"
            self.count = 0
            self.pop()
        
        self.l2.remove_widget(self.b4)
        val1 = random.random() * 0.9
        val2 = random.random() * 0.9
        self.b4 = Button(size_hint = (0.08,0.08), pos_hint = {"x": val1, "top": 1 - val2},
                    background_color = [0,0,0,0.9])
        self.b4.on_press = self.change4
        self.l2.add_widget(self.b4)
        
        
sm.add_widget(w5(name = "gs_mouse"))

class w6(Screen):
    # Touch Screen
    
    def __init__(self, **kwargs):
#        with self.canvas:
#            pass
        super(w6, self).__init__(**kwargs)
        self.l2 = FloatLayout()
        self.add_widget(self.l2)
        self.count = 0
        
        
        self.Lab1 = Label(text = "Score", font_size = 20, 
                          size_hint = (0.15,0.1), pos_hint = {"right": 1, "top": 1}, 
                          color = [0,0,0,1])
        self.l2.add_widget(self.Lab1)
        
        self.Lab2 = Label(text = str(self.count), font_size = 40,
                          size_hint = (0.15, 0.1), pos_hint = {"right": 1, "top": 0.925},
                          color = [0,0,0,1])
        self.l2.add_widget(self.Lab2)
        
        val1 = random.random() * 0.9
        val2 = random.random() * 0.9        
        self.b1 = Button(size_hint = (0.08,0.08), pos_hint = {"x": val1, "top": 1 - val2},
                    background_color = [0,0,0,0.9])
        self.b1.on_press = self.change1
        self.l2.add_widget(self.b1)
        
        val1 = random.random() * 0.9
        val2 = random.random() * 0.9        
        self.b2 = Button(size_hint = (0.08,0.08), pos_hint = {"x": val1, "top": 1 - val2},
                    background_color = [0,0,0,0.9])
        self.b2.on_press = self.change2
        self.l2.add_widget(self.b2)
        
        val1 = random.random() * 0.9
        val2 = random.random() * 0.9        
        self.b3 = Button(size_hint = (0.08,0.08), pos_hint = {"x": val1, "top": 1 - val2},
                    background_color = [0,0,0,0.9])
        self.b3.on_press = self.change3
        self.l2.add_widget(self.b3)
        
        
        self.comments= [("Bruh, What",'Winners never Quit, Not that you would know'),
                        ("Noob",'A new born could do better'),
                        ("Internediate",'Not bad for a beginner you know'),
                        ("Adept",'Oh, Looks like we have a natural over here'),
                        ("Hot Shot", "You should try out for professional esports"),
                        ('Legendary', "You must be flash in disguise")]
        
    def pop(self):
        if self.fscore < 5:
            t = self.comments[0][0]
            content = self.comments[0][1]
        elif self.fscore <= 25:
             t = self.comments[1][0]
             content = self.comments[1][1]
        elif self.fscore <= 40:
             t = self.comments[2][0]
             content = self.comments[2][1]
        elif self.fscore <= 50:
             t = self.comments[3][0]
             content = self.comments[3][1]
        elif self.fscore <= 70:
             t = self.comments[4][0]
             content = self.comments[4][1]
        else:
             t = self.comments[5][0]
             content = self.comments[5][1]
            
        popup = Popup(title = str(t), size_hint = (None, None),
                      size = (400, 200), auto_dismiss = True, content = Label(text = content))
        popup.open()
        
        
    def change1(self, *args):
        
        self.count = self.count + 1
        
        self.l2.remove_widget(self.Lab2)
        self.Lab2 = Label(text = str(self.count), font_size = 40,
                          size_hint = (0.15, 0.1), pos_hint = {"right": 1, "top": 0.925},
                          color = [0,0,0,1])
        self.l2.add_widget(self.Lab2)
        
        if self.count == 1:
            self.a = time.time()
        
        if (time.time() - self.a) > (10 ^ 17):
            self.fscore = self.count
            self.manager.current = "ui"
            self.count = 0
            self.pop()
        
        self.l2.remove_widget(self.b1)
        val1 = random.random() * 0.9
        val2 = random.random() * 0.9
        self.b1 = Button(size_hint = (0.08,0.08), pos_hint = {"x": val1, "top": 1 - val2},
                    background_color = [0,0,0,0.9])
        self.b1.on_press = self.change1
        self.l2.add_widget(self.b1)
        
    def change2(self, *args):
        
        self.count = self.count + 1
        self.l2.remove_widget(self.Lab2)
        self.Lab2 = Label(text = str(self.count), font_size = 40,
                          size_hint = (0.15, 0.1), pos_hint = {"right": 1, "top": 0.925},
                          color = [0,0,0,1])
        self.l2.add_widget(self.Lab2)
        
        if self.count == 1:
            self.a = time.time()
        
        if (time.time() - self.a) > (10 ^ 17):
            self.fscore = self.count
            self.manager.current = "ui"
            self.count = 0
            self.pop()
        
        self.l2.remove_widget(self.b2)
        val1 = random.random() * 0.9
        val2 = random.random() * 0.9
        self.b2 = Button(size_hint = (0.08,0.08), pos_hint = {"x": val1, "top": 1 - val2},
                    background_color = [0,0,0,0.9])
        self.b2.on_press = self.change2
        self.l2.add_widget(self.b2)
    
    def change3(self, *args):
        
        self.count = self.count + 1
        self.l2.remove_widget(self.Lab2)
        self.Lab2 = Label(text = str(self.count), font_size = 40,
                          size_hint = (0.15, 0.1), pos_hint = {"right": 1, "top": 0.925},
                          color = [0,0,0,1])
        self.l2.add_widget(self.Lab2)
        
        if self.count == 1:
            self.a = time.time()
        
        if (time.time() - self.a) > (10 ^ 17):
            self.fscore = self.count
            self.manager.current = "ui"
            self.count = 0
            self.pop()
        
        self.l2.remove_widget(self.b3)
        val1 = random.random() * 0.9
        val2 = random.random() * 0.9
        self.b3 = Button(size_hint = (0.08,0.08), pos_hint = {"x": val1, "top": 1 - val2},
                    background_color = [0,0,0,0.9])
        self.b3.on_press = self.change3
        self.l2.add_widget(self.b3)
        
        
sm.add_widget(w6(name = "gs_touch"))

#Play mode Screen
class w3(Screen):
    
    def __init__(self, **kwargs):
        super(w3, self).__init__(**kwargs)
        l1 = FloatLayout()
        self.add_widget(l1)
        
        b1 = Button(text = "Trackpad", font_size = 20, size_hint = (0.3, 0.2), 
                    pos_hint = {"x": 0.35, "top": 0.9}, background_color = [0,1,0,0.5],
                    color = [0.929, 0.961, 0.882, 1], bold = True, 
                    on_press = self.change_to_game_tpad
                    )
        b2 = Button(text = "External Mouse", font_size = 20, size_hint = (0.3, 0.2), 
                    pos_hint = {"x": 0.35, "top": 0.6}, background_color = [0,0,1,0.7]
                    , color = [0.929, 0.961, 0.882, 1], bold = True,
                    on_press = self.change_to_game_mouse)
        b3 = Button(text = "Touch", font_size = 20, size_hint = (0.3, 0.2), 
                    pos_hint = {"x": 0.35, "top": 0.3}, background_color = [255,0,0,0.7],
                    color = [0.929, 0.961, 0.882, 1], bold = True,
                    on_press = self.change_to_game_touch)
        l1.add_widget(b1)
        l1.add_widget(b2)
        l1.add_widget(b3)
    
    def change_to_game_tpad(self, value):
        self.manager.current = "gs_tpad"  
    
    def change_to_game_mouse(self, value):
        self.manager.current = "gs_mouse" 
        
    def change_to_game_touch(self, value):
        self.manager.current = "gs_touch" 

sm.add_widget(w3(name = "ds"))


#Instructions Screen

class w4(Screen):
    
    def __init__(self, **kwargs):
        super(w4, self).__init__(**kwargs)
        self.l = FloatLayout()
        
        self.add_widget(self.l)
        Lab1 = Label(text = "Instructions", font_size = 30, size_hint = (0.1,0.1),
                     pos_hint = {"top": 0.95, "right" : 0.55}, color =[0, 0, 0, 1])
        self.l.add_widget(Lab1)
        
        Lab2 = Label(text = """
                                                        Click Crusader

| Choose one of three modes |
| Goal: Click on Black Boxes, worth a point each |
| Time Limit: 30 s |
| You can look at your current score at the top right corner of the screen |
| Higher the score, the cooler the final message |

""", font_size = 22.5, size_hint = (0.1,0.3),
                     pos_hint = {"top": 0.8, "right" : 0.55}, color =[0, 0, 128, 0.7])
        self.l.add_widget(Lab2)
        
        b1 = Button(text = "Start", font_size = 20, size_hint = (0.15, 0.1), 
                    pos_hint = {"x": 0.6, "top": 0.4}, background_color = [0,1,0,0.8],
                    color = [0.929, 0.961, 0.882, 1], bold = True, 
                    on_press = self.change_to_ds
                    )
        b2 = Button(text = "Back", font_size = 20, size_hint = (0.15, 0.1), 
                    pos_hint = {"x": 0.3, "top": 0.4}, background_color = [255,0,0,0.7]
                    , color = [0.929, 0.961, 0.882, 1], bold = True,
                    on_press = self.change_to_ui
                    )
        self.l.add_widget(b1)
        self.l.add_widget(b2)
        
    def change_to_ds(self, value):
        self.manager.current = "ds"
        
    def change_to_ui(self, value):
        self.manager.current = "ui"
    
sm.add_widget(w4(name = "ins"))



class ClickCrusader(App):
    def build(self):
#        Window.clearcolor = (0.02,0.22,0.42,0.1)
        Window.clearcolor = (1,1,1,1)
        return(sm)

if __name__ == "__main__":
    ClickCrusader().run()
    

        
             
        
