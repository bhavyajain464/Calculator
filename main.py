import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.core.window import Window
import re 

Builder.load_file('my.kv')
Window.fullscreen=True

class MyLayout(Widget):
    def clear(self):
        self.ids.calc_input.text=""

    def button_press(self,button):
        prior = self.ids.calc_input.text
        if(prior=="0" or prior=="inf"):
            self.ids.calc_input.text = f'{button}'
        else:
            self.ids.calc_input.text += f'{button}'

    def add(self):
        prior = self.ids.calc_input.text
        if(prior[-1]!='+' and prior[-1]!='-' and prior[-1]!='*' and prior[-1]!='/'):
            self.ids.calc_input.text+= '+'
    def subtract(self):
        prior = self.ids.calc_input.text
        if(prior[-1]!='+' and prior[-1]!='-' and prior[-1]!='*' and prior[-1]!='/'):
            self.ids.calc_input.text += '-'

    def multiply(self):
        prior = self.ids.calc_input.text
        if(prior[-1]!='+' and prior[-1]!='-' and prior[-1]!='*' and prior[-1]!='/'):
            self.ids.calc_input.text += '*'
    
    def divide(self):
        prior = self.ids.calc_input.text
        if(prior[-1]!='+' and prior[-1]!='-' and prior[-1]!='*' and prior[-1]!='/'):
            self.ids.calc_input.text += '/'

    def decimal(self):
        prior = self.ids.calc_input.text
        array = prior.split('+')[-1]
        array = array.split('*')[-1]
        array = array.split('/')[-1]
        array = array.split('-')[-1]
        if('.' not in array):
            self.ids.calc_input.text += '.'


    def equals(self):
        s = self.ids.calc_input.text
        array = s.split('-')
        for j,k in enumerate(array):
            array2 = k.split('+')
            ans2 = 0
            for p in array2:
                array3 = p.split('*')
                ans3 = 1
                for t in array3:
                    array4 = t.split('/')

                    if(array4[0]!='.'):
                        ans4 = float(array4[0])
                    else:
                        ans4 = 0
                    for i in range(1,len(array4)):
                        if(array4[i]!='.'):
                            if(float(array4[i])!=0.0):
                                ans4/=float(array4[i])
                            else:
                                self.ids.calc_input.text ="inf"
                                return
                        else:
                            self.ids.calc_input.text ="inf"
                            return
 
                    ans3*=ans4

                ans2+=ans3
            array[j]=ans2
        ans = float(array[0])
        for i in range(1,len(array)):
            ans-=array[i]

        # print(s)
        self.ids.calc_input.text =str(eval(s))
                        


class MyApp(App):
    def build(self):
        return MyLayout()
    


if __name__=='__main__':
    MyApp().run()