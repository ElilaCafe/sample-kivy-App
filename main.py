from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.utils import platform



Builder.load_string('''
<myboxLayout>:


    BoxLayout:
        orientation:"vertical"
        size:root.width,root.height

        TextInput:
            id:calc_input
            text:"0"
            halign:"right"
            font_size: 55 
            size_hint: (1,.15)

        GridLayout:
            cols:4
            rows:5

            Button:
                text:"%"
                size_hint:(.2,.2)
                font_size:32
            Button:
                text:"C"
                size_hint:(.2,.2)
                font_size:32
                on_press:root.clear()
            Button:
                id:name_clear
                text:u"\u00AB"
                size_hint:(.2,.2)
                font_size:32
                on_press:root.remove()
            Button:
                text:"/"
                size_hint:(.2,.2)
                font_size:32
                on_press:root.math_sign("/")
            #row
            Button:
                text:"7"
                size_hint:(.2,.2)
                font_size:32
                background_color:(157/255,157/255,157/255,1)
                on_press:root.press(7)
            Button:
                text:"8"
                size_hint:(.2,.2)
                font_size:32
                background_color:(157/255,157/255,157/255,1)
                on_press:root.press(8)
            Button:
                text:"9"
                size_hint:(.2,.2)
                font_size:32
                background_color:(157/255,157/255,157/255,1)
                on_press:root.press(9)
            Button:
                text:"X"
                size_hint:(.2,.2)
                font_size:32
                on_press:root.math_sign("*")
            #row
            Button:
                text:"4"
                size_hint:(.2,.2)
                font_size:32
                background_color:(157/255,157/255,157/255,1)
                on_press:root.press(4)
            Button:
                text:"5"
                size_hint:(.2,.2)
                font_size:32
                background_color:(157/255,157/255,157/255,1)
                on_press:root.press(5)
            Button:
                text:"6"
                size_hint:(.2,.2)
                font_size:32
                background_color:(157/255,157/255,157/255,1)
                on_press:root.press(6)
            Button:
                text:"-"
                size_hint:(.2,.2)
                font_size:32
                on_press:root.math_sign("-")
            #row
            Button:
                text:"1"
                size_hint:(.2,.2)
                font_size:32
                background_color:(157/255,157/255,157/255,1)
                on_press:root.press(1)
            Button:
                text:"2"
                size_hint:(.2,.2)
                font_size:32
                background_color:(157/255,157/255,157/255,1)
                on_press:root.press(2)
            Button:
                text:"3"
                size_hint:(.2,.2)
                font_size:32
                background_color:(157/255,157/255,157/255,1)
                on_press:root.press(3)
            Button:
                text:"+"
                size_hint:(.2,.2)
                font_size:32
                on_press:root.math_sign("+")
            #row
            Button:
                text:"+/-"
                size_hint:(.2,.2)
                font_size:32
                background_color:(157/255,157/255,157/255,1)
                on_press:root.pos_neg()
            Button:
                text:"0"
                size_hint:(.2,.2)
                font_size:32
                background_color:(157/255,157/255,157/255,1)
                on_press:root.press(0)
            Button:
                text:"."
                size_hint:(.2,.2)
                font_size:32
                background_color:(157/255,157/255,157/255,1)
                on_press:root.dot()
            Button:
                text:"="
                size_hint:(.2,.2)
                font_size:32
                on_press:root.equal()                    
                    
''')

class myboxLayout(Widget):
    def clear (self):
        self.ids.calc_input.text="0"

    #create function to remove last character in textbox
    def remove(self):
        #create a variable that contain whatever was in the text box already
        prior= self.ids.calc_input.text
        prior=prior[:-1]
        self.ids.calc_input.text=prior

    #create decimal function
    def dot(self):
        #create a variable that contain whatever was in the text box already
        prior= self.ids.calc_input.text
        #finde dot is wich site of oprator
        if "+" in prior:
            numbs=prior.split("+")
            if "." in numbs[-1]:
                pass
            else:
                self.ids.calc_input.text=f'{prior}.'
        elif "-" in prior:
            numbs=prior.split("-")
            if "." in numbs[-1]:
                pass
            else:
                self.ids.calc_input.text=f'{prior}.'
        elif "*" in prior:
            numbs=prior.split("*")
            if "." in numbs[-1]:
                pass
            else:
                self.ids.calc_input.text=f'{prior}.'
        elif "/" in prior:
            numbs=prior.split("/")
            if "." in numbs[-1]:
                pass
            else:
                self.ids.calc_input.text=f'{prior}.'

        #if haven't oprator
        else:
            if '.' in prior:
                pass
            else:
                self.ids.calc_input.text=f'{prior}.'

    #creat function to make text box positive and negative
    def pos_neg(self):
        #create a variable that contain whatever was in the text box already
        prior= self.ids.calc_input.text
        if "-" in prior:
            self.ids.calc_input.text=f'{prior.replace("-","")}'

        else:
            self.ids.calc_input.text=f'-{prior}'



    #create a button pressing function
    def press (self,button):
        #create a variable that contain whatever was in the text box already
        prior= self.ids.calc_input.text

        #test an Errror first
        if prior=="Error":
            prior=""

        #determine if o is setting there
        if prior == "0":
            self.ids.calc_input.text=""
            self.ids.calc_input.text=f'{button}'
        else:
            self.ids.calc_input.text=f'{prior}{button}'

        #create additon function
    def math_sign (self,sign):
         #create a variable that contain whatever was in the text box already
         prior= self.ids.calc_input.text
         #don't adding two or more operators to contniue of each other 
         if prior[-1] =="+" or prior[-1] =="-" or prior[-1] =="*" or prior[-1] =="/" :
             pass
         else:
            #Doing previous oprator
            if "+" in prior:
                numbers=prior.split("+")
                answer=float(numbers[0])+float(numbers[1])
                prior=str(answer)
            elif "-" in prior:
                numbers=prior.split("-")
                answer=float(numbers[0])-float(numbers[1])
                prior=str(answer)
            elif "*" in prior:
                numbers=prior.split("*")
                answer=float(numbers[0])*float(numbers[1])
                prior=str(answer)
            elif "/" in prior:
                numbers=prior.split("/")
                if numbers[0]=="0":
                    answer="0"
                elif numbers[1]=="0":
                    answer="Error"
                else:
                    answer=float(numbers[0])/float(numbers[1])

                prior=str(float(answer))

            #slap a plus sign in to the text box
            self.ids.calc_input.text=f'{prior}{sign}'


    def equal (self):
        #create a variable that contain whatever was in the text box already
        prior= self.ids.calc_input.text
        #Error handling
        try:
        #Evaluate the math from the text box
            answer=eval(prior)
            self.ids.calc_input.text=str(answer)
        except:
            self.ids.calc_input.text="Error"

              
         
         


        
        
class mycalculatorApp(App):
    def build(self):
        if platform == 'android' or platform == 'ios':
            Window.maximize()
        else:
            Window.size = (480,800)
        return myboxLayout()
    
if __name__=="__main__":
    mycalculatorApp().run()