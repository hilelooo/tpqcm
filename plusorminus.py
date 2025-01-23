import random


def game(max=100, lives = 10):
  number = random.randint(1,max)
  while lives > 0:
    guess = int(input("Choix"))
    if guess > number:
      print("Moins")
    elif guess < number:
      print("Plus")
    elif guess == number:
      print("ouais c'est ca")
      break
  if lives == 0:
    print("t nul")

max = input("Nombre max (défaut : 100)")
max = None if max == '' else int(max)
lives = input("Nombre de vies (défaut : 10)")
lives = None if lives == '' else int(lives)

game(max,lives)
