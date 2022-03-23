from dashboard import *

class InputLogin(MDTextField):
    def on_text_validate(self):
        app = App.get_running_app()
        LoginForm().login_validation(app, user_inputed=self.parent.parent.ids.Usuario.text,
                                          pass_inputed=self.parent.parent.ids.Senha.text)
        self.parent.parent.ids.Usuario.text = ''
        self.parent.parent.ids.Senha.text = ''

class LoginForm(MDBoxLayout):
    def login_validation(self, app, user_inputed=None, pass_inputed=None):
        # Verification
        access = False
        if user_inputed == None:
            user_inputed = self.ids.Usuario.text
        if pass_inputed == None:
            pass_inputed = self.ids.Senha.text
        results = session.query(usuarios).where(usuarios.Usuario == user_inputed).where(usuarios.Senha == pass_inputed).all()
        for result in results:
            access = True
            user_data = {'usuario':result.Usuario, 'senha':result.Senha, 'tipo':result.Tipo}
            print(user_data)
        # succesful
        if access == True:
            app.root.remove_widget(app.login)
            app.dash = DashBoard()
            app.root.add_widget(app.dash)
            topbar = app.dash.ids.tpb
            app.set_user(user_data['usuario'], topbar=topbar)
            session.add(historico_de_acessos(Usuario=app.usuario, Status='Entrada'))
            session.commit()
        # Failed
        else:
            print('Acesso Negado')
        # always do
        self.ids.Usuario.text = ''
        self.ids.Senha.text = ''

class Login(MDCard):
    pass
