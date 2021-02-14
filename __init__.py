import os
from cudatext import *
import cudatext_keys as keys

fn_icon = os.path.join(os.path.dirname(__file__), 'terminal.png')

class Command:
    def __init__(self):
        self.h_dlg = None
    
    def open_init(self):

        self.h_dlg = self.init_form()
        
        app_proc(PROC_BOTTOMPANEL_ADD_DIALOG, ('Fake', self.h_dlg, fn_icon))


    def init_form(self):
        h = dlg_proc(0, DLG_CREATE)
        dlg_proc(h, DLG_PROP_SET, prop={
            'border': False,
            'on_key_down': self.form_key_down,
            })

        n = dlg_proc(h, DLG_CTL_ADD, 'editor_combo')
        dlg_proc(h, DLG_CTL_PROP_SET, index=n, prop={
            'name': 'input',
            'h': 26,
            'align': ALIGN_TOP,
            })
            
        self.input = Editor(dlg_proc(h, DLG_CTL_HANDLE, index=n))

        self.input.set_prop(PROP_ONE_LINE, True)
        self.input.set_prop(PROP_GUTTER_ALL, True)
        self.input.set_prop(PROP_GUTTER_NUM, False)
        self.input.set_prop(PROP_GUTTER_FOLD, False)
        self.input.set_prop(PROP_GUTTER_BM, False)
        self.input.set_prop(PROP_GUTTER_STATES, False)
        self.input.set_prop(PROP_UNPRINTED_SHOW, False)
        self.input.set_prop(PROP_MARGIN, 2000)
        self.input.set_prop(PROP_MARGIN_STRING, '')
        self.input.set_prop(PROP_HILITE_CUR_LINE, False)
        self.input.set_prop(PROP_HILITE_CUR_COL, False)

        return h
        
            
    def on_snippet(self, ed_self, snippet_id, snippet_text):
        print('=== on snippet')
        print(f' == on snippet: ed:{ed_self}, snippet_id:{snippet_id}; text:{snippet_text}')
        
    def form_key_down(self, id_dlg, id_ctl, data='', info=''):

        #Enter
        if (id_ctl==keys.VK_ENTER) and (data==''):
            text = self.input.get_text_line(0)
            self.input.set_text_all('')
            self.input.set_caret(0, 0)
            self.run_cmd(text)
            return False
            
        elif id_ctl == ord('R')  and data == 'c':
            text = 'one\ttwo\tthree'
            self.input.complete_alt(text, snippet_id='fake_snippet', len_chars=0)
            return False
            
    def real_complete(self):
        text = 'one\ttwo\tthree'
        ed.complete_alt(text, snippet_id='fake_snippet', len_chars=0)
            
            
    def open(self):
        if not self.h_dlg:
            self.open_init()
            

        