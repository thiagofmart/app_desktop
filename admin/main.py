from login import *

class Sessao(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        App.get_running_app().login = Login()
        self.add_widget(App.get_running_app().login)
        return

class Solar(MDApp):
    usuario = StringProperty('None')
    dash = ObjectProperty()
    login= ObjectProperty()
    tables = DictProperty(tables)
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Builder.load_file('login.kv')
        Builder.load_file('dashboard.kv')
        Builder.load_file('searchbar.kv')
        Builder.load_file('resultbar.kv')
        Builder.load_file('sidebar.kv')
    def build(self):
        self.theme_cls.primary_palette = 'Orange'
        self.theme_cls.accent_palette = 'Yellow'
    def set_user(self, user, topbar):
        self.usuario = user
        topbar.title = f'[b][color=#ffffff]Solar ADM - {self.usuario}[/color][/b]'
    def on_stop(self):
        if self.usuario != 'None':
            ins = atividades_de_usuarios.insert()
            ins.execute({'Usuario':app.usuario, 'Status': 'Saída'})
if __name__ == "__main__":
    Solar().run()
