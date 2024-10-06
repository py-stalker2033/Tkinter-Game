from tkinter import *
import tkinter as tk

window = tk.Tk()
window.title("Стрелочки")
window.geometry("1000x700")

label = tk.Label(window, text="Приветствую!")
label.pack()

def arrow( x) :
    global arr
    if arr[x] == "->":
        if arr[x + 1]== " ":
            arr[x + 1]= "->"
            arr[x] = " "

        elif arr[x + 2]== " " and  arr[x + 1]== "<-":
            arr[x + 2] = "->"
            arr[x] = " "
        else:
            title = Label(window, text='Не тицяй, їнотику паласкунчику', font=40, bg='gray')
            title.pack()


    if arr[x] == "<-":
        if arr[x - 1]== " ":
            arr[x - 1]= "<-"
            arr[x] = " "

        elif arr[x - 2]== " " and  arr[x - 1]== "->":
            arr[x - 2] = "<-"
            arr[x] = " "
        else:
            title = Label(window, text='Не тицяй, їнотику паласкунчику', font=40, bg='gray')
            title.pack()

    print(arr)
    if arr==["<-","<-","<-"," ","->","->","->"]:
        title=Label(window, text='Ви вийграли',font=40,bg='gray')
        title.pack()



def obnova() :


    first_arrow.config(text=arr[0],
                    font=('Comic Sans MS',20),
                    bg='white',

                       )
    second_arrow.config(text=arr[1],
                        font=('Comic Sans MS', 20),
                        bg='white',

                        )
    third_arrow.config(text=arr[2],
                    font=('Comic Sans MS',20),
                    bg='white',

                       )
    fourth_arrow.config(text=arr[3],
                        font=('Comic Sans MS', 20),
                        bg='white',

                        )
    fifths_arrow.config(text=arr[4],
                        font=('Comic Sans MS', 20),
                        bg='white',
                        )
    sixth_arrow.config(text=arr[5],
                        font=('Comic Sans MS', 20),
                        bg='white',
                        )
    seventh_arrow.config(text=arr[6],
                        font=('Comic Sans MS', 20),
                        bg='white',
                        )

def reset_arrows():
    global arr
    # Возвращаем стрелочки в исходное состояние
    arr = ["->", "->", "->", " ", "<-", "<-", "<-"]
    obnova()

arr=["->","->","->"," ","<-","<-","<-"]
first_arrow = tk.Button(window,

                    text=arr[0],
                    font=('Comic Sans MS',20),
                    bg='white',
                    command=lambda:(arrow(0), obnova()),

                        )
first_arrow.place(x=120,y=300)

second_arrow = Button(window,
                    text=arr[1],
                    font=('Comic Sans MS',20),
                    bg='white',
                    command=lambda: (arrow(1), obnova())
                        )
second_arrow.place(x=220,y=300)

third_arrow = Button(window,
                    text=arr[2],
                    font=('Comic Sans MS',20),
                    bg='white',
                    command=lambda: (arrow(2),obnova())
                        )
third_arrow.place(x=320,y=300)
fourth_arrow =Button(window,
                    text=arr[3],
                    font=('Comic Sans MS',20),
                    bg='white',
                    command=lambda: (arrow(3), obnova())
                        )
fourth_arrow.place(x=420,y=300)

fifths_arrow=Button(window,
                    text=arr[4],
                    font=('Comic Sans MS',20),
                    bg='white',
                    command=lambda: (arrow(4), obnova())

                        )
fifths_arrow.place(x=520,y=300)


sixth_arrow=Button(window,
                    text=arr[5],
                    font=('Comic Sans MS',20),
                    bg='white',
                    command=lambda: (arrow(5), obnova())

                        )
sixth_arrow.place(x=620,y=300)


seventh_arrow=Button(window,
                    text=arr[6],
                    font=('Comic Sans MS',20),
                    bg='white',
                    command=lambda: (arrow(6), obnova())

                        )
seventh_arrow.place(x=720,y=300)

reset_button = Button(window, text="Заново", font=('Comic Sans MS', 15), command=reset_arrows)
reset_button.place(x=400, y=500)

window.mainloop()