from tkinter import *
from tkinter import ttk
import os

def LOGO() :
    print('l')

def OPEN() :
    new_file = filecombo.get()
    print(new_file)
    file = open('racine','r')
    past = file.read()
    file.close()
    past += new_file + "/"
    file = open("racine","w")
    file.write(past)
    file.close()
    try :
        filelist = os.listdir(past)
        filelist = SUPP_badfile(filelist)
        print(filelist)
        filecombo['values'] = filelist
        filecombo.set(filelist[0])
    except NotADirectoryError :
        final = past[:-1]
        print(final)
        file = open('result_search.txt','w')
        file.write(final)
        file.close()
        os.remove('racine')
        Explorateur.quit()
def PAST() :
    file = open('racine','r')
    past = file.read().split('/')
    file.close()
    print(past)
    del past[-1]; del past[-1]
    past = "/".join(past)
    past += "/"
    print(past)
    file = open("racine","w")
    file.write(past)
    file.close()
    filelist = os.listdir(past)
    filelist = SUPP_badfile(filelist)
    print(filelist)
    filecombo['values'] = filelist
    filecombo.set(filelist[0])
def SUPP_badfile(liste) :
    final = []
    for i in liste : 
        if i[0] != '.' : final.append(i)
    print(final)
    return final
def start(racine) :
    file = open("racine","w")
    file.write(racine)
    file.close()
    global Explorateur
    Explorateur = Tk()
    Explorateur.title('Explorateur')
    Explorateur.geometry("350x250")
    Explorateur.minsize(350,250)
    Explorateur.maxsize(400,400)
    global filecombo
    global filelist
    filelist = os.listdir(racine)
    filelist = SUPP_badfile(filelist)
    filecombo = ttk.Combobox(Explorateur,values=filelist)
    filecombo.pack()
    global Canva_Type
    Canva_Type = Canvas(Explorateur,height=170,width=250)
    img = PhotoImage(file='Filelogo.png')
    Canva_Type.create_image(120,70,image=img,anchor='center')
    Canva_Type.pack()
    Button(Explorateur,text='Open',command=OPEN,width=20).pack()
    Button(Explorateur,text='Past',command=PAST,width=20).pack()
    Explorateur.mainloop()
racine = '/'
start(racine)