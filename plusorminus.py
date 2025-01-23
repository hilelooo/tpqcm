import random


def game(max, lives = 10):
  number = random.randint(1,max)
  while lives > 0:
    guess = int(input("Choix"))
    if guess > number:
      print("Moins")
    else if guess < number:
      print("Plus")
    else if guess == number:
      print("ouais c'est ca")
      break
  if lives == 0:
    print("t nul")

max = int(input("Nombre max"))
