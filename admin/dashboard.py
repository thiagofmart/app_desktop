from sidebar import *
from searchbar import *
from resultbar import *

class TopBar(MDToolbar):
    menustate = StringProperty('open')
    def logout(self, app):
        app.root.remove_widget(app.dash)
        app.root.add_widget(app.login)
        session.add(historico_de_acessos(Usuario=app.usuario, Status='Saída'))
        session.commit()
        app.set_user('', topbar=self)
    def min_or_max(self):
        # -> https://stackoverflow.com/questions/40356521/how-to-get-list-of-all-widgets-from-widget-tree-in-kivy-python-recursion-functi
        def save_state(widget, dimension):
            for child in widget.children:
                save_state(child, dimension)
                if 'MyTogBut' in str(child) or 'MDBoxLayout' in str(child):
                    child.size_hint = dimension

        if self.menustate == 'open':
            self.parent.ids.sdb.size_hint_x = 0
            self.parent.ids.line.pos_hint =  {'x':0, 'y':0}
            self.parent.ids.g.size_hint_x = 1
            self.parent.ids.g.pos_hint = {'x':0, 'y':0}
            save_state(self.parent.ids.sdb.children[0], dimension=(0, 0))
            self.menustate = 'close'

        elif self.menustate == 'close':
            self.parent.ids.sdb.size_hint_x = 0.15
            self.parent.ids.line.pos_hint =  {'x':0.15, 'y':0}
            self.parent.ids.g.size_hint_x = 0.85
            self.parent.ids.g.pos_hint = {'x':0.15, 'y':0}
            save_state(self.parent.ids.sdb.children[0], dimension=(1, None))
            self.parent.ids.line.size_hint = (None, 0.90)
            self.menustate = 'open'

class Tela(MDScreen):
    table = ObjectProperty()
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        scrl = ScrollView()
        grid = MDGridLayout(adaptive_height=True, cols=1)
        grid.add_widget(SearchBar(table=self.table))
        grid.add_widget(MiddleBar())
        self.resultbar = ResultBar(table=self.table)
        grid.add_widget(self.resultbar)
        scrl.add_widget(grid)
        self.add_widget(scrl)

class Gerenciador(ScreenManager):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.transition = NoTransition()
        for key, value in App.get_running_app().tables.items():
            print(list(value), '===================================================')
            for v in value:
                print(v,'=====================================================')
                self.add_widget(Tela(name=v.__tablename__, table=v))

class DashBoard(MDFloatLayout):
    pass
