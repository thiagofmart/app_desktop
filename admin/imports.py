from kivy.app import App
from kivy.uix.stacklayout import StackLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.actionbar import ActionBar
from kivy.uix.screenmanager import ScreenManager
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.screenmanager import NoTransition
from kivy.uix.spinner import Spinner
from kivy.uix.scrollview import ScrollView

from kivy.properties import StringProperty, ColorProperty, ObjectProperty, DictProperty, ListProperty
from kivy.lang import Builder
from kivy.clock import Clock
from kivy.utils import get_color_from_hex
from kivy.metrics import dp


from kivymd.app import MDApp
from kivymd.uix.label import MDLabel, MDIcon
from kivymd.uix.datatables import MDDataTable
from kivymd.uix.screen import MDScreen
from kivymd.uix.card import MDCard, MDSeparator
from kivymd.uix.toolbar import MDToolbar
from kivymd.uix.button import MDRaisedButton, MDFlatButton, MDRectangleFlatButton, MDIconButton, MDTextButton
from kivymd.uix.stacklayout import MDStackLayout
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.behaviors.toggle_behavior import MDToggleButton
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.expansionpanel import MDExpansionPanel, MDExpansionPanelOneLine
from kivymd.uix.gridlayout import MDGridLayout
from kivymd.uix.behaviors import HoverBehavior
from kivymd.uix.list import OneLineListItem
from kivymd.uix.textfield import MDTextField, MDTextFieldRect
from kivymd.uix.datatables import MDDataTable
from kivymd.theming import ThemableBehavior
from kivymd.uix.behaviors.backgroundcolor_behavior import BackgroundColorBehavior



from db import *
from time import sleep

from kivy.core.window import Window
from kivy.config import Config
#https://kivy.org/doc/stable/_modules/kivy/config.html
Config.set('input', 'mouse', 'mouse,multitouch_on_demand')
Config.set('graphics', 'window_state', 'maximized')
Config.set('graphics', 'minimum_width', 1000)
Config.set('graphics', 'minimum_height', 600)
Config.write()
colors = {
'Orange':{
    "50": "FFF3E0",
    "100": "FFE0B2",
    "200": "FFCC80",
    "300": "FFB74D",
    "400": "FFA726",
    "500": "FF9800",
    "600": "FB8C00",
    "700": "F57C00",
    "800": "EF6C00",
    "900": "E65100",
    "A100": "FFD180",
    "A200": "FFAB40",
    "A400": "FF9100",
    "A700": "FF6D00",
},
"Light": {
        "StatusBar": "E0E0E0",
        "AppBar": "F5F5F5",
        "Background": "FAFAFA",
        "CardsDialogs": "FFFFFF",
        "FlatButtonDown": "cccccc",
},
"Dark": {
        "StatusBar": "000000",
        "AppBar": "212121",
        "Background": "303030",
        "CardsDialogs": "424242",
        "FlatButtonDown": "999999",
},
}
