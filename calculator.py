import customtkinter 
from customtkinter import *

set_appearance_mode("dark")
set_default_color_theme("green")

root = CTk()
root.title('CalDrain')
root.geometry('600*400')
root.resizable(False, False)
button_font = ('Helvetica', 19)  
buttonDo_font = ('Helvetica', 29) 
label_font = ('Helvetica',15)


btnNUM = ''
btnDO =''
A = True
B = ''
C = ''
D = []
Equalizer = True
e = CTkEntry(root, width=200,font=button_font, corner_radius=50, height=50,)
e.grid(row=0, column=1, pady = 25)

label = CTkLabel(root, text='', font = label_font, text_color='#C6C0C0')
label.grid(row=0, column=3, pady = 25)

class ButtonNum:
    def __init__(self,  rowd, columnd, text =''):
        global btnNUM
        self.button = CTkButton(root, text=text, command=lambda:self.get_text(text), height=100, font=button_font, )
        self.button.grid(row=rowd, column=columnd, padx=5, pady=10,)
        
    def get_text(self, text):
        if Equalizer == False:
            clear()
        global A
        global C
        e.insert(END, text)
        A = False
        C = C + text
        
class ButtonDO:
    def __init__(self,  rowd, columnd, text =''):
        global btnDO
        self.button = CTkButton(root, text=text,command=lambda:self.clicked(text), height=100, font = buttonDo_font)
        self.button.grid(row=rowd, column=columnd, padx=15, pady=5,)
    def clicked(self, text):
        global A
        global B
        global C
        global D
        A1 = '0.0'
        A2 = '1.0'
        

        D.append(C)
        
        entry_text = e.get()
        label.configure(text=label.cget('text') + entry_text + text)
                
        if A == False:
            if B =='+':
                for i in D :
                    A1 = float(A1) + float(i)
                A1 = str(A1)
                label.configure(text= A1 + text)
                
                D.clear()
                D.append(A1)

            if B == '-':
                for i in D :
                    if A1 != '0.0':
                        A1 = float(A1) - float(i)
                    if A1 == '0.0':
                        A1 = float(i)
                A1 = str(A1)
                label.configure(text=A1 + text)

                D.clear()
                D.append(A1)
            if B == 'x':
                for i in D :
                    A2 = float(A2) * float(i)
                
                A2 = str(A2)
                label.configure(text=A2 + text)
            if B == '/':
                first = '0'
                second = '0'
                for i in D :
                    if second!= '0':
                        first = float(i)
                        D2 = float(second) / float(first)
                    if second == '0':
                        second = float(i)
                D2 = str(D2)
                label.configure(text=D2 + text)
        A = True
        B = ''
        C = ''
        e.delete(0, END)
        
        A = True
        B = text
        if Equalizer == False:
            clear()
        
def equal():
    global A
    global B
    global C
    global D
    global D1 
    global D2
    global Equalizer
    D1 = '0.0'
    D2 = '1.0'
    
    get = float(e.get())

    D.append(get)
    e.delete(0, END)

    if B == '+':
        for i in D :
            D1 = float(D1) + float(i)
            
        label.configure(text=D1, text_color='#2AFF00')
        D.clear()
        A = True
        B = ''
        C = ''
    if B == '-':
        for i in D :
            if D1 != '0.0':
                D1 = float(D1) - float(i)
            if D1 == '0.0':
                D1 = float(i)
        label.configure(text=D1, text_color='#2AFF00')
        D.clear()
        A = True
        B = ''
        C = ''
    if B == 'x':
        for i in D :
            D2 = float(D2) * float(i)
            
        label.configure(text=D2, text_color='#2AFF00')
        D.clear()
        A = True
        B = ''
        C = ''
    if B == '/':
        first = '0'
        second = '0'
        for i in D :
            if second!= '0':
                first = float(i)
                D2 = float(second) / float(first)
            if second == '0':
                second = float(i)
            
        label.configure(text=D2, text_color='#2AFF00')
        D.clear()
        A = True
        B = ''
        C = ''
    
    Equalizer = False
    

def clear():
    global A
    global B
    global C
    global D
    global D1 
    global Equalizer
    D1 = '0.0'
    D.clear()
    e.delete(0, END)
    label.configure(text='', text_color='#C6C0C0')
    A = True
    B = ''
    C = ''
    Equalizer = True
   

btn1 = ButtonNum(1, 0, '1')
btn2 = ButtonNum(1, 1, '2')
btn3 = ButtonNum(1, 2, '3')
btn4 = ButtonNum(2, 0, '4')
btn5 = ButtonNum(2, 1, '5')
btn6 = ButtonNum(2, 2, '6')
btn7 = ButtonNum(3, 0, '7')
btn8 = ButtonNum(3, 1, '8')
btn9 = ButtonNum(3, 2, '9')
btn0 = ButtonNum(4, 1, '0')
btnplus = ButtonDO(1, 3, '+')
btnmin = ButtonDO(2 , 3, '-')
btnmul = ButtonDO(3, 3, 'x')
btndiv = ButtonDO(4, 3, '/')
btnEquals = CTkButton(root, text='=', command=equal, height=100, font=buttonDo_font, fg_color='white', text_color='black', hover_color='#E4E2E2')
btnEquals.grid(row=4, column=2, padx=5, pady=5)
buttonClear = CTkButton(root, text='C', command=clear, height=100, font=button_font, fg_color='red', text_color='black', hover_color='#AB0805')
buttonClear.grid(row=4, column=0, padx=5, pady=5)

root.mainloop()