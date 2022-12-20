print('''
   __________________
    .-'  \ _.-''-._ /  '-.
  .-/\   .'.      .'.   /\-.
 _'/  \.'   '.  .'   './  \'_
:======:======::======:======:  
 '. '.  \     ''     /  .' .'
   '. .  \   :  :   /  . .'
     '.'  \  '  '  /  '.'
       ':  \:    :/  :'
         '. \    / .'
           '.\  /.'    
             '\/'
''')

print("Welcome to the treasure island")
print("Your mission is to find the treasure")

while True:
  try:
    answer_1 = input("left or wright? ")

    if answer_1 != "left":
      print("Fail into a hole. Game over")
      break
    
    answer_2 = input("Swim or wait? ")

    if answer_2 != "wait":
      print("Attacked by trout. Game Over.")
      break

    answer_3 = input("Which door? blue, red, yellow or another color ")

    if answer_3 == "red":
      print("Burned by fire. Game over.")
      break
    elif answer_3 == "blue":
      print("Eaten by beasts. Game Over.")
      break
    elif answer_3 == "yellow":
      print("You Win!")
      break

    print("Game Over.")
    break
  
  except:
    print("Please enter valid inputs")

