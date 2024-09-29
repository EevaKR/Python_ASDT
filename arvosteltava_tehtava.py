import tkinter as tk
import random
import threading
import winsound
import time
import numpy as np

#tehään ikkuna
ikkuna=tk.Tk()
ikkuna.title("Pako autiolta saarelta")
ikkuna.geometry("1000x550+100+200") #koko, etäisyys reunasta
title = tk.Label(ikkuna, text="Autio saari")
title.place(x=10, y=10)
#tehään canvas jotta voidaan visualisoida saari ja mantere
canvas = tk.Canvas(ikkuna, width=600, height=400, bg="white")
canvas.pack()


hatasanoma = {
    "sana1": "Ernesti",
    "sana2": "ja",
    "sana3": "Kernesti",
    "sana4": "tässä",
    "sana5": "terve",
    "sana6": "Olemme",
    "sana7": "autiolla",
    "sana8": "saarella",
    "sana9": "voisiko",
    "sana10": "joku",
    "sana11": "tulla",
    "sana12": "sieltä",
    "sana13": "sivistyneestä",
    "sana14": "maailmasta",
    "sana15": "hakemaan",
    "sana16": "meidät",
    "sana17": "pois",
    "sana18": "Kiitos"
}


# Ernesti = canvas.create_rectangle(45, 290, 65, 310, fill="blue", outline="black")
# Kernesti = canvas.create_rectangle(45, 50, 65, 70, fill="violet", outline="black")

#canvas.create_line(50, 300, 550, 300, fill="black", width=2)
canvas.create_line(550, 50, 550, 300, fill="yellow", width=5) #oikea laita
canvas.create_line(50, 50, 50, 300, fill="green", width=5) #vasen laita
# havainnollistetaan vasempaan reunaan autio saari ja toiseen reunaan asuttu mantere
canvas.create_text(580, 310, text="Sivistys", anchor='e')
canvas.create_text(80, 310, text="Autio saari", anchor='e')

tiedot = {} 
tiedot['Kernestin_apinamaara'] = 0
tiedot["apinamaara"] = 0
tiedot['apina']={} #keyword = apina
tiedot['aika_askel']=100 #200 ms


#luodaan toiminto, jolla Ernesti pystyy lähettämään apinan uimaan saaren pohjoispäästä 

def luo_ja_laheta_apina():
    global tiedot
    print("Luodaan apina...")
    tiedot["apinamaara"] +=1 #lisätään apinamäärää yhdellä
    apina_id=tiedot["apinamaara"]
    
    tiedot['apina'][apina_id]={
        'nimi': 'Ernestin apina', 
        'x':10, 
        'y':60+np.random.randint(-20,20),
        'sanalista' : []
        }
    random_word = random.choice(list(hatasanoma.values())) 
    tiedot['apina'][apina_id]['sanalista'].append(random_word)
    #lisätään jokaiselle apinalle yksilöllinen nimi
    # havainnollista tämän uinti käyttöliittymässä parhaaksi katsomallasi tavalla
    tiedot['apina'][apina_id]['yksilollinen_nimi']=''.join(['E',str(apina_id), random_word]) #komento joka yhdistää nämä yhdeksi stringiksi
    
    
    apinakahva=tk.Label(text=tiedot['apina'][apina_id]['yksilollinen_nimi'])
    apinakahva.place(x=tiedot['apina'][apina_id]['x'], y=tiedot['apina'][apina_id]['y'])

    tiedot['apina'][apina_id]['label']= apinakahva
    print(tiedot)
    
    winsound.Beep(1000,500)
    time.sleep(0.5)#soitetaan ääni, odotellaan soinnin ajan


    print("Lähetetään se uimaan...")
    # sadan pienen askelen verran (yksi ”askel” kuvaa aina jokaista uitua kilometriä)
    for i in range(100): #muuta sadaksi
        tiedot['apina'][apina_id]['x']+=35
        tiedot['apina'][apina_id]['y']+=np.random.randint(-10,10)

        if np.random.random()>0.98:       #odennäköisyys tulla syödyksi
            tiedot['apina'][apina_id]['label'].configure(fg='red')

        apinakahva.place(x=tiedot['apina'][apina_id]['x'], y=tiedot['apina'][apina_id]['y'])
        ikkuna.update()
        #.draw toinen vastaava komento
        winsound.Beep(2000+apina_id*10,tiedot['aika_askel'])
        time.sleep(tiedot['aika_askel']/1000)

 
#luodaan toiminto, jolla Kernesti pystyy lähettämään apinan mutta saaren eteläpäästä!!!!
def Kernesti_luo_ja_laheta_apina():
    global tiedot
    print("Luodaan apina...")
    tiedot["Kernestin_apinamaara"] +=1 #lisätään apinamäärää yhdellä
    apina_id=tiedot["Kernestin_apinamaara"]
    #luodaan toiminto, joka määrittelee apinan, jolle on opetettu yksi sana Ernestin ja Kernestin luomasta hätäviestistä
    tiedot['apina'][apina_id]={
        'nimi': 'Kernestin apina', 
        'x':10, 
        'y':300+np.random.randint(-20,20),
        'sanalista' : []
        }
    random_word = random.choice(list(hatasanoma.values())) 
    tiedot['apina'][apina_id]['lempiväri']='oranssi'
    #lisätään jokaiselle apinalle yksilöllinen nimi
    tiedot['apina'][apina_id]['yksilollinen_nimi']=''.join(['K',str(apina_id), random_word]) #komento joka yhdistää nämä yhdeksi stringiksi
 
    apinakahva=tk.Label(text=tiedot['apina'][apina_id]['yksilollinen_nimi'])
    apinakahva.place(x=tiedot['apina'][apina_id]['x'], y=tiedot['apina'][apina_id]['y'])

    tiedot['apina'][apina_id]['label']= apinakahva
    print(tiedot)
    
    #time.sleep(0.5)
    winsound.Beep(1000,500)
    time.sleep(0.5)#soitetaan ääni, odotellaan soinnin ajan


    print("Lähetetään se uimaan...")
    for i in range(100): 
        tiedot['apina'][apina_id]['x']+=35
        tiedot['apina'][apina_id]['y']+=np.random.randint(-10,10)
        #luo apinan uintimatkaan toiminto, jossa joka ilmentää sitä, että jokaisella kuljetulla kilometrillä 
        # apinalla on noin prosentin todennäköisyys tulla syödyksi. 
        # Säädä tätä "syödyksi tulemisen riskiprosenttia" siten, että noin puolet lähetetyistä apinoista 
        # pääsee perille. Mikäli hai syö apinan, luo uintimatkaan tätä ilmentävä ääniefekti
        syontitodennakoisyys = 0.01
        if np.random.random()>syontitodennakoisyys:       #todennäköisyys tulla syödyksi
            tiedot['apina'][apina_id]['label'].configure(fg='red')
            winsound.Beep(400,200)

        apinakahva.place(x=tiedot['apina'][apina_id]['x'], y=tiedot['apina'][apina_id]['y'])
        ikkuna.update()
        winsound.Beep(2000+apina_id*10,tiedot['aika_askel'])
        time.sleep(tiedot['aika_askel']/1000)

#luodaan toiminta threading, jolla Ernesti voi lähettää yksittäisen apinan mukanaan yksi sana kohti manteretta. 
#mikäli apina pääsee perille, ilmaise tämä sopivalla äänimerkillä.
def luo_ja_laheta_apina_saikeistin():
    kahva=threading.Thread(target=luo_ja_laheta_apina)
    kahva.start()


#luodaan vastaava toiminto Kernestille apinan lähettämistä varten
def Kernesti_luo_ja_laheta_apina_saikeistin():
    kahva=threading.Thread(target=Kernesti_luo_ja_laheta_apina)
    kahva.start()

# #tehdään tarkkailija
# def tarkkaile():
#     global tiedot
#     for i in range(100):  
#         for api in range(tiedot['apinamaara']): #VOI KÄYDÄ DICTIONARYN LÄPI TÄLLÄ TAVALLA
#             print(api)
#             tiedot['apina'][api]['y']
#             y_koordinantti_juuri_talla_apinalla=tiedot['apina'][api+1]['y']
#             print("Hätäviesti vastaanotettu")
#         if tiedot['apinamaara']>20:
#             winsound.Beep(4000,1000)
#             print("Pelastuslautta lähetetty") 

#         winsound.Beep(262,200)  
#         time.sleep(1)

def tarkkaile():
    global tiedot
    for i in range(100):  # voi olla myös while loop
        hätäviesti_sanat = set()  # Joukko (set), johon kerätään kaikki hätäviestissä olevat sanat
        for api in range(1, tiedot['apinamaara'] + 1):  # Käydään kaikki apinat läpi
            #apinan_tiedot = tiedot['apina'][api+1]  # Otetaan tietyn apinan tiedot
            #print(f"Tarkastetaan apina {apinan_tiedot['yksilollinen_nimi']} korkeudella: {apinan_tiedot['y']}")
            sanalista = tiedot['apina'][api]['sanalista']
            print(f"Apina {api} kuljettaa sanoja: {', '.join(sanalista)}")

        if len(sanalista)> 10:
            winsound.Beep(4000, 1000)
            print("Pelastuslautta lähetetty!")
        
        # Viestin seuraava tarkistus sekunnin kuluttua
        winsound.Beep(262, 200)
        time.sleep(1)


#tehdään Kernestin tarkkailija

def tarkkaile_Kernestia():
    global tiedot
    for i in range(100):  
         hätäviesti_sanat = set() 
         for api in range(1, tiedot['Kernestin_apinamaara'] + 1):  # Käydään kaikki apinat läpi
            #apinan_tiedot = tiedot['apina'][api+1]  # Otetaan tietyn apinan tiedot
            #print(f"Tarkastetaan apina {apinan_tiedot['yksilollinen_nimi']} korkeudella: {apinan_tiedot['y']}")
            sanalista = tiedot['apina'][api]['sanalista']
            print(f"Apina {api} kuljettaa sanoja: {', '.join(sanalista)}")
            
            if len(sanalista)> 10:
                winsound.Beep(4000,1000)
            print("Pelastuslautta lähetetty!") 

            winsound.Beep(262,200)  
            time.sleep(1)


def tarkkaile_Kernestia_saikeistin():
    kahva=threading.Thread(target=tarkkaile_Kernestia)
    kahva.start()

#tehdään tarkkailija_säie
def tarkkaile_saikeistin():
    kahva=threading.Thread(target=tarkkaile)
    kahva.start()

#Määritellään Ernesti lähettämään 10 apinaa saarelta mantereelle, samoin määritellään Kernesti tekemään sama. 
#Tarkkaile ja varmista visuaalisesti, pääseekö lähetetyistä apinoista noin puolet perille.

def laheta_10_apinaa():
    for _ in range(10):
        kahva = threading.Thread(target=luo_ja_laheta_apina_saikeistin)
        kahva.start()


def Kernesti_laheta_10_apinaa():
    for _ in range(10):
        kahva = threading.Thread(target=Kernesti_luo_ja_laheta_apina_saikeistin)
        kahva.start()



ernestin_10_painike=tk.Button(text="Ernesti, lähetä 10 apinaa", command= laheta_10_apinaa)
ernestin_10_painike.place(x=14, y=600) 

Kernestin_10_painike=tk.Button(text="Kernesti, lähetä 10 apinaa", command= Kernesti_laheta_10_apinaa)
Kernestin_10_painike.place(x=800, y=550) 

#luodaan ernestin säikeistyspainike
ernestin_painike=tk.Button(text="Ernesti, lähetä säik.apina", command= luo_ja_laheta_apina_saikeistin)
ernestin_painike.place(x=250, y=500)

#luodaan kernestin painike
Kernestin_painike=tk.Button(text="Kernesti, lähetä säik.apina", command= Kernesti_luo_ja_laheta_apina_saikeistin)
Kernestin_painike.place(x=250, y=450)

tarkkailija_painike=tk.Button(text="Tarkkaile Ernestin apinoita", command= tarkkaile_saikeistin)
tarkkailija_painike.place(x=14, y=500)

tarkkailija_Kernesti_painike=tk.Button(text="Tarkkaile Kernestin apinoita", command= tarkkaile_Kernestia_saikeistin)
tarkkailija_Kernesti_painike.place(x=500, y=450)

#KOHTA YKSI
Kernestin_painike=tk.Button(text="Kernesti, lähetä 1 apina", command= Kernesti_luo_ja_laheta_apina)
Kernestin_painike.place(x=500, y=500) #lähettää nyt ernestin apinan

ernestin_painike1=tk.Button(text="Ernesti, lähetä 1 apina", command= luo_ja_laheta_apina)
ernestin_painike1.place(x=800, y=500) #lähttää nyt ernestin apinan #KOHTA YKSI!!! SÄILYTÄ TÄMÄ

ikkuna.mainloop()