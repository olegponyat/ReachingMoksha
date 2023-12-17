class Shudra():
    def __init__(self, name, profession):
        self.name = name
        self.profession = profession
    def __str__(self):
        return f"{self.name}, {self.profession}"
class Vaishya(Shudra):
    def __init__(self, name, profession, craft):
        super().__init__(name, profession)
        self.craft = craft
        self.privileges = "Vaishya"
    def __str__(self):
        return f"{self.name}, {self.profession}, {self.craft}"
class Kshatriya(Shudra):
    def __init__(self, name, profession, warrior_type):
        super().__init__(name, profession)
        self.warrior_type = warrior_type
    def __str__(self, ):
        return f"{self.name}, {self.profession}, {self.warrior_type}"
class Brahmin(Shudra):
    def __init__(self, name, profession, sacrificials):
        super().__init__(name, profession)
        self.sacrificials = sacrificials
    def __str__(self):
        return f"{self.name}, {self.profession}, {self.sacrificials}"
 
shudras = []
vaishyas = []
kshatriyas = []
brahmins = []
 
def create_new_shudra(name, profession):
    new_shudra = Shudra(name, profession)
    shudras.append(new_shudra)
    for shudra in shudras:
        print(shudra)
def create_new_vaishya(name, profession, craft):
    new_vaishya = Vaishya(name, profession, craft)
    vaishyas.append(new_vaishya)
    for vaishya in vaishyas:
        print(vaishya)
def create_new_ksahtriya(name, profession, warrior_type):
    new_kshatriya = Kshatriya(name, profession, warrior_type)
    kshatriyas.append(new_kshatriya)
    for kshatriya in kshatriyas:
        print(kshatriya)
def create_new_brahmin(name, profession, sacrificials):
    new_brahmin = Brahmin(name, profession, sacrificials)
    brahmins.append(new_brahmin)
    for brahmin in brahmins:
        print(brahmin)
 
import random
import time
shudra_dharma = [
    "You serve someone well. Good Job! +20 karma points.",
    "You serve someone badly. Better luck next time! -20 karma points",
    "You serve someone extremely well! Amazing job! +40 karma points",
    "You serve someone reasonably well! Continue on.... +10 points"
]
shudra_occupations = [
    "No Occupations: gain 10 less points but lose 10 less",
    "Laborer: +40 points at the start of the game",
    "Artisan: 1.5x points gained and 1.5x points lost",
]
vaishya_dharma = [
    "You serve someone well. Good Job! +20 karma points.",
    "You serve someone badly. Better luck next time! -20 karma points",
    "You serve someone extremely well! Amazing job! +40 karma points",
    "You serve someone reasonably well! Continue on.... +10 points"
]
vaishya_occupations = [
    "Traveling Merchant: ",
    "Architect: ",
    "Weapon Maker: 2x points gained and 2x points lost",
]
kshatriya_dharma = [
    "You serve someone well. Good Job! +20 karma points.",
    "You serve someone badly. Better luck next time! -20 karma points",
    "You serve someone extremely well! Amazing job! +40 karma points",
    "You serve someone reasonably well! Continue on.... +10 points"
]
kshatriya_occupations = [
    "Soldier: ",
    "Anarchist: ",
    "King: 2.5x points gained and 2.5x points lost",
]
brahmin_dharma = [
    "You serve someone well. Good Job! +20 karma points.",
    "You serve someone badly. Better luck next time! -20 karma points",
    "You serve someone extremely well! Amazing job! +40 karma points",
    "You serve someone reasonably well! Continue on.... +10 points"
]
brahmin_occupations = [
    "Traveling Merchant: ",
    "Priest: Gain an extra 10 points when y",
    "Academic Weapon: 3x points gained and 3x points lost",
]
shudra_possible_deaths = [
    "The Brahmin you are serving decides to kill you for your terrible work. The gods do not approve. -20 points",
    "You peacefully die of old age, having fulfilled your dharma. The gods are pleased with your hard work. +20 points",
    "You slip on a stray banana peel while walking to work. The gods say: L bozo 💀. No points added."
]
vaishya_possible_deaths = [
    "The wares you have sold malfunction at a crucial time -40 points",
    "You peacefully die of old age, having fulfilled your dharma. The gods are pleased with your hard work. +20 points",
    "Congratulations! You made the first edition of gunpowder. Sadly, it blows up a little too early. The gods say: wrong civilization bro 💀. No points added"
]
kshatriya_possible_deaths = [
    "The guy you were serving, a brahmin, decides to kill you for your terrible work. The gods see this as unworthy of moksha. -20 points",
    "You peacefully die of old age, having fulfilled your dharma. The gods are pleased with your hard work. +20 points",
    "You slip on a stray banana peel while walking to work. The gods say: L bozo 💀. No points added."
]
brahmin_possible_deaths = [
    "You were sacrificing a dog to Yan, but the creature escapes its ties and bumps you into the fire pit. The gods giggle as they say: -20 points.",
    "You peacefully die of old age, having fulfilled your dharma The gods are pleased with your hard work. +20 points",
    "The guy you were serving, a brahmin, decides to kill you for your terrible work. The gods see this as unworthy of moksha. No points added",
]
 
 
beginning_range = random.randrange(50,200,10)
def karma_points(x, y):
    random.shuffle(x)
    user_input = int(input("\nPick a number 0-3:"))
    print(f"\n {x[user_input]}")
    if "+20" in x[user_input]:
        y+=20
        print(f"You currently have",beginning_range,"karma points.")
        return(x,y)
    elif"+40" in x[user_input]:
        y+=40
        print(f"You currently have",beginning_range,"karma points.")
        return (x,y)
    elif "-20" in x[user_input]:
        y+=-20
        print(f"You currently have",beginning_range,"karma points.")
        return (x,y)
    elif "+10" in x[user_input]:
        y+=10
        print(f"You currently have",beginning_range,"karma points.")
        return (x,y)
def shuffle_deaths(x,y):
    random.shuffle(x)
    print(x[1])
    if "-20" in (x[1]):
        y+=-40
        return(x,y)
    elif "+20" in (x[1]):
        y+=20
        return(x,y)
    elif "No points added" in (x[1]):
        y+=0
        return(x,y)


 
print("Welcome to 'Achieving Moksha', a game about gaining karma points while going through the rebirth cycle. To win the game you must  ")


turns = 0
continue_game = "Y"
while continue_game == "Y":
    print("Rebirthing, please wait....\n")
    time.sleep(3)
    print(f"You have begun with", {beginning_range}, "karma points\n")
 
    if (beginning_range < 200):
        name = input ("You were born as a shudra. What is your name?:")
        profession = input("What is your profession?\n")


        while turns < 3:
            shudra_dharma, beginning_range = karma_points(shudra_dharma, beginning_range)
            if turns >= 3:
                break
        turns=0
        print("You have reached the end of your life: Your death is being calculated.\n")
        time.sleep(1)
        
        print("...\n")
        time.sleep(1)
       
        shudra_possible_deaths, beginning_range = shuffle_deaths(shudra_possible_deaths, beginning_range)
        print(f"You currently have",beginning_range,"karma points.")
    elif (200 <= beginning_range < 500):
        name = input ("You were born as a vaishya. What is your name?")
        profession = input("What is your profession?")
        vaishya_dharma, beginning_range = karma_points(vaishya_dharma, beginning_range)
        print(f"You currently have",beginning_range,"karma points.")
        vaishya_dharma, beginning_range = karma_points(vaishya_dharma, beginning_range)
        print(f"You currently have",beginning_range,"karma points.")
        vaishya_dharma, beginning_range = karma_points(vaishya_dharma, beginning_range)
        print(f"You currently have",beginning_range,"karma points.")
    elif (500 <= beginning_range < 700):
        name = input ("You were born as a kshatriya. What is your name?")
        profession = input("What is your profession?")
        kshatriya_dharma, beginning_range = karma_points(kshatriya_dharma, beginning_range)
        print(f"You currently have",beginning_range,"karma points.")
        kshatriya_dharma, beginning_range = karma_points(kshatriya_dharma, beginning_range)
        print(f"You currently have",beginning_range,"karma points.")
        kshatriya_dharma, beginning_range = karma_points(kshatriya_dharma, beginning_range)
        print(f"You currently have",beginning_range,"karma points.")
    elif (700 <= beginning_range < 999):
        name = input ("You were born as a Brahmin. What is your name?")
        profession = input("What is your profession?")
        brahmin_dharma, beginning_range = karma_points(brahmin_dharma, beginning_range)
        print(f"You currently have",beginning_range,"karma points.")
        brahmin_dharma, beginning_range = karma_points(vaishya_dharma, beginning_range)
        print(f"You currently have",beginning_range,"karma points.")
        brahmin_dharma, beginning_range = karma_points(vaishya_dharma, beginning_range)
        print(f"You currently have",beginning_range,"karma points.")
    elif (beginning_range >= 1000):
        print("Congratulations, you achieved moksha!")
        continue_game = input("Would you like to continue? Y or N:").upper()
        if continue_game == "Y":
            continue
        else:
            print(f"You ended the game. You ended with",{beginning_range},"points.")
            break
    else:
        print("You somehow managed to break the game. Heres a while loop with no break!")
        time.sleep(2)
        while beginning_range > 0:
            print("heheheha")
