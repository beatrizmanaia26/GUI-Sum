from tkinter import * 

janela = Tk()
janela.geometry("400x400")

n1 = Label(janela, text="Entre o primeiro número:") 
n1.place(x=119,y=100, anchor=CENTER) 

n2 = Label(janela, text="Entre o segundo número:") 
n2.place(x=120,y=140, anchor=CENTER) 

resp = Label(janela, text="Resultado:") 
resp.place(x=80,y=180, anchor=CENTER) 

caixa_texto = Entry(janela, width=15,font = ("Comic Sans", 14)) 
caixa_texto.place(x=200,y=90) 

caixa_texto2 = Entry(janela, width=15,font = ("Comic Sans", 14))
caixa_texto2.place(x=200,y=130)

caixa_texto3 = Entry(janela, width=15,font = ("Comic Sans", 14))
caixa_texto3.place(x=120,y=170)

def soma():
    n1 = int(caixa_texto.get())
    n2 = int(caixa_texto2.get())
    resp = n1 + n2
    caixa_texto3.insert(0, resp)
    
def apagar():
    caixa_texto.delete(0,"end")
    caixa_texto2.delete(0,"end")
    caixa_texto3.delete(0,"end")
    
botao = Button(janela,text="Soma!", command=soma)
botao.place(x=200,y=250)

botao2 = Button(janela,text="Apagar!", command=apagar)
botao2.place(x=200,y=350)

janela.mainloop() 