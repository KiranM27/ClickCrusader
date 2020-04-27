# Click Crusader

## Introduction

**Click Crusader** is a fun cross-platfrom game designed to imporve your mouse and trackpad mechnaics as well as improve your hand eye coordination. You can choose one of three game modes
-  Trackpad
- External Mouse
- Touch

The goal of the game, irrespective of the game mode, is simple enough. Click on as many boxes as possible within the time limit of 30 s. Each box is worth one point. Your current score can be seen at the top right corner of the screen and the higher your score at the end of the game, the cooler the comment that you will receive.  Have Fun !!

## Dependencies

Apart from the built in python functions, the game only makes use of three other modules namely:
- Kivy ( install @ https://kivy.org/doc/stable/installation/installation-windows.html )
- Time ( built-in )
- Random ( built-in )

## Code Explanation

### Kivy Imports

```python
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.button import Button
from kivy.core.window import Window
```

### Classes, Functions and Widgets

```python
sm = ScreenManager()
```
> This creates an instance of the Screen Manager and stores it in the variable *sm*

```python
sm.add_widget(w1(name = "ui"))   
```
> The above command adds the screen *w1* to the Screen Manager *sm* and names the screen as "*ui*".

>This command can only be used once a class named *w1* and the Object type has to be that of a Screen, else it will return an error



```python
class w1(Screen):

    def quit_app(self):
        App.get_running_app().stop()
        Window.close()
        
    def change_to_gs(self, value):
        self.manager.current = "ds"
        
    def __init__(self, **kwargs):
        super(w1, self).__init__(**kwargs)
        l1 = FloatLayout()
        self.add_widget(l1)
```
> The first statement creates a class called *w1* which is of the type *Screen*. 

> We then define a method called *quit_app()* which when called causes the game window to close. This function is bound to a button. 

> The method *change_to_gs( )* is similar to the *quit_app()* method, but instead of closing the game window, it used the Screen Manager to display a screen whose name is "*ds*".

> In the __init__ ( ) method, takes in an argument called \*\*kwargs which allows us to pass in any number of arguments without explicitly typing out the same .

> The *super( )* method is used to call the methods of the superclass and to access the superclass constructor.

> We then create a Float Layout and store that in the variable *l1*. The float layout is then added to the the screen using the last line of the above code.



```python
b1 = Button(text = "Start", font_size = 20, size_hint = (0.3, 0.2), 
                    pos_hint = {"x": 0.35, "top": 0.9}, background_color = [0,1,0,0.5],
                    color = [0.929, 0.961, 0.882, 1], bold = True, 
                    on_press = self.change_to_gs
                    )
l1.add_widget(b1)
```

> A button *b1* is then created with the above mentioned paramenters and the button, upon press, calls the method *change_to_gs( )*. This button is then added to the Float Layout using the *add_widget* command.


```python
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
```
> Here we define a method called *pop ( )* which creates a popup thats pops up on the screen once the 30 s are over. *self.comments* is a pre-defined list of tuples of an adjevtive and a comment corresponf to the *self.fscore* which is the final score once the 30 s are done. 

The above is more or less an overview of the methods and classes used in this game



## Code Overview

The game is made up of 6 screens in total, namely the
- Start Screen
- Instructions Screen 
- Game Mode Screen
- Trackpad Game Screen
- External Mouse Game Screen
- Touch Game Screen

While the code for all the three game modes are very similar, they differ in the number of boxes that are on the screen at any given point in time. Since the touch game mode is easier than the others it has only 3 boxes, 4 boxes for the external mouse and as playing on a trackpad is the hardest, 5 boxes appear at a time for the trackpad game mode. 

The timer begins once the first box is pressed and 30 seconds later, a popup pops up on your screen and delivers a cool comment based on your score. Click anywhere on the screen will take you back to the start screen from where you can either play another game or leave the game if you feel like you have had enough.