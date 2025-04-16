
import random
import os
import time
class Events:
    @staticmethod
    def the_riddler(plr):
        riddlers = {
            "The more of me you take, the more you leave behind. What am I?":"footsteps",
            "I speak without a mouth and hear without ears. I have no body, but I come alive with the wind. What am I?":"echo",
            "What has to be broken before you can use it?":"egg",
            "I’m tall when I’m young, and I’m short when I’m old. What am I?":"candle",
        }
        print("-"*10)
        print("You have met the riddler!")
        riddle, answer = random.choice(list(riddlers.items()))
        print(f"The riddle: {riddle}")
        plr_answer = input("Your answer: ")
        if answer in plr_answer.lower():
            print("Lucky!")
        else:
            damage = random.randint(5,30)
            food_lost = random.randint(3,plr.food)
            print(f"Wrong!\nYou took {damage} damage! and lost {food_lost} food!")
    @staticmethod
    def group_of_kids(plr):
        print("-"*10)
        total_kids = random.randint(2,10)
        print(f"You met {total_kids} kids wandering around, do you give them food? (2food per kid)")
        if "y" in input("Yes or no: "):
            plr.food -= total_kids*2
            print(f"You gave away {total_kids*2} food")
        else:
            print("You left them behind..")
    @staticmethod
    def surprise_attack(plr):
        print("-"*10)
        print("You got ambushed!")
        food_lost = random.randint(2,plr.food)
        health_lost = random.randint(2,plr.hp-10)
        time_lost = random.randint(2,plr.time_left-25)
        energy_lost = random.randint(2,plr.energy-5)
        print(f"You lost:\n{food_lost} food\n{health_lost} health\n{time_lost} time\n{energy_lost}\n")

class Player:
    def __init__(self,hp,food,energy):
        self.hp = hp
        self.food = food
        self.energy = energy
        self.time_left = 100
    def rest(self):
        if self.food>0:
            self.food -= 1
            self.energy += 10
            print("Well rested! you lost 1 food and gained 10 energy")
            return
        print("Not enough food!")

    def state(self):
        print(f"HP:{self.hp}\nFood:{self.food}\nEnergy:{self.energy}")

    def collect_resources(self):
        if random.random() < 0.25: # 25%
            found_food = random.randint(1,25)
            print(f"Success! You found: {found_food} Food!")
            return True
        damage = random.randint(5,30)
        self.hp -= damage
        print(f"Failed, you took {damage} damage!")
        return False
    def random_event(self,plr):
        events = [Events.the_riddler,Events.group_of_kids]
        if random.random() < 0.10: # 10%
            print("A random event occured!")
            random.choice(events)(plr)
    def move(self):
        moved_kms = random.randint(2,15)
        self.food -= moved_kms + 2
        self.energy -= moved_kms + 25
        print(f"You moved {moved_kms} kilometers and lost {moved_kms + 2} food and {moved_kms+25} energy!")
    def stay(self):
        people_attacking = random.randint(1,20)
        if random.random() < 0.30: # 30%
            print("You got caught!")
            print(f"{people_attacking} attacked you!")
            self.hp -= people_attacking*2
            self.food -= people_attacking*2
            self.energy -= people_attacking*2
            print(f"You lost {people_attacking*2} hp,food and energy!")
            return True
        print(f"{people_attacking} people walked past you and did not notice you!")
        print(f"You gained {people_attacking*5} food!")
        self.food += people_attacking*5



def test_rest():
    test_player = Player(100,100,100)
    test_player.rest()
    if(test_player.food == 99 and test_player.energy == 110):
        print("Test went through!")
        return True
    else:
        print(f"Something happened: Food:{test_player.food}, Energy: {test_player.energy}")
        return False

plr = Player(100,25,35)
options = {
    "1":plr.state,
    "2":plr.rest,
    "3":plr.collect_resources,
    "4":plr.move,
    "5":plr.stay
}
while 1:
    os.system("cls")
    if plr.time_left == 0:
        print("Time is up!")
        break
    if plr.energy <= 0:
        print("You have no energy and you collapsed!!")
        plr.time_left -= 10
        plr.hp -= 25
    if plr.hp <= 0:
        print("You died!")
        break
    print(f"Time left: {plr.time_left} hours\n")
    print("Choices:\n1 - See your current state\n2 - Rest\n3 - Find food(25% chance)\n4 - Move away\n5 - Stay here(RISKY)")
    choice = input("Your choice: ")
    if options.get(choice):
        plr.random_event(plr)
        options[choice]()
        plr.time_left -= 1
        plr.energy -= random.randint(1,5)
    else:
        print("Wrong choice!")
    time.sleep(2)