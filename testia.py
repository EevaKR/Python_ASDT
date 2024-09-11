import pandas as pd
import matplotlib.pyplot as plt
import winsound
import random
import time
import tkinter as tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

ennatyksen_sanakirja = {
    1912: {'aika': 10.6, 'juoksija': 'Donald Lippincott'},
    1936: {'aika': 10.2, 'juoksija': 'Jesse Owens'},
    1968: {'aika': 9.95, 'juoksija': 'Jim Hines'},
    1988: {'aika': 9.79, 'juoksija': 'Ben Johnson'},
    2009: {'aika': 9.58, 'juoksija': 'Usain Bolt'}
}

df = pd.read_csv(r'C:\Users\Eeva\OneDrive\Tiedostot\Syksy_2024\Python_ASDH\data2.csv', delimiter=';', quotechar='"')

vuodet = [1912, 1936, 1968, 1988, 2009]
ajat = [10.6, 10.2, 9.95, 9.79, 9.58]

plt.plot(vuodet, ajat, marker='o')
plt.title('100 metrin maailmanennätysajat vuosina 1912 - 2009')
plt.xlabel('Vuosi')
plt.ylabel('Aika (s)')
plt.show()

leijonat = {
    'Simba': {'nopeus': 10.5, 'kunto': 'erinomainen'},
    'Nala': {'nopeus': 9.8, 'kunto': 'hyvä'},
    'Scar': {'nopeus': 8.5, 'kunto': 'kohtalainen'},
    'Mufasa': {'nopeus': 11.0, 'kunto': 'huippu'},
    'Kovu': {'nopeus': 9.9, 'kunto': 'hyvä'}
}

ikkuna = tk.Tk()
ikkuna.title("Juoksukilpailu")
ikkuna.geometry("500x800+500+300")

###################################TESTIA

window = tk.Tk()
window.title("Juoksukilpailu")
window.geometry("600x400")

canvas = tk.Canvas(window, width=600, height=400, bg="white")
canvas.pack()

canvas.create_line(50, 300, 550, 300, fill="black", width=2)  
canvas.create_line(50, 50, 50, 300, fill="black", width=2)   

canvas.create_text(580, 310, text="Maali", anchor='e')

runner = canvas.create_oval(45, 290, 65, 310, fill="blue", outline="black")
runner2 = canvas.create_oval(45, 290, 65, 310, fill="green", outline="black")

runner_speed = 1  
runner_speed2 = 2  

def move_runner():
    global runner_speed
    current_pos = canvas.coords(runner)  
    if current_pos[2] < 550:  
        new_x1 = current_pos[0] + runner_speed
        new_x2 = current_pos[2] + runner_speed
        canvas.coords(runner, new_x1, current_pos[1], new_x2, current_pos[3])
        window.after(1000, move_runner)  
    else:
        canvas.create_text(300, 150, text="Ernesti maaliin!", font=('Helvetica', 24), fill="red")

def move_runner2():
    global runner_speed2
    current_pos2 = canvas.coords(runner2)  
    if current_pos2[2] < 550:  
        new_x12 = current_pos2[0] + runner_speed2
        new_x22 = current_pos2[2] + runner_speed2
        canvas.coords(runner2, new_x12, current_pos2[1], new_x22, current_pos2[3])
        window.after(1000, move_runner2)  
    else:
        canvas.create_text(300, 150, text="Kernesti maaliin!", font=('Helvetica', 24), fill="blue")

move_runner()
move_runner2()


#############################TESTI LOPPUU

ernestin_nopeus = random.uniform(9.0, 12.0)
kernestin_nopeus = random.uniform(9.0, 12.0)

ernesti_aika = 100 / ernestin_nopeus  
kernesti_aika = 100 / kernestin_nopeus

def yhteislahto():
    print("Yhteislähtö!")
    winsound.Beep(1000, 500)

def toiminto():
    yhteislahto()

def toiminto2():
    print("Harjoittele 1 päivä")

def tuota_aani():
    global markkerin_x_koordinantti
    markkerin_x_koordinantti += 1
    markkeri.place(x=markkerin_x_koordinantti, y=500)
    winsound.Beep(440, 200)

def tuota_aani2():
    winsound.Beep(500, 1000)
    for _ in range(10):
        tuota_aani()

def race_simulation():
    global markkerin_x_koordinantti, kernestin_x_koordinantti
    while markkerin_x_koordinantti < 300 and kernestin_x_koordinantti < 300:
        time.sleep(0.5)
        
        markkerin_x_koordinantti += ernesti_aika
        markkeri.place(x=markkerin_x_koordinantti, y=500)
        winsound.Beep(440, 200)
        
        kernestin_x_koordinantti += kernesti_aika
        markkeri2.place(x=kernestin_x_koordinantti, y=550)
        winsound.Beep(500, 200)
        
        if markkerin_x_koordinantti >= 300 and kernestin_x_koordinantti >= 300:
            if ernesti_aika < kernesti_aika:
                print("Ernesti voitti!")
            else:
                print("Kernesti voitti!")
            break

def harjoittele_paiva():
    global ernestin_nopeus, kernestin_nopeus
    for _ in range(100):
        ernestin_nopeus *= 1.001
        kernestin_nopeus *= 1.001
        print(f"Ernesti nopeus: {ernestin_nopeus}, Kernesti nopeus: {kernestin_nopeus}")
        time.sleep(0.01)

tekstijuttu = tk.Label(ikkuna, text="Juoksukilpailu")
tekstijuttu.place(x=10, y=30)

markkerin_x_koordinantti = 10
kernestin_x_koordinantti = 10

markkeri = tk.Label(ikkuna, text="X")
markkeri.place(x=markkerin_x_koordinantti, y=500)

markkeri2 = tk.Label(ikkuna, text="Y")
markkeri2.place(x=kernestin_x_koordinantti, y=550)

painike = tk.Button(ikkuna, text="Harjoittele", command=toiminto)
painike.place(x=10, y=60)

# painike_2 = tk.Button(ikkuna, text="Ota askel", command=tuota_aani)
# painike_2.place(x=100, y=60)

painike_3 = tk.Button(ikkuna, text="1 päivän harj.", command=toiminto2)
painike_3.place(x=100, y=60)

# painike_4 = tk.Button(ikkuna, text="Ääni", command=tuota_aani2)
# painike_4.place(x=220, y=60)

fig = Figure(figsize=(5, 4), dpi=100)
ax = fig.add_subplot(111)
ax.plot(1, 1, 'b+')

kuvaaja_canvas = FigureCanvasTkAgg(fig, master=ikkuna)
kuvaaja_canvas.draw()
kuvaaja_canvas.get_tk_widget().place(x=20, y=700)

ikkuna.mainloop()

