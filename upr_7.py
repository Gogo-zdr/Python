import random

daljina_pole = 51
poziciya_1 = 0
poziciya_2 = 0
poziciya_3 = 0
poziciya_4 = 0

while True:
    zar = random.randint(1, 6)           
    if poziciya_1 + zar <= daljina_pole:
        poziciya_1 = poziciya_1 + zar

    zar = random.randint(1, 6)            
    if poziciya_2 + zar <= daljina_pole:
        poziciya_2 = poziciya_2 + zar

    zar = random.randint(1, 6)            
    if poziciya_3 + zar <= daljina_pole:
        poziciya_3 = poziciya_3 + zar

    zar = random.randint(1, 6)            
    if poziciya_4 + zar <= daljina_pole:
        poziciya_4 = poziciya_4 + zar


    for tekushta_poziciya in range(1, daljina_pole+1):
        simvol_za_izvejdane = "_"

        if tekushta_poziciya == poziciya_1:
            simvol_za_izvejdane = "i"
        if tekushta_poziciya == poziciya_2:
            simvol_za_izvejdane = "I"
        if tekushta_poziciya== poziciya_3:
            simvol_za_izvejdane = "T"
        if tekushta_poziciya == poziciya_4:
            simvol_za_izvejdane = "V"

        print(simvol_za_izvejdane),
    

    print(zar)


    if poziciya_1 >= daljina_pole:
        break
    if poziciya_2 >= daljina_pole:
        break
    if poziciya_3 >= daljina_pole:
        break
    if poziciya_4 >= daljina_pole:
        break

for tekushta_poziciya in range(1, daljina_pole+1):
        simvol_za_izvejdane = "_"

        if tekushta_poziciya == poziciya_1:
            simvol_za_izvejdane = "i"
        if tekushta_poziciya == poziciya_2:
            simvol_za_izvejdane = "I"
        if tekushta_poziciya== poziciya_3:
            simvol_za_izvejdane = "T"
        if tekushta_poziciya == poziciya_4:
            simvol_za_izvejdane = "V"

print(simvol_za_izvejdane),
        


