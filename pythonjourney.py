import sys

# Journey Challenge:
# Create your own survival story by being creative in your story telling and create ways of surviving your simulation!
# Input at least 10 key-value pairs in your new dictionary and have more than 2 tool to help you survive!
# Make sure the conditions match with the bad and good decision making behind the template!

# BONUS: Create a functions within the program to make it more efficient and clean!


# dictionary for the tools
options = {
  "headphones": "A",
  "lighter": "B",
  "flashlight": "C",
  "batteries": "D"
}

print("Welcome to the journey simulator to choose options to win and escape! \n")
print("------------------------------------------------------------------------")
print("You're currently stuck in the woods and you need to find a way out.") 
print("It is raining heavy and you need to find a way to get out of the woods.") 
print("You see a house in the distance and you. What tool will you choose to get out of the woods? \n")


values = options.values()

# Get all key-value pairs
items = options.items()

# Print each key-value pair
for key, value in items:
  print(f"{value}: {key}")


print("Choose your option")
userChoices = input("Insert the letters you want to choose with no spaces but with a comma between each letter: ")
userList = list(userChoices.split(','))

# create a variable that holds on to the correct amount of tools needed to win the game
correctItems = 2

# each condition where if the right items aren't chosen, you describe the reason why you need it
if "C" not in userList:
  print("You need batteries to start up something\n")
  sys.exit()
if "D" not in userList:
  print("You need a tool to see at night\n")
  sys.exit()

# condition where you will the right choices were there BUT there are other options that were chosen
if "C" and "D" in userList:
  print("You have chosen the right tools to get to the house! \n")
  # nested condition where you will win the game if you have the right tools 
  if len(userList) == correctItems:
    print("You have chosen the right tools to get to the house! \n")
    #print("======= YOU WON =======")
else:
  print("You have chosen the wrong tools to get out of the woods, try again! \n")

  print("------------------------------------------------------------------------")

options2 = {
  "Yell Loudly": "A",
  "Run Outside the House": "B",
  "Run Upstairs and Attack Blindly": "C",
  "Quietly Sneak Around": "D"
}

print("------------------------------------------------------------------------")    
print("You have made it to the house.") 
print("You hear footsteps in the house; the floorboards creak loudly.") 
print("You need to quickly figure out to do. What will you do? \n")

values2 = options2.values()

# Get all key-value pairs
items2 = options2.items()

# Print each key-value pair
for key, value in items2:
  print(f"{value}: {key}")


print("Choose your option")
userChoices = input("Insert the letters you want to choose with no spaces but with a comma between each letter: ")
userList2 = list(userChoices.split(','))

# each condition where if the right items aren't chosen, you describe the reason why you need it
if len(userList2) > 1:
    print("Invalid option. You cannot do two things at once.")
elif "D" in userList2:
    print("""
You slowly twist the doorknob and step inside the dark house.
Every creak in the floor sends a chill down your spine.
You crouch low, moving silently through the hallway.
A shadow moves past a doorway, but you freeze—unseen.
Breathing shallow, you find a room to hide in and wait it out...
You made the right move. 
======= YOU SURVIVED THIS ENCOUNTER =======
    """)
elif "A" in userList2:
    print("""
You burst into the hallway and yell, "IS ANYONE THERE?!"
Your voice echoes through the wooden walls.
Footsteps rush toward you from the upper floor.
Before you can react, something grabs you.
Your voice gave you away...
======= YOU DIDN'T MAKE IT =======
    """)
    sys.exit()
elif "B" in userList2:
    print("""
Panic takes over—you swing the front door open and dash outside.
The rain pours harder, drenching your clothes and blurring your vision.
You slip on the muddy ground just as you hear something behind you.
======= YOU ESCAPED... BUT AT WHAT COST? =======
    """)
    sys.exit()
elif "C" in userList2:
    print("""
You run upstairs, gripping your flashlight like a weapon.
Each step groans under your weight.
You reach the hallway, flinging doors open and swinging wildly.
Suddenly, a mirror shatters beside you—it was your own reflection.
In your panic, you’ve revealed your position...
======= AMBUSHED =======
    """)
    sys.exit()

print("------------------------------------------------------------------------")    
print("You stand still as a mouse inside the room.") 
print("You hear deep breathing right outside the door.") 
print("Your heart pounds loudly; the door handle starts to turn. What will you do? \n")

options3 = {
  "Hide Behind the Door as It Opens": "A",
  "Open the Door and Swing": "B",
  "Run Past it as the Door Opens": "C",
  "Play Dead": "D"
}

values3 = options3.values()

# Get all key-value pairs
items3 = options3.items()

# Print each key-value pair
for key, value in items3:
  print(f"{value}: {key}")

print("Choose your option")
userChoices = input("Insert the letters you want to choose with no spaces but with a comma between each letter: ")
userList3 = list(userChoices.split(','))

if len(userList3) > 1:
    print("Invalid option. You can only react one way in a split-second decision.")
elif "A" in userList3:
    print("""
You press your back flat against the wall behind the door, barely breathing.
The door creaks open, brushing past your arm—close, but not enough to be noticed.
A tall figure steps inside, scanning the room, unaware you’re inches away.
He walks deeper in. You slip out silently and close the door behind you.
You outsmarted him.
======= ESCAPE SUCCESSFUL =======
    """)
elif "B" in userList3:
    print("""
Your adrenaline spikes—you rip the door open and swing your flashlight with all your strength.
It connects, but the figure is much stronger than expected.
They grunt and grab your arm mid-swing.
A struggle ensues... you're not fast enough.
======= CAPTURED =======
    """)
    sys.exit()
elif "C" in userList3:
    print("""
As the door cracks open, you take your chance and bolt forward.
You shove the figure aside and sprint toward the hallway.
But your foot slips on the slick wooden floor.
You crash into the wall with a loud thud.

Before you can get up, the figure grabs your leg and yanks you back into the room.
======= YOU WERE CAUGHT =======
    """)
    sys.exit()
elif "D" in userList3:
    print("""
You drop to the ground, eyes wide open, forcing your body still like a corpse.
The door swings open. Heavy boots step inside.
The figure hovers above you... waiting.
They nudge your side with a foot. You don't flinch.
It stands there for hours. Then, silence.
When you open your eyes, you're alone.
Playing dead saved your life.
======= YOU SURVIVED =======
    """)