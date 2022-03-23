from imports import *

class Content(MDBoxLayout):
    pass

class MyTogBut(MDFlatButton, MDToggleButton):
    def action(self):
        if self.state == 'down':
            self.parent.md_bg_color = (1, 0.6, 0, 1)
            gerenciador = self.parent.parent.parent.parent.parent.parent.ids.g
            gerenciador.children[0].resultbar.limpar()
            gerenciador.transition.direction = 'down'
            gerenciador.current = self.text
        elif self.state == 'normal':
            self.parent.md_bg_color = (1,1,1,0.75)

class MyHoverBG(MDBoxLayout, ThemableBehavior, HoverBehavior):
    def __init__(self, text, group, **kwargs):
        super().__init__(**kwargs)
        self.add_widget(MyTogBut(text=text, group=group))
    def on_enter(self, *args):
        if not self.md_bg_color == [1, 0.6, 0, 1]:
            self.md_bg_color = (1, 0.6, 0, 0.5)
    def on_leave(self, *args):
        if not self.md_bg_color == [1, 0.6, 0, 1]:
            self.md_bg_color = (1,1,1,0)

class MyPanel(MDExpansionPanelOneLine):
    pass

class SideBar(ScrollView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        gdl = MDGridLayout(cols=1, adaptive_height=True, spacing=10, md_bg_color=(1,1,1,0.75))
        for key, value in App.get_running_app().tables.items():
            content = Content()
            for v in value:
                content.add_widget(MyHoverBG(text=v.__tablename__, group='sidebar'))
                content.add_widget(MDSeparator(height='1px'))#
            panel = MDExpansionPanel(content=content, panel_cls=MyPanel(text=key))
            gdl.add_widget(panel)
        self.add_widget(gdl)
