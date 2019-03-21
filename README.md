

#Overview

Qute is a wrapped extension of Marcus Ottosson's Qt.py. The emphasis is on
utilising the convience of Qt.py (allowing for use of PyQt, PySide and 
PySide2 seamlessly) whilst also exposing a set of common pieces of functionality
we tend to replicate and utilise in many places.


#Key Features

## General Usage

```python
import qute


class MyWidget(qute.QWidget):

    def __init__(self, parent=None):
        super(MyWidget, self).__init__(parent=parent)
        
        # -- Create a layout and set it as the base layout. Use 
        # -- qute to slim the layout - removing margins
        self.setLayout(
            qute.slimify(qute.QVBoxLayout())
        )
        
        # -- Create some widgets
        self.spinner = qute.QSpinBox()
        self.checker = qute.QCheckBox()
        
        # -- Add these to our layout
        self.layout().addWidget(self.spinner)
        self.layout().addWidget(self.checkbox)
        
        # -- Finally lets connect some signals and slots without
        # -- caring what it is
        qute.connectBlind(self.spinner, self.do_something)
        qute.connectBlind(self.checker, self.do_something)
        
    def do_something(self, *args, **kwargs):
        print('doing something...')

if __name__ == '__main__':

    # -- Use qute to get or create the QApplication instance
    q_app = qute.qApp()
    
    widget = MyWidget()
    widget.show()
    
    q_app.exec_()
```
In this example we see some of the features of qute in use, but most importantly is that it is usable in environments using either PyQt, PySide or PySide2 (thanks to Qt.py), and then utilises the various helper functionality defined within qute which you can read about below.


##Styling

Qute gives a convience function for applying stylesheets to Qt widgets. Crucually it also exposes a mechanism allowing you do define variables to be replaced within stylesheets. This helps when wanting to use the same values multiple times across a stylesheet.

For example, if we have a stylesheet such as:

```css
QWidget {
    background-color: rgb(BG_COLOR);
    color: rgb(TEXT_COLOR);
}

QLabel {
    padding-top: 7px;
    padding-bottom: 7px;
    background-color: transparent;
    color: rgb(TEXT_COLOR);
}
```

This can be assigned to a widget using:

```python
import qute

qute.applyStyle(
    css_str,
    apply_to=widget,
    BG_COLOR='50, 50, 50',
    TEXT_COLOR='255, 0, 0',
)
```
In this example we pass a CSS string and the widget we want to apply to. Any additional keywords will be used as search and replace elements. This is handy when wanting to change sections of your stylesheet easily. Your replacements can be numbers, strings or filepaths (just ensure your slashing is / and not \\). The ```space``` example stylesheet demonstrates this by using png files for widget backgrounds.

Equally, you can pass the full path to a css/qss file too:

```python
qute.applyStyle(
    '/usr/styles/my_style.qss',
    widget,
)
```

Alternatively you can have a library of style sheets and set the environment variable `QUTE_STYLE_PATH` to that location. By doing this you can pass the name of the style rather than the absolute path. Qute comes with one example stylesheet called `space` which can be used to demonstrate this as below:
```python
qute.applyStyle(
    'space',
    widget,
)   
```

This is an example of the space stylesheet:

![alt text](https://github.com/mikemalinowski/qute/blob/master/docs/space_demo.png?raw=true)



##Menu Generation

Generating menu's can be tedious and involve a lot of repetative code. In many cases a menu is made up of either actions, sseperators or sub-menus. 

Each of these are supported by the menu generation function ```qute.menuFromDictionary```. The format of the dictionary you provide must conform to:

`{'Label': function}` or `{'Label': dict}` or `{'Label': None}`

If a function is given then the function is set as the callable when the item is clicked. If a dictionary is given as the value a submenu is generated (this is recusive, so you can nest menus). If the value is None then a Seperator will be added regardless of the key.

Here is an example:

```python
import qute

def foo():
    print('calling foo')

def bar():
    print('calling bar')

menu_definition = {
    'Foo': foo,
    '-': None,
    'More': dict(bar=bar)
}

menu = qute.menuFromDictionary(menu_definition)
```

In this example we define some functions and add them as keys, we can then generate a QMenu from that dictionary. This is especially useful when you're dynamically generating menu from variable data.

You can also define icons for your menu. To utilise this mechanism your icons must have the same name as the label and end in .png. You can then define the path to the icons during the menu call as shown here:

```python
menu = qute.menuFromDictionary(
    structure=menu_definition,
    icon_paths=[
        os.path.dirname(__file__),
    ]
)
```


##Derive

Derive is all about dynamically generating ui elements based on data types and being able to extract values from widgets without having to know what they are. This is particularly useful when generating ui elements on the fly without knowing what they are up front.

A good example of this is the exposure of options or attributes on a class without knowing exactly what those options are. We can see an example of that here:

```python
import qute

class Node:
    """
    Define a base class for something
    """
    
    def __init__(self):
        self.options=dict()

class Circle(Node):

    def __init__(self):
        self.options['radius'] = 5
        self.options['closed'] = True
   
class Quadtrilateral(Node):

    def __init__(self):
        self.options['force_rectangle']

def example_callback(*args, **kwargs):
    print('In Callback')
    
nodes = [
    Circle(),
    Quadtrilateral(),
    Quadtrilateral(),
    Circle(),
]

for node in nodes:
    for option, value in node.options:
    
        # -- Blindly create a widget to represent the widget
        widget = qute.deriveWidget(
        value=value,
        label=option,
        )
        
        # -- Connect the change event of the widget
        # -- to our callback - without knowing what 
        # -- the widget is or what to connect
        qute.connectBlind(widget, example_callback)
```

We can also ask for the value from a widget without knowing what the widget is. This can be done using:

```python
import qute

value = qute.deriveValue(widget)
```

This mechanism makes it easier to create dynamic ui's, especially when you're trying to expose data which can be manipulated on code objects.



## Compatability

This has been tested under Python 2.7.13 and Python 3.6.6 under both Windows and Ubuntu.


## Contribute

If you would like to contribute thoughts, ideas, fixes or features please get in touch! mike@twisted.space

