from tkinter import *
from PIL import ImageTk,Image
import random
root=Tk()
root.title("pokemon card game")
root.geometry("600x400")
root.configure(background="orange")

img=ImageTk.PhotoImage(Image.open("button.jpg"))

pikachu=ImageTk.PhotoImage(Image.open("pikachu.png"))
charmander=ImageTk.PhotoImage(Image.open("charmander.png"))
charizard=ImageTk.PhotoImage(Image.open("charizard.png"))
abra=ImageTk.PhotoImage(Image.open("abra.png"))
kadabra=ImageTk.PhotoImage(Image.open("Kadabra.png"))
meowth=ImageTk.PhotoImage(Image.open("meowth.jpg"))
squirtle=ImageTk.PhotoImage(Image.open("squirtle.png"))
persian=ImageTk.PhotoImage(Image.open("persian.png"))
jigglypuff=ImageTk.PhotoImage(Image.open("jigglypuff.jpg"))
nidoking=ImageTk.PhotoImage(Image.open("nidoking.png"))
ivysaur=ImageTk.PhotoImage(Image.open("ivysaur.png"))
bulbasaur=ImageTk.PhotoImage(Image.open("bulbasaur.png"))
label_player1=Label(root,text="player1",bg="red",fg="white")
label_player2=Label(root,text="player2",bg="green",fg="black")
label_player1.place(relx=0.1,rely=0.3,anchor=CENTER)
label_player2.place(relx=0.9,rely=0.3,anchor=CENTER)
label_score1=Label(root,bg="royal blue",fg="white")
label_score2=Label(root,bg="royal blue",fg="white")
label_score1.place(relx=0.1,rely=0.4,anchor=CENTER)
label_score2.place(relx=0.9,rely=0.4,anchor=CENTER)

pokemon_list=[pikachu,charmander,charizard,abra,kadabra,meowth,squirtle,persian,jigglypuff,nidoking,ivysaur,bulbasaur]

power_list=[200,60,100,50,50,40,70,60,70,30,70]

player1_score=0

def player_1():
    global player1_score
    random_pokemon_no=random.randint(0,11)
    random_pokemon=pokemon_list[random_pokemon_no]
    label_rand_pokemon_image["image"]=random_pokemon
    
    random_power=power_list[random_pokemon_no]
    
    player1_score=player1_score=random_power
    label_score1["text"]=str(player1_score)
    

player_1_button=Button(root,image=img,command=player_1)
player_1_button.place(relx=0.1,rely=0.5,anchor=CENTER)

player2_score=0

def player_2():
    global player2_score
    random_pokemon_no2=random.randint(0,11)
    random_pokemon2=pokemon_list[random_pokemon_no2]
    label_rand_pokemon_image["image"]=random_pokemon2
    
    random_power2=power_list[random_pokwmon_no2]
    
    player2_score=player2_score=random_power2
    label_score2["text"]=str(player2_score)
    

player_2_button=Button(root,image=img,command=player_2)
player_2_button.place(relx=0.9,rely=0.5,anchor=CENTER)

label_rand_pokemon_image=Label(root)
label_rand_pokemon_image.place(relx=0.5,rely=0.5,anchor=CENTER)
root.mainloop()