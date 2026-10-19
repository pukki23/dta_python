import requests

city = 'London'
url = 'http://api.weatherapi.com/v1/current.json?key=21159bca8235487da73102813261210&q='+city+'&aqi=no'
response = requests.get(url)
json = response.json()
temp = json.get('current').get('temp_c')
print (temp)
forcast = json.get('current').get('condition').get('text')
print(forcast)

import random

def roll():
    dice = random.randint(1, 6)
    return dice

def main():
    player_1 = input("player 1 roll a dice ")
    player_2 = input("player 2 roll a dice ")

    if player_1 == 'roll' and player_2 == 'roll':
        player_1_value = roll()
        player_2_value = roll()

        print ("Player 1", player_1_value)
        print ("Player 2", player_2_value)

        if player_1_value > player_2_value:
            print('player 1 WINS')
        else:
            print("player 2 WINS")
    else:
        print("Type roll to start the game")

main()

class Robot_dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        print('woof woof')


def main():
    my_dog = Robot_dog('spot', 'chihuahua')
    my_dog.bark()

    print(my_dog.breed)
    print(my_dog.name)

main()

class Robot:
    def __init__(self, name):
        self.name = name
        self.position = [0,0]
        print('My name is ',  self.name)

    def walk(self, x, y):
        self.position[0] = self.position[0] + x
        self.position[1] = self.position[1] + y
        print('New position: ', self.position)

    def eat(self):
        print('I am hungry')

class Robot_Dog(Robot):

    def talk(self):
        print("woff woof")

    def eat(self):
        super().eat()
        print('I like bacon')

def main():
    my_dog = Robot_Dog('spot')
    my_dog.walk(40, 40)
    my_dog.talk()
    my_dog.eat()

main()     

#FILE MANIPULATION
def add_acronym():
    new_acronym = input('What acronym do you want to add: ')
    acronym_definition = input('Whats is the defination of the new acronym: ')
    with open ('files.txt', 'a') as file:
        file.write(new_acronym + ' - ' + acronym_definition + '\n')

    
def find_acronym():
    lookup_word = input("What do you want to look up: ")

    try: 
        found = False
        with open ('files.txt') as file:
            for line in file:
                if lookup_word in line:
                    print(line)
                    found = True
                    break
    
        if not found:
            print('acronym does not exist')

    except FileNotFoundError as e:
            print ('File not found')
            return

def main():
    operation = input('use f for find and a for add: ')
    if operation == 'a':
        add_acronym()
    elif operation == 'f':
        find_acronym()
    else:
        print ('enter f or a')

main()

# a, b = 10, 0

# try:
#     print(a / b)
# except:
#     print("Cant be divided by zero")