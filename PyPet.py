from colorama import Fore, Back, Style
import random

stat = {
  'bored': {1: Style.DIM + "I'm Bored", 2: Style.NORMAL + "I'm Okay", 3: Style.BRIGHT + "I'm Bored"},
  'hungry': {1: Style.DIM + "I'm Hungry", 2: Style.NORMAL + "I'm Okay", 3: Style.BRIGHT + "I'm not Happy"},
  'sleep': {1: Style.DIM + "I'm Sleepy", 2: Style.NORMAL + "I'm Okay", 3: Style.BRIGHT + "I'm not Sleepy"}
}

dog = {
  'image': 'ˁ˚ᴥ˚ˀ',
  'name': '',
  'age': 10,
  'weight': random.randint(30, 70) / 10,
  'healthy_weight': random.randint(10, 100) / 10,
  'bored': 2,
  'hungry': 2,
  'sleep': 2
}

cat = {
  'image': '^ↀᴥↀ^',
  'name': '',
  'age': 10,
  'weight': random.randint(30, 70) / 10,
  'healthy_weight': random.randint(10, 100) / 10,
  'bored': 2,
  'hungry': 2,
  'sleep': 2
}

fish = {
  'image': "><(((('>",
  'name': '',
  'age': 10,
  'weight': random.randint(30, 70) / 10,
  'healthy_weight': random.randint(10, 100) / 10,
  'bored': 2,
  'hungry': 2,
  'sleep': 2
}


def choose_pet():
  print('1. Dog |', dog['image'], '|')
  print('2. Cat |', cat['image'], '|')
  print('3. Fish |', fish['image'], '|')
  pet = int(input('Which Pet do you want? '))
  if pet == 1:
    pet = dog
    pet['name'] = input('Enter the name of the pet: ')
  elif pet == 2:
    pet = cat
    pet['name'] = input('Enter the name of the pet: ')
  elif pet == 3:
    pet = fish
    pet['name'] = input('Enter the name of the pet: ')
  else:
    print('Invalid Choice!')
  help()
  return pet


def play(pet):
  pet['bored'] += 1
  if pet['bored'] < 1:
    pet['bored'] = 1
    pet['sleep'] -= 1
  if pet['bored'] > 3:
    pet['bored'] = 3
  print('Woohooo, That was fun!!')


def sleep(pet):
  pet['sleep'] += 1
  if pet['sleep'] < 1:
    pet['sleep'] = 1
    pet['hungry'] -= 1
  if pet['sleep'] > 3:
    pet['sleep'] = 3
    pet['bored'] -= 1

  if pet['bored'] < 1:
    print('Your pet is bored a lot')

  if pet['hungry'] < 1:
    pet['hungry'] = 1
    pet['weight'] -= random.randint(10, 30) / 10
  if pet['hungry'] > 3:
    pet['hungry'] = 3
    pet['weight'] += random.randint(10, 30) / 10

  print('Goodnight, zzZZZ')


def feed(pet):
  pet['hungry'] += 1
  if pet['hungry'] < 1:
    pet['hungry'] = 1
    pet['weight'] -= random.randint(10, 30) / 10
  if pet['hungry'] > 3:
    pet['hungry'] = 3
    pet['weight'] += random.randint(10, 30) / 10

  print('Yummy!!')


def help():
  print()
  print('pet\t\t\t\tDisplay the Status of your Pet')
  print('pet feed\t\tFeed your pet')
  print('pet play\t\tPlay with your pet')
  print('pet sleep\t\tLet your pet sleep')
  print('pet help\t\tDisplay the commands')
  print('pet sell\t\tExit the game')
  print()


def pet_status(pet):
  print(pet['image'])
  print('name:\t', pet['name'])
  print('age:\t', pet['age'])
  print('weight:\t', pet['weight'])
  print('hunger:\t', stat['hungry'][pet['hungry']])
  print('bored:\t', stat['bored'][pet['bored']])
  print('sleepy:\t', stat['sleep'][pet['sleep']])


def main():
  print('----Welcome to PyPet!!----')
  pet = choose_pet()
  while True:
    print()
    cmd = input('>>')
    if cmd[:3] == 'pet':
      if cmd[4:] == 'feed':
        feed(pet)
      elif cmd[4:] == 'play':
        play(pet)
      elif cmd[4:] == 'sleep':
        sleep(pet)
      elif cmd[4:] == 'help':
        help()
      elif cmd[4:] == 'sell':
        break
      elif cmd[:3] == 'pet':
        pet_status(pet)
    else:
      if cmd == 'exit':
        break

    # if pet['weight'] > pet['healthy_weight']:
    #   print('Your pet died due to excessive weight')
    #   break

    # if pet['weight'] < (pet['healthy_weight'])/5:
    #   print('Your pet died due to hunger')
    #   break

# Main Code
main()
