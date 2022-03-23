from imports import *


class SearchField(MDBoxLayout):
    def __init__(self, txt, **kwargs):
        super().__init__(**kwargs)
        self.add_widget(MDLabel(text=txt.replace('_', ' ')))
        self.btn = BTN(txt='Contém', btn=MyButton)
        menu_items = [
        {
                "text": i,
                "viewclass": "OneLineListItem",
                "on_release": lambda text=i: self.menu_callback(text),
            } for i in ['Contém', 'Inicia com', 'Termina com', '<>']
        ]
        self.menu = MDDropdownMenu(
                caller=self.btn.btn,
                items=menu_items,
                width_mult=2.5,
                max_height='190dp',
        )
        self.btn.btn.bind(on_release=self.open_menu)
        self.add_widget(self.btn)
        self.add_widget(MDTextFieldRect(multiline=False))
    def menu_callback(self, text_item):
        self.btn.btn.text = text_item
        self.menu.dismiss()
    def open_menu(self, obj):
        self.menu.open()

class SearchBar(MDGridLayout):
    def __init__(self, table, **kwargs):
        super().__init__(**kwargs)
        c=0
        for column in table.__table__.columns:
            c+=1
            self.add_widget(SearchField(txt=column.key))
        while c%3 !=0:
            self.add_widget(MDBoxLayout(size_hint=(0.5, None), height='30dp'))
            c+=1
        self.height = f'{25+(30*(c/3))}dp'

class MiddleBar(MDBoxLayout):
    togvalue = StringProperty('10')

class Middle1(MDStackLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        for type_btn in 'Buscar Novo Limpar'.split():
            self.add_widget(BTN(txt=type_btn, btn=MyButton))
class Middle2(MDStackLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        for type_btn in '30 20 10'.split():
            self.add_widget(BTN(txt=type_btn, btn=TgBtn))

class BTN(MDBoxLayout):
    def __init__(self, txt, btn, **kwargs):
        super().__init__(**kwargs)
        if btn == TgBtn:
            if txt == '10':
                self.btn = btn(text=txt, group='search', state='down')
            else:
                self.btn = btn(text=txt, group='search', state='normal')
        elif btn == MyButton:
            self.btn = btn(text=txt)
        self.add_widget(self.btn)
class MyButton(MDRectangleFlatButton):
    def action(self):
        resultbar = self.parent.parent.parent.parent.parent.parent.resultbar
        middlebar = self.parent.parent.parent
        if self.text == 'Buscar':
            resultbar.buscar(quantity=int(middlebar.togvalue))
        elif self.text == 'Limpar':
            resultbar.limpar()
class TgBtn(MDRectangleFlatButton, MDToggleButton):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Clock.schedule_once(self.set_self_color)
    def action(self):
        Clock.schedule_once(self.set_self_color)
    def set_self_color(self, time):
        if self.state == 'down':
            self.parent.md_bg_color = (1, 1, 1, 0.5)
            middlebar = self.parent.parent.parent
            middlebar.togvalue = self.text
        elif self.state == 'normal':
            self.parent.md_bg_color = (0.9, 0.9, 0.9, 1)
        self.text_color = (0,0,0,1)
