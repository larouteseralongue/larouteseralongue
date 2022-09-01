import time
from tkinter import *
from playsound import playsound


wind = Tk()
wind.title("Minuteur")
wind.geometry("400x600")
wind.config(bg="#191025")
wind.resizable(False, False)
heading = Label(wind, text="Minuteur", font="arial 30 bold", bg="#191025", fg="#ea3548")
heading.pack(pady=10)
Label(wind, font=("arial", 15, "bold"), text="Heure : ", bg="papaya whip").place(x=65, y=70)
current_time = Label(wind, font=("arial", 15, "bold"), text="", fg="#191025", bg="#fff")


# Clock
def clock():
    clock_time = time.strftime('%H:%M:%S %p')
    current_time.config(text=clock_time)
    current_time.after(1000, clock)


current_time = Label(wind, font=("arial", 15, "bold"), text="", fg="#191025", bg="#fff")
current_time.place(x=190, y=70)
clock()

# chrono

# Heure
hrs = StringVar()
Entry(wind, textvariable=hrs, width=2, font="arial 50", bg="#191025", fg="#fff", bd=0).place(x=30, y=155)
hrs.set("00")

# Minutes
mins = StringVar()
Entry(wind, textvariable=mins, width=2, font="arial 50", bg="#191025", fg="#fff", bd=0).place(x=150, y=155)
mins.set("00")

# Seconde
sec = StringVar()
Entry(wind, textvariable=sec, width=2, font="arial 50", bg="#191025", fg="#fff", bd=0).place(x=270, y=155)
sec.set("00")

Label(wind, text="heure", font="arial 12", bg="#191025", fg="#fff").place(x=105, y=200)
Label(wind, text="min", font="arial 12", bg="#191025", fg="#fff").place(x=225, y=200)
Label(wind, text="sec", font="arial 12", bg="#191025", fg="#fff").place(x=345, y=200)


def Timer():
    times = int(hrs.get()) * 3600 + int(mins.get()) * 60 + int(sec.get())
    while times > -1:
        minute, seconde = (times // 60, times % 60)
        heure = 0
        if minute > 60:
            heure, minute = (minute // 60, minute % 60)

        sec.set(seconde)
        mins.set(minute)
        hrs.set(heure)

        wind.update()
        time.sleep(1)
        if times == 0:
            playsound("sonnerie.mp3")
            sec.set("00")
            mins.set("00")
            hrs.set("00")
        times -= 1


def brush():
    hrs.set("00")
    mins.set("02")
    sec.set("00")


def face():
    hrs.set("00")
    mins.set("15")
    sec.set("00")


def stream():
    hrs.set("00")
    mins.set("20")
    sec.set("00")



button = Button(wind, text="Start", bg="#ae3548", bd=0, fg="#fff", width=20, height=2, font="arial 10 bold", command=Timer)
button.pack(padx=5, pady=40, side=BOTTOM)


Image1 = PhotoImage(file="brush.png")
button1 = Button(wind, image=Image1, bg="#191025", bd=0, command=brush)
button1.place(x=7, y=300)

Image2 = PhotoImage(file="face.png")
button2 = Button(wind, image=Image2, bg="#191025", bd=0, command=face)
button2.place(x=137, y=300)

Image3 = PhotoImage(file="stream.png")
button3 = Button(wind, image=Image3, bg="#191025", bd=0, command=stream)
button3.place(x=267, y=300)

wind.mainloop()
