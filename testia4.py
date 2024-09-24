import tkinter as tk
import winsound
import random

Ernesti_speed = 5
tomato_speed = 10
kernesti_pos = random.randint(50, 250)  

scores = {'Ernesti': 0, 'Kernesti': 0}

def liiku_ernesti():
    current_pos = canvas.coords(Ernesti)
    if current_pos[2] < 550:  
        new_x1 = current_pos[0] + Ernesti_speed
        new_x2 = current_pos[2] + Ernesti_speed
        canvas.coords(Ernesti, new_x1, current_pos[1], new_x2, current_pos[3])
        ikkuna.after(50, liiku_ernesti)
    else:
        heita_tomaatti('Ernesti')

def liiku_kernesti():
    current_pos = canvas.coords(Kernesti)
    if current_pos[2] < 550:  
        new_x1 = current_pos[0] + Ernesti_speed
        new_x2 = current_pos[2] + Ernesti_speed
        canvas.coords(Kernesti, new_x1, current_pos[1], new_x2, current_pos[3])
        ikkuna.after(50, liiku_kernesti)
    else:
        heita_tomaatti('Kernesti')

def heita_tomaatti(player):
    if player == 'Ernesti':
        current_pos = canvas.coords(Ernesti)
    else:
        current_pos = canvas.coords(Kernesti)

    tomato = canvas.create_oval(current_pos[0], current_pos[1], current_pos[0] + 10, current_pos[1] + 10, fill="red")

    def liikuta_tomaattia():
        nonlocal tomato
        tomato_pos = canvas.coords(tomato)
        if tomato_pos[2] < 550:  
            new_x1 = tomato_pos[0] + tomato_speed
            new_x2 = tomato_pos[2] + tomato_speed
            new_y1 = tomato_pos[1] + random.randint(-5, 5)  
            new_y2 = tomato_pos[3] + random.randint(-5, 5)
            canvas.coords(tomato, new_x1, new_y1, new_x2, new_y2)
            ikkuna.after(50, liikuta_tomaattia)
        else:
            tarkista_osuma(tomato_pos, player)
            canvas.delete(tomato)

    liikuta_tomaattia()

# Function to check if the tomato hit the target
def tarkista_osuma(tomato_pos, player):
    if 50 < tomato_pos[1] < 300:  # Assuming target is in this range
        winsound.Beep(1000, 300)
        canvas.create_text(300, 200, text=f"{player} Osui!", font=('Helvetica', 24), fill="green")
        scores[player] += 1  # Increase score
    else:
        winsound.Beep(500, 300)
        canvas.create_text(300, 200, text=f"{player} Ei osunut!", font=('Helvetica', 24), fill="red")

    paivita_pisteet()

# Function to update the score display
def paivita_pisteet():
    score_label.config(text=f"Ernesti: {scores['Ernesti']} - Kernesti: {scores['Kernesti']}")

# Function to reset the scores
def nollaa_pisteet():
    scores['Ernesti'] = 0
    scores['Kernesti'] = 0
    paivita_pisteet()

#sijoitetaan ernesti satunnaiseen kohtaan
def sijoita_ernesti_random():
    random_y = random.randint(50, 300)
    canvas.coords(Ernesti, 45, random_y, 65, random_y + 20)

#tehään tkinter ikkuna
ikkuna = tk.Tk()
ikkuna.title("Tomaatinheittokilpailu")
ikkuna.geometry("600x400")

title = tk.Label(ikkuna, text="Ernestin ja Kernestin kisa")
title.place(x=10, y=10)

canvas = tk.Canvas(ikkuna, width=600, height=400, bg="white")
canvas.pack()

canvas.create_line(50, 300, 550, 300, fill="black", width=2)
canvas.create_line(550, 50, 550, 300, fill="red", width=2)
canvas.create_text(580, 310, text="Kohde", anchor='e')

Ernesti = canvas.create_oval(45, 290, 65, 310, fill="blue", outline="black")
Kernesti = canvas.create_oval(45, kernesti_pos, 65, kernesti_pos + 20, fill="green", outline="black")

score_label = tk.Label(ikkuna, text=f"Ernesti: 0 - Kernesti: 0", font=('Helvetica', 14))
score_label.place(x=10, y=350)

start_ernesti_button = tk.Button(ikkuna, text="Ernesti heittää", command=liiku_ernesti)
start_ernesti_button.place(x=10, y=50)

start_kernesti_button = tk.Button(ikkuna, text="Kernesti heittää", command=liiku_kernesti)
start_kernesti_button.place(x=120, y=50)

random_ernesti_button = tk.Button(ikkuna, text="Ernestin satunnainen sijainti", command=sijoita_ernesti_random)
random_ernesti_button.place(x=10, y=80)

reset_button = tk.Button(ikkuna, text="Nollaa pisteet", command=nollaa_pisteet)
reset_button.place(x=10, y=110)

ikkuna.mainloop()
