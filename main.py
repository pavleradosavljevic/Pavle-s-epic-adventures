print("Welcome to me game")
name = input("Whats your name ? ")
print("Welcome " + name)
age = int(input("How old are you ? "))
if age >= 18:
  print("Great you can play this game!")
  start = input("Shall we get started ? yes/no ")
  if start == "yes" or "Yes":
    print("Epic ")
    health = 10
    forest = input("In front of you is a forest do you want do go acros it or around ? 1/2 ")
    if forest == "1":
      health = health - 5
      print("you got attacked by a bear and you lost 5 health points")
      print(health)
      lake = input("Now in frony of you is a lake will you swim across or will you go around it? 1/2 ")
      if lake == "1":
        print("You drowned, bad luck")
      if lake == "2":
        print("You kept moving forward like the brave solder that you are !!!")
        food = input("You have found some food it will help you heal from the bear attack will you take some ? yes/no ")
        if food == "yes":
          print("you have died of food poisoning")
        if food == "no":
          print("ÿou kept moving forward")
          house = input("You have found a house with an old man and his daughter they asked if you need help will you take it ? yes/no ")
          if house == "yes":
            print("They helped you alot and you heald back up")
            health = health + 5
            print ("Your health is now " + "health")
            print("You ended up marying the daugter and you ended up living with a bunch of kids and you lived happily ever after. The end!!!")
          if house == "no":
            print("you have died from starvatio.")
    else:
      print("you died from dehydration, sorry")
else:
  print("What are you doing here go home kid !")