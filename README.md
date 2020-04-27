# Click Crusader

-----------------------------------
## Introduction

--------------------------------------
**Click Crusader** is a fun cross-platfrom game designed to imporve your mouse and trackpad mechnaics as well as improve your hand eye coordination. You can choose one of three game modes
-  Trackpad
- External Mouse
- Touch

The goal of the game, irrespective of the game mode, is simple enough. Click on as many boxes as possible within the time limit of 30 s. Each box is worth one point. Your current score can be seen at the top right corner of the screen and the higher your score at the end of the game, the cooler the comment that you will receive.  Have Fun !!

## Dependencies

---------------------------------------------
Apart from the built in python functions, the game only makes use of three other modules namely:
- Kivy ( install @ https://kivy.org/doc/stable/installation/installation-windows.html )
- Time ( built-in )
- Random ( built-in )

-------------------------------------------------
## Code Explanation

------------------------------------------------
### Kivy Imports

-------------------------------------------------
```python
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.button import Button
from kivy.core.window import Window
```

-------------------------------------------------------
### Classes, Functions and Widgets

---------------------------------------------------------
```python
sm = ScreenManager()
```
> This creates an instance of the Screen Manager and stores it in the variable *sm*

```python
sm.add_widget(w1(name = "ui"))   
```
> The above command adds the screen *w1* to the Screen Manager *sm* and names the screen as "*ui*".
This command can only be used once a class named *w1* and the Object type has to be that of a Screen, else it will return an error

```python
class w1(Screen):

    def quit_app(self):
        App.get_running_app().stop()
        Window.close()
        
    def __init__(self, **kwargs):
        super(w1, self).__init__(**kwargs)
        l1 = FloatLayout()
        self.add_widget(l1)
```
> The first statement creates a class called *w1* which is of the type *Screen*. 

> We then define a method called *quit_app()* which when called causes the game window to close. This function is bound to a button. 