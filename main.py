from ast import Compare
import random
def gameWin(comp, you):
      if comp == you:
            return None
      #condition 1
      elif comp == 's':
            if you == 'w':
                  return False
            elif you == 'g':
                  return True
      #condition 2
      elif comp == 'w':
            if you == 's':
                  return True
            elif you == 'g':
                  return False
      #condition 3
      elif comp == 'g':
            if you == 's':
                  return False
            elif you == 'w':
                  return True
print("Comp turn: Snake(s) Water(w) Gun(g)?")
randnumber =random.randint(1,3)
if randnumber == 1:
      comp = 's'
elif randnumber == 2:
      comp = 'w'
elif randnumber == 3:
      comp = 'g'

you = input("Your turn: Snake(s) Water(w) Gun(g)?")
a = gameWin(comp, you)
print(f"Computer chose {comp}")
print(f"You chose {you}")

if a == None:
      print("THE GAME ID TIE!")
elif a:
      print("HURRAY, YOU WIN!")
else:
      print("OH NO, YOU LOSE!")


