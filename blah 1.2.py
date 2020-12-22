import cv2
import numpy as np
from tkinter import*
import tkinter as tk
from PIL import Image, ImageTk

#-----------------------Functii-----------------------
def Pornire_Preprocesare():
    _, img = cap_cam.read()
    # De aici se scrie cod
    img = cv2.resize(img, (300, 200))
    rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    imagine_gri = cv2.cvtColor(rgb, cv2.COLOR_RGB2GRAY)
    Kernel_BG = setareBG
    imagine_blur_gaussian = cv2.GaussianBlur(imagine_gri, (Kernel_BG, Kernel_BG), 0)  #bg e de tip class 'int'
    margini_detectate = cv2.Canny(imagine_blur_gaussian, Prag1.get(), Prag2.get())  # 1:3 ratie
    # si pana aici se va scrie cod



    # Aici se afiseaza imaginea camerelor
    Imagine = Image.fromarray(rgb)
    iago = ImageTk.PhotoImage(Imagine)
    labelc1_io2.configure(image=iago)
    labelc1_io2.image = iago

    Imagine_2 = Image.fromarray(imagine_gri)
    iago_2 = ImageTk.PhotoImage(Imagine_2)
    labelc1_ig2.configure(image=iago_2)
    labelc1_ig2.image = iago_2

    Imagine_3 = Image.fromarray(imagine_blur_gaussian)
    iago_3 = ImageTk.PhotoImage(Imagine_3)
    labelc1_ibg2.configure(image=iago_3)
    labelc1_ibg2.image = iago_3

    Imagine_4 = Image.fromarray(margini_detectate)
    iago_4 = ImageTk.PhotoImage(Imagine_4)
    labelc1_imd2.configure(image=iago_4)
    labelc1_imd2.image = iago_4

    Fereastra_Principala.after(10, Pornire_Preprocesare)


def Oprire_Preprocesare():
    cv2.waitKey(1)

    cap_cam.release()
    cv2.destroyAllWindows()


def info_buton_BG():
    try:
        #BG = int(introducere_blur_gaussian.get())
        BG = introducere_blur_gaussian.get()
        print(type(BG))
        BG = int(BG)
        print((type(BG)))
        raspuns_bg.config(text= 'S-a introdus valoarea %d' %BG)

    except ValueError:
        raspuns_bg.config(text='Introduceti o valoare de tip intreg!')

def setareBG():
    print("Se aplica setarea")
    A = 5
    BG = introducere_blur_gaussian.get()
    print((type(BG)))
    print(BG)
    A = int(BG)
    print((type(A)))
    print(A)

    return A



def Rulare_TH():
    _, img = cap_cam.read()
    # De aici se scrie cod
    img = cv2.resize(img, (300, 200))
    rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
#-----------------------------------------------------

#---------------------Interfata-----------------------
Fereastra_Principala=Tk()
Fereastra_Principala.geometry("1600x820")#rezolutia optima pentru laptopul meu
Fereastra_Principala.title("Detectarea traiectoriilor plane")

    #-----------------------Variabile---------------------
var1 = IntVar()
var2 = IntVar()
var3 = IntVar()
var4 = IntVar()
Lungime_Scala = 255

#BG = IntVar()
BG = 5


    #-----------------------------------------------------

Bara_scroll = Scrollbar(Fereastra_Principala)
Bara_scroll.pack( side = RIGHT, fill = Y )

    #------------------Cadrul 1 Preprocesare imagine----------------------
Cadrul1 = LabelFrame(Fereastra_Principala,text="Preprocesare imagine")
Cadrul1.pack(fill="both", expand="yes")
Cadrul1.place(x=20,y=20, width=1550, height=390)

cap_cam = cv2.VideoCapture(0)

                                    #----------------Setare valoare Kernel pentru Blur Gaussian
introducere_blur_gaussian=Entry(Fereastra_Principala, textvariable='')
introducere_blur_gaussian.place(x=1010, y=300)

B_bg=Button(Fereastra_Principala, text="Setare Valoare Kernel",command=lambda:[info_buton_BG(), setareBG()])
B_bg.place(x=1010, y=330)

raspuns_bg = Label(Fereastra_Principala,text='Introduceti valoare Kernel')
raspuns_bg.place(x=1010, y=360)



                                    #------------------------------------------------------------

btn_pc1 = Button(Cadrul1, text='Preprocesare imagini',command = Pornire_Preprocesare)#aici trebuie sa introduce parametrul command si sa ii ofer un parametru pentru pornire
btn_pc1.place(x=20, y=20) #am setat ca butonul de pornire preprocesare imagini sa fie la coordonatele specificate

btn_pc1 = Button(Cadrul1, text='Oprire Preprocesare',command = Oprire_Preprocesare)#aici trebuie sa introduce parametrul command si sa ii ofer un parametru pentru pornire
btn_pc1.place(x=150, y=20) #am setat ca butonul de oprire preprocesare sa fie la coordonatele specificate

                    #Camera 1 originala preprocesare#
labelc1_io2 = Label(Cadrul1)
labelc1_io2.place(x=270, y=20) #aici va fi plasata imaginea webcamului principal, la coordonatele specificate

labelc1_io = Label(Cadrul1, text="1.Imagine originală")
labelc1_io.place(x=370, y=230)#am plasat textul la coordonatele specificate
                    #Camera 2 gri preprocesare#
labelc1_ig2 = Label(Cadrul1)
labelc1_ig2.place(x=580 ,y=20)

labelc1_ig = Label(Cadrul1, text="2.Imagine gri")
labelc1_ig.place(x=700, y=230)#am plasat textul la coordonatele specificate
                    #Camera 3 Blur Gaussian preprocesare#
labelc1_ibg2 = Label(Cadrul1)
labelc1_ibg2.place(x=890 ,y=20)

labelc1_ibg = Label(Cadrul1, text="3.Imagine Blur Gaussian")
labelc1_ibg.place(x=980, y=230)#am plasat textul la coordonatele specificate

                    #Camera 4 Margini Detectate preprocesare#
labelc1_imd2 = Label(Cadrul1)
labelc1_imd2.place(x=1200 ,y=20)

labelc1_imd = Label(Cadrul1, text="4.Imagine margini detectate")
labelc1_imd.place(x=1280, y=230)#am plasat textul la coordonatele specificate

Prag1 = Scale(Cadrul1, label="Prag1", from_=0, to=255, orient=HORIZONTAL, variable=var3, activebackground='#339999')
Prag1.set(0)
Prag1.place(x=1230, y=250, width=Lungime_Scala)

Prag2 = Scale(Cadrul1, label="Prag2", from_=0, to=255, orient=HORIZONTAL, variable=var4, activebackground='#339999')
Prag2.set(255)
Prag2.place(x=1230, y=310, width=Lungime_Scala)
    #---------------------------------------------------------------------



    #-------------------------------Cadrul2 Transformata Hough------------
Cadrul2 = LabelFrame(Fereastra_Principala,text="Transformata Hough")
Cadrul2.place(x=20,y=430, width=1550, height=390)

btn_pc2 = Button(Cadrul2, text='Rulare Transformata Hough',command = Rulare_TH)#aici trebuie sa introduce parametrul command si sa ii ofer un parametru pentru pornire
btn_pc2.place(x=20, y=20) #am setat ca butonul de pornire preprocesare imagini sa fie la coordonatele specificate

btn_pc2 = Button(Cadrul2, text='Oprire Transformata Hough',command = Oprire_Preprocesare)#aici trebuie sa introduce parametrul command si sa ii ofer un parametru pentru pornire
btn_pc2.place(x=20, y=60) #am setat ca butonul de oprire preprocesare sa fie la coordonatele specificate
    #---------------------------------------------------------------------










#-----------------------------Cadru3 Invatare Automata----------------
Cadrul3 = LabelFrame(Fereastra_Principala,text="Învățare Automată")
#Cadrul3.pack(fill="both", expand="yes", padx=20, pady=20)
#---------------------------------------------------------------------

#-----------------------------Cadru4 Invatare Automata----------------
Cadrul4 = LabelFrame(Fereastra_Principala,text="Rulare program")
#Cadrul4.pack(fill="both", expand="yes", padx=20, pady=20)
#---------------------------------------------------------------------

Fereastra_Principala.mainloop()
#-----------------------------------------------------