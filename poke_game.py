# -*- coding: utf-8 -*-
from libdw import sm
import random
import time

"""
initialising the pokemon 
using Object Oriented Programming (OOP)
"""

class Pokemon():
    def __init__(self, hp, A, D,speed, Type, name):
        self.hp = hp
        self.A = A
        self.D = D
        self.speed = speed
        # storing type of the pokemon in a list
        self.Type = Type.split(" ")  
        self.name = name
        
    def A1(self, name, AP, Type):
        # method for first attack
        self.A1_name = name
        self.A1 = AP
        self.A1_Type = Type 
        # Type of the move
        
    def A2(self, name, AP, Type):
        # method for second attack
        self.A2_name = name
        self.A2 = AP
        self.A2_Type = Type 
        # Type of the move
        
    def A3(self, name, AP, Type):
        # method for third attack
        self.A3_name = name
        self.A3 = AP
        self.A3_Type = Type 
        # Type of the move
        
    def A4(self, name, AP, Type):
        # method for dpurth attack
        self.A4_name = name
        self.A4 = AP
        self.A4_Type = Type 
        # Type of the move
        
mew_two = Pokemon(322, 202, 166, 238, "P", "Mew Two")
deoxys = Pokemon(210, 274, 94, 274, "P", "Deoxys")
eternatus = Pokemon(390, 157, 175, 238, "Po Dr", "Eternatus")
reshiram = Pokemon(310, 120, 184, 90, "F Dr", "Reshiram")
snorlax = Pokemon(430, 202, 121, 58, "N", "Snorlax") 


"""
initialising the moves of the pokemon 
using Object Oriented Programming (OOP)
"""

# mew_two
mew_two.A1("Future Sight", 120, "P")
mew_two.A2("Psystrike", 100, "P")
mew_two.A3("Aura Sphere", 120, "Fi")
mew_two.A4("Mega Kick", 120, "N")

# deoxys
deoxys.A1("Focus Blast", 120, "Fi")
deoxys.A2("Psycho Boost", 140, "P")
deoxys.A3("Psychic", 90, "P")
deoxys.A4("Giga Impact", 150, "N")

# eternatus
eternatus.A1("Eternabeam", 160, "Dr")
eternatus.A2("Dynamax Cannon", 100, "Dr")
eternatus.A3("Flame Thrower", 90, "F")
eternatus.A4("Solarbeam", 120, "G")

# reshiram
reshiram.A1("Blue Flare", 130, "F")
reshiram.A2("Outrage", 120, "Dr")
reshiram.A3("Giga Impact", 150, "N")
reshiram.A4("Focus Blast", 120, "Fi")

# snorlax
snorlax.A1("Giga Impact", 150, "N")
snorlax.A2("Last Resort", 140, "N")
snorlax.A3("Hydro Pump", 110, "W")
snorlax.A4("Outrage", 120, "Dr")


"""
list of all pokemons
"""

poke = [mew_two, deoxys, eternatus, reshiram, snorlax]


"""
game code
"""

# function to claculate damage by each attack
def damage(p, A, D, mod = 1):
    dam = (((42 * p * A / D ) / 50) + 2) * mod
    return(dam)
    
# dictionary of weaknesses
d= dict()
d["N"] = ["Fi"]
d["Dr"] = ["Dr"]
d["F"] = ["W"]

print("""
Pick a Pokemon

1 - Mew Two
2 - Deoxys
3 - Eternatus
4 - Reshiram
5 - Snorlax

Key in the number next to your desired pokemon and hit enter
""")

pick = int(input())
pick = poke.pop(pick - 1)
print("Ypu have picked {}\n".format(pick.name))
random.shuffle(poke)
att_list = [pick.A1, pick.A2, pick.A3, pick.A4]

#ene = poke[random.randint(0,3)]
#ene_list =  [ene.A1, ene.A2, ene.A3, ene.A4]


"""
SM Class
deciding which pokemon attacks first using state mahines
"""

class moves(sm.SM):
    if ene.speed > pick.speed:
        start_state = 1
    else:
        start_state = 0
        
    def start(self):
        self.state = self.start_state
        
    def get_next_values(self, state, inp):
        if state == 1:
            ene_att = ene_list[random.randint(0,3)]
            pick.hp -= ene_att
            if pick.hp < 0:
                return (1, "You Lose. Better Luck Next Time !!")
            ene.hp -= inp
            return (1, """Your opponent attacked {} for {} HP
and you attacked {} for {} HP\n""".format(pick.name, ene_att, ene.name, inp))
        else:
            ene.hp -= inp
            if ene.hp < 0:
                return (0, "You beat this one. Good luck with the rest !!")
            ene_att = ene_list[random.randint(0,3)]
            pick.hp -= ene_att
            return (0, """Your opponent attacked {} for {} HP
and you attacked {} for {} HP\n""".format(pick.name, ene_att, ene.name, inp))
    def step(self, inp):
        (state, output) = self.get_next_values(self.state, inp)
        self.state = state
        if output == "You beat this one. Good luck with the rest !!" or output ==  "You Lose. Better Luck Next Time !!":
            print("{} has {} HP left".format(pick.name, pick.hp))
            print("{} has {} HP left".format(ene.name, ene.hp))
            print(output)
        else:
            print(output)
            print("{} has {} HP left".format(pick.name, pick.hp))
            print("{} has {} HP left".format(ene.name, ene.hp))
            

m = moves()
m.start()



for i in range(len(poke)):
    ene = poke[i]
    print("You are up against a {}".format(ene.name))
    ene_list =  [ene.A1, ene.A2, ene.A3, ene.A4]
    
    
    
    while pick.hp > 0 and ene.hp > 0:
        
        print("""
    Which attack would you like to use ?
    
    1 - {}
    2 - {}
    3 - {}
    4 - {}
    
    Key in the number next to your desired attack and hit enter
        """.format(pick.A1_name, pick.A2_name, pick.A3_name, pick.A4_name))
        att_no = int(input())
        att = att_list[att_no - 1]
        
        print("Your opponent is deciding what move to use\n")
        time.sleep(2)
        
        m.step(att)
    
    

                
            
        
            
            
    












        
