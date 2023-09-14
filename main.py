from kivy.uix.gridlayout import GridLayout
from kivy.app import App
from kivy.uix.button import Button



class mainApp (App):
    def build(self):
        #layout = GridLayout(cols=2)
        #layout = GridLayout(cols=2, row_force_default=True, row_default_height=40)
        layout=GridLayout(cols=2, 
                          row_force_default=True, 
                          row_default_height=100,
                          col_force_default=True,
                          col_default_width=200)


        btn1= Button(text="Hello #1")
        #btn1= Button(text='Hello 1', size_hint_x=None, width=200)
        #btn1= Button(text='Hello 1', size_hint=(None,None), width=200, height=40)
        btn2= Button(text="World #1")

        btn3= Button(text="Hello #2")
        #btn3=Button(text='Hello 1', size_hint_x=None, width=100)
        btn4= Button(text="World #2")


        layout.add_widget(btn1)
        layout.add_widget(btn2)
        layout.add_widget(btn3)
        layout.add_widget(btn4)

        return layout
    
mainApp().run()    

