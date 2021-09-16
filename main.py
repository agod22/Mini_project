import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty, StringProperty
from kivy.lang import Builder
from kivy.uix.popup import Popup
from client import send_data


class MyGrid(Widget):
    Builder.load_file('Predictor.kv')
    name = ObjectProperty(None)
    age = ObjectProperty(None)
    sex = ObjectProperty(None)
    cpt = ObjectProperty(None)
    rbp = ObjectProperty(None)
    chol = ObjectProperty(None)
    fbs = ObjectProperty(None)
    rer = ObjectProperty(None)
    mhr = ObjectProperty(None)
    exia = ObjectProperty(None)
    oldpeak = ObjectProperty(None)
    slope = ObjectProperty(None)
    num = ObjectProperty(None)
    thal = ObjectProperty(None)
    
    def btn(self):
        print("Name:", self.name.text, "Age:", self.age.text)
        name1 = self.name.text
        age1 = self.age.text
        sex1 = self.sex.text
        cpt1 = self.cpt.text
        rbp1 = self.rbp.text
        chol1 = self.chol.text
        fbs1 = self.fbs.text
        rer1 = self.rer.text
        mhr1 = self.mhr.text
        exia1 = self.exia.text
        oldpeak1 = self.oldpeak.text
        slope1 = self.slope.text
        num1 = self.num.text
        thal1 = self.thal.text
        r = self.process(name1,age1,sex1,cpt1,rbp1,chol1,fbs1,rer1,mhr1,exia1,oldpeak1,slope1,num1,thal1)
        print(r)
        show_popup(r,name1)
        self.name.text = ""
        self.age.text = ""
        self.sex.text = ""
        self.cpt.text = ""
        self.rbp.text = ""
        self.chol.text = ""
        self.fbs.text = ""
        self.rer.text = ""
        self.mhr.text = ""
        self.exia.text = ""
        self.oldpeak.text = ""
        self.slope.text = ""
        self.num.text = ""
        self.thal.text = ""

    def process(self,a,b,c,d,e,f,g,h,i,j,k,l,m,n):
        b = int(b)
        c = 1 if (c=='M') else 0
        d = int(d)
        e = int(e)
        f = int(f)
        g = 1 if (int(g)>120) else 0
        h = int(h)
        i = int(i)
        j = int(j)
        k = float(k)
        l = int(l)
        m = int(m)
        n = int(n)
        s = [b,c,d,e,f,g,h,i,j,k,l,m,n]
        r = send_data(s)
        return r


def show_popup(f,name):
    if(f==1):
        msg = "Dear " + name + ",\nUnfortunately, you are at high risk of a heart disease or already have one.\n We would recommend you balanced diet and regular exercise.\n Please consult a doctor.\n Some commonly recommended and precribed medicines are: \n1. Captopril(Capoten)\n2. Enalapril(Vasotec)\n3. Fosinopril(Monopril)\n 4. Lisinopril(Prinivil, Zestril)\n5. Perindopril(Aceon)\n6. Quinapril(Accupril)\n\nStay Healthy! Stay Safe!"
    else:
        msg = "Congratulations " + name + "! You are at low risk of having any heart disease.\n We would still recommend you to have a balanced diet and regular exercise.\n And do not miss your health checkups.\n Stay Healthy! Stay Safe!"

    popupWindow = Popup(title="Results", content =Label(text = msg), size_hint=(None,None), size=(600,400))

    #content = Button(text = "CLOSE")
    #content.bind(on_press = popup.dismiss)

    popupWindow.open()

#interface = Builder.load_file('Predictor.kv')

class PredictorApp(App):
    def build(self):
        return MyGrid()

if __name__ == "__main__":
    PredictorApp().run()
