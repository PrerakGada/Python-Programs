from colorama import Fore, Back, Style
import random

dog = {
    'image': 'ˁ˚ᴥ˚ˀ',
    'name': '',
    'age': 10,
    'weight': random.randint(30, 70) / 10,
    'healthy_weight': random.randint(10, 100) / 10,
    'bored': {1: Style.DIM + "I'm Bored", 2: Style.NORMAL + "I'm Bored", 3: Style.BRIGHT + "I'm Bored"},
    'hungry': {1: Style.DIM + "I'm Hungry", 2: Style.NORMAL + "I'm Hungry", 3: Style.BRIGHT + "I'm Hungry"},
    'sleep': {1: Style.DIM + "I'm Sleepy", 2: Style.NORMAL + "I'm Sleepy", 3: Style.BRIGHT + "I'm Sleepy"}
}

cat = {
    'image': '^ↀᴥↀ^',
    'name': '',
    'age': 10,
    'weight': random.randint(30, 70) / 10,
    'healthy_weight': random.randint(10, 100) / 10,
    'bored': {1: Style.DIM + "I'm Bored", 2: Style.NORMAL + "I'm Bored", 3: Style.BRIGHT + "I'm Bored"},
    'hungry': {1: Style.DIM + "I'm Hungry", 2: Style.NORMAL + "I'm Hungry", 3: Style.BRIGHT + "I'm Hungry"},
    'sleep': {1: Style.DIM + "I'm Sleepy", 2: Style.NORMAL + "I'm Sleepy", 3: Style.BRIGHT + "I'm Sleepy"}
}

fish = {
    'image': "><(((('>",
    'name': '',
    'age': 10,
    'weight': random.randint(30, 70) / 10,
    'healthy_weight': random.randint(10, 100) / 10,
    'bored': {1: Style.DIM + "I'm Bored", 2: Style.NORMAL + "I'm Bored", 3: Style.BRIGHT + "I'm Bored"},
    'hungry': {1: Style.DIM + "I'm Hungry", 2: Style.NORMAL + "I'm Hungry", 3: Style.BRIGHT + "I'm Hungry"},
    'sleep': {1: Style.DIM + "I'm Sleepy", 2: Style.NORMAL + "I'm Sleepy", 3: Style.BRIGHT + "I'm Sleepy"}
}


def choose_pet():
    print('1. Dog |', dog['image'], '|')
    print('2. Cat |', cat['image'], '|')
    print('3. Fish |', fish['image'], '|')
    pet = input('Which Pet do you want? ')



def pet_action():
    pass


def pet_status():
    pass


def main():
    print('----Welcome to PyPet!!----')
    choose_pet()

# Main Code
main()
