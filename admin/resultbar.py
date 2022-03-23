from imports import *

class ColumnLabel(MDLabel):
    pass
class ColumnCell(MDBoxLayout):
    def __init__(self, text, **kwargs):
        super().__init__(**kwargs)
        self.add_widget(ColumnLabel(text=text))

class Columns(MDBoxLayout):
    def __init__(self, names, **kwargs):
        super().__init__(**kwargs)
        self.add_widget(ColumnCell(text='', size_hint_x=None, width='30dp'))
        for column in names:
            self.add_widget(ColumnCell(text=column))
        self.add_widget(ColumnCell(text='', size_hint_x=None, width='30dp'))

class RowLabel(MDLabel):
    pass
class RowCell(MDBoxLayout):
    def __init__(self, text, **kwargs):
        super().__init__(**kwargs)
        self.add_widget(RowLabel(text=text))

class DeleteBtn(MDTextButton):
    def delet(self):
        row = self.parent.parent.parent
        table = self.parent.parent.parent.parent
        table.remove_widget(row)
class DeleteCell(MDBoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        bg = MDBoxLayout(md_bg_color=(1, 0.3, 0, 0.9))
        bg.add_widget(DeleteBtn())
        self.add_widget(bg)

class Row(MDBoxLayout, ThemableBehavior, HoverBehavior):
    def __init__(self, data, **kwargs):
        super().__init__(**kwargs)
        self.add_widget(RowCell(text='', size_hint_x=None, width='30dp'))
        for d in data:
            self.add_widget(RowCell(text=d))
        self.add_widget(DeleteCell())
    def on_enter(self,*args):
        def save_state(widget):
            for child in widget.children:
                save_state(child)
                if 'RowLabel' in str(child):
                    child.md_bg_color = (1, 0.80, 0.5, 1)
        save_state(self)
    def on_leave(self,*args):
        def save_state(widget):
            for child in widget.children:
                save_state(child)
                if 'RowLabel' in str(child):
                    child.md_bg_color = (1, 1, 1, 1)
        save_state(self)
class Rows(MDBoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.adjust=Row(data=['', '', ''])
        self.add_widget(self.adjust)

class ResultBar(MDBoxLayout):
    table = ObjectProperty()
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        columns = self.table.__table__.columns.keys()
        self.add_widget(Columns(names=[c for c in columns]))
        self.add_widget(MDSeparator(height='1px', color=(0,0,0,1)))
        self.rows = Rows()
        self.add_widget(self.rows)
        self.add_widget(MDSeparator(height='1px', color=(0,0,0,1)))
        self.add_widget(Pagination())
        Clock.schedule_once(self._limpar)
    def buscar(self, quantity):
        self.limpar()
        result = session.query(self.table).limit(quantity).all()
        for r in result:
            self.rows.add_widget(Row(data=str(r).split('^')))
        #for i in range(0, quantity):
        #    self.rows.add_widget(Row(data=['Erick', '14/11/1992', 'EKSOLADM']))
    def limpar(self):
        for i in range(0, 6):
            for child in self.rows.children:
                if 'resultbar.Row ' in str(child):
                    self.rows.remove_widget(child)
    def _limpar(self, t):
        self.limpar()

class PaginationCell(MDBoxLayout):
    pass
class Pagination(MDBoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.add_widget(PaginationCell())
