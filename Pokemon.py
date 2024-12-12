import csv

class Pokemon(object):
    def __init__(self, number, name, type_1, type_2, total, hp, attack, defense, sp_atk, sp_def, speed, gen, leg):
        self.number = number
        self.name = name
        self.type_1 = type_1
        self.type_2 = type_2
        self.total = total
        self.hp = hp
        self.attack = attack
        self.defense = defense
        self.sp_atk = sp_atk
        self.sp_def = sp_def
        self.speed = speed
        self.gen = gen
        self.leg = leg

    def __str__(self):
        return str(self.number) + "," + str(self.name) + "," +  str(self.type_1) + "," + \
               str(self.type_2) + "," + str(self.total) + "," + str(self.hp) + "," + str(self.attack) + \
               "," + str(self.defense) + "," + str(self.sp_atk) + "," + str(self.sp_def) + "," + \
               str(self.speed) + "," + str(self.gen) + "," + str(self.leg)

    def __lt__(self, other):
        if self.gen < other.gen:
            return "This Pokemon is not a part of the latest generation"
        else:
            return "This Pokemon is a part of the latest generation"

    def finish(self):
        return "Congratulations, {} have been added to the pokedox".format(self.name)

    def type_of(self):
        if self.type_2 != "":
            return "This Pokemon is a {}-type, and a {}-type".format(self.type_1, self.type_2)
        else:
            return "This Pokemon is a {}-type".format(self.type_1)

def main():
    item = open_file()
    choice = num_con("\nWhat kind of action do you want to do:\n1:Search for pokemon\n2:Add pokemon\n3:Exit program\nVal: ", 3)
    if choice == 1:
        search_poke(item)
    elif choice == 2:
        add_poke()
        
def search_poke(package):
    choice = num_con("\nWhat kind of action do you want to do:\n1:Search by name\n2:Search by type\nVal: ", 3)
    print("")
    if choice == 1:
        name_list = list()
        name = input("Name: ").upper()
        for x in range(len(package)):
            if name == package[x][1].upper():
                name_list.append(package[x])
            else:
                pass
        if len(name_list) < 1 :
            print("There were no pokemon by the name of: " + name)
            main()
        else:
            print("Result")
            for y in range(len(name_list)):
                print(name_list[y])
            print("Sending you to main menu")
            main()
    elif choice == 2:
        type_list = list()
        type_pok = input("Type: ").upper()
        for x in range(len(package)):
            if type_pok == package[x][2].upper() or type_pok == package[x][3].upper():
                type_list.append(package[x])
            else:
                pass
        if len(type_list) < 1 :
            print("There were no pokemon by the type of: " + type_pok)
            main()
        else:
            print("Result")
            for y in range(len(type_list)):
                print(type_list[y])
            print("Sending you to main menu")
            main()

def open_file():
    poke_list = list()
    while True:
        try:
            with open("pokemon.csv",'r', encoding = "utf8") as csv_file:
                intro_rad = csv_file.readline()
                for x in csv_file:
                    rensad = x.strip()
                    splited = rensad.split(",")
                    number = int(splited[0])
                    name = splited[1]
                    type_1 = splited[2]
                    type_2 = splited[3]
                    total = int(splited[4])
                    hp = int(splited[5])
                    attack = int(splited[6])
                    defense = int(splited[7])
                    sp_atk = int(splited[8])
                    sp_def = int(splited[9])
                    speed = int(splited[10])
                    gen = int(splited[11])
                    leg = splited[12]
                    poke_tuple = (number, name, type_1, type_2, total, hp, attack, defense, sp_atk, sp_def, speed, gen, leg)
                    poke_list.append(list(poke_tuple))
            return poke_list
        except IOError:
            print("Something went wrong, couldn't find the file you're seeking")
            break
        break

def num_con(sentence, limit):
    while True:
        try:
            number = int(input(sentence))
            while number < 1 or number > limit :
                number = int(input("Please type in only positive numbers: "))
            return number
        except(IndexError, ValueError):
            print("Type in only numbers, try again\n")        
            
def add_poke():
    inf = pow(10, 10)
    name = input("\nName of your pokemon: ")
    type_1 = input("What kind of pokemon is it: ")
    choice = input("Would you like to make it a duel-type pokemon (Y)/(N): ")
    while choice.upper() != 'N' and choice.upper() != 'Y':
        choice = input("Please choose either (Y)/(N): ")
    if choice.upper() == "Y":
        type_2 = input("What kind of pokemon is it: ")
    elif choice.upper() == "N":
        type_2 = ""
    total = num_con("How many of this pokemon exist: ", inf)
    hp = num_con("What HP does the pokemon have: ", inf)
    attack = num_con("What attack strength does the pokemon have: ", inf)
    defense = num_con("What defense strength does the pokemon have: ", inf)
    sp_atk = num_con("What Sp.Atk does the pokemon have: ", inf)
    sp_def = num_con("What Sp.Def does the pokemon have: ", inf)
    speed = num_con("What's the speed of pokemon: ", inf)
    gen = num_con("What generation is your pokemon: ", 8)
    choice_2 = input("Is your pokemon a Legendery (Y)/(N): ")
    while choice_2.upper() != "N" and choice_2.upper() != "Y":
        choice_2 = input("Please choose either (Y)/(N): ")
    if choice_2.upper() == "Y":
        leg = "True"
    elif choice_2.upper() == "N":
        leg = "False"    
    with open("pokemon.csv",'r', encoding = "utf8") as csv_file :
        csv_file.readline()
        for x in csv_file:
            splited = x.strip().split(",")
            number = int(splited[0])
        number += 1
        Poke = Pokemon(number,name,type_1,type_2,total,hp,attack,defense,sp_atk,sp_def,speed,gen,leg)
        print(Poke)
        confirm = input("Are you sure you want to add this pokemon or restart (Y)/(R): ")
        while confirm.upper() != 'R' and confirm.upper() != 'Y':
            confirm = input("Please choose either (Y)/(R): ")
        if confirm.upper() == "Y":
            row = [number,name,type_1,type_2,total,hp,attack,defense,sp_atk,sp_def,speed,gen,leg]
            with open("pokemon.csv",'a', newline = '', encoding = "utf8") as csv_file:
                new_line = csv.writer(csv_file)
                new_line.writerow(row)
            print(Poke.finish())
            print(Poke.type_of())
            x = "na"
            gen_check = Pokemon(x, x, x, x, x, x, x, x, x, x, x, int(8), x)
            print(Poke < gen_check)
            print("")
            main()
        elif confirm.upper() == "R":
            add_poke()
main()











