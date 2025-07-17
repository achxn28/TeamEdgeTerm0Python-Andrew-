#This is the starter file for zombie_manor.py
#Use it to develop your skills as needed

input_msg ="" #an empty string to hold our user inputs
game_is_on = True #the game loop will depend on this being true
current_room = None #to keep track of where we are
rooms = [] #append any new rooms you create to this list

#******** DEFINE CLASSES *******************
class Room:
  def __init__(self, name=None, description=None, objects=None, paths=None):
    self.name = name
    self.description = description
    self.objects = objects
    self.paths = paths
      
class Player:
  def __init__(self, name=None, items=[]):
      self.name =name
      self.items = items

#**********INSTANTIATE OBJECTS ***************
player = Player()

kitchen = Room()
kitchen.name = "Kitchen"
kitchen.description = "The kitchen is a really nice one! It has all the stuff you need to cook a healthy meal...of zombie parts! on the table there is a red pill."
kitchen.objects =["potion", "sandwich", "knife", "red pill"]
kitchen.paths=["Living Room" , "Bathroom" , "Backyard" ]

bathroom = Room() 
bathroom.name= "Bathroom"
bathroom.description ="You are in a Bathroom. Everything is a mess. There is blood on the floor. The shower is still on... "
bathroom.objects = ["towel" , "toothbrush", "toilet Paper", "soap"]
bathroom.paths =["Kitchen"]

living_room = Room()
living_room.name = "Living Room"
living_room.description = "You are in a Living Room. There is a flicking TV on the wall and a decrepit couch in the middle of the room. There is a strange smell coming from the couch."
living_room.objects = ["remote control", "couch cushion", "old newspaper"]
living_room.paths = ["Kitchen", "Backyard", "Stairs", "Foyer"]

backyard = Room()
backyard.name = "Backyard"
backyard.description = "You are in a Backyard. There is a garden shed and a creepy tree in the corner. The grass is overgrown."
backyard.objects = ["shovel", "watering can", "hand rake"]
backyard.paths = ["Kitchen", "Living Room"]

stairs = Room()
stairs.name = "Stairs"
stairs.description = "You are at the stairs. They are creaky and old. You can hear something moving upstairs."
stairs.objects = []
stairs.paths = ["Living Room", "Upstairs Hallway"]

foyer = Room()
foyer.name = "Foyer"
foyer.description = "You are in the foyer. Piles of rotton flesh are stacked up against the walls. The front door is ajar, and you can see the street outside."
foyer.objects = ["flesh"]
foyer.paths = ["Living Room"]

upstairs_hallway = Room()
upstairs_hallway.name = "Upstairs Hallway"
upstairs_hallway.description = "You are in the upstairs hallway. The walls are covered in blood and there are doors leading to various rooms."
upstairs_hallway.objects = []
upstairs_hallway.paths = ["Stairs", "Guest Bedroom", "Master Bedroom", "Master Bathroom"]

guest_bedroom = Room()
guest_bedroom.name = "Guest Bedroom"
guest_bedroom.description = "You are in the guest bedroom. The bed is unmade and there are clothes scattered everywhere."
guest_bedroom.objects = ["pillow", "blanket"]
guest_bedroom.paths = ["Upstairs Hallway"]

master_bedroom = Room()
master_bedroom.name = "Master Bedroom"
master_bedroom.description = "You are in the master bedroom. The bed is large and there is a closet full of clothes. There is a blue pill laying on the table."
master_bedroom.objects = ["blue pill", "watch", "book"]
master_bedroom.paths = ["Upstairs Hallway", "Master Bathroom"]

master_bathroom = Room()
master_bathroom.name = "Master Bathroom"
master_bathroom.description = "You are in the master bathroom. The bathtub is filled with murky water and there are towels hanging on the rack. A part of the wall looks flipsy. Do you have any brute force weapons?"
master_bathroom.objects = ["toothpaste", "shampoo", "conditioner"]
master_bathroom.paths = ["Master Bedroom"]

#add the rooms to the rooms list
rooms.append(kitchen)
rooms.append(bathroom)
rooms.append(living_room)
rooms.append(backyard)
rooms.append(stairs)
rooms.append(foyer)
rooms.append(upstairs_hallway)
rooms.append(guest_bedroom)

def prompt_user():
  reply = input("What do you want to do?  >>  ")

  return reply

def check_answer(input):
  global current_room
  global input_msg
  global rooms

  print("checking input :  " +  input)
  input_msg = input

  #GO
  if "go" in input_msg:

    #split the string into two arguments
    msg_array  = input_msg.split(" ")
    new_room = msg_array[1] #get the second element
    print(" user typed go to " + new_room)

    if new_room in current_room.paths:
      print("Yes you can go there")

      #find the room that has that "key" new_room as a property
      for room in rooms:  #Make challenge!!!!
          if room.name.lower() == new_room.lower():
            #set the current room by grabbing its index
            index = rooms.index(room)
            current_room = rooms[index]
            print("You are now at the : " + current_room.name)
      
    else:
      print("No you can't go there")
      
  #LOOK          
  elif "look" in input_msg:
      #loop through all the objects and paths and print them out so user can see options
      print("You see the following: ") 

      for object in current_room.objects:
          print(" -  " + object)

      print("From here you can go to: ")

      for path in current_room.paths:
          print(" - " + path)
  #TAKE
  elif "take" in input_msg:
      print("Taking item...")

      items_list  = input_msg.split(" ")
      item_to_take = items_list[1] #get the second element

      #check to see if it is part of the room's inventory..

      if item_to_take in current_room.objects:
          print("Yes you can take this item: " + item_to_take)
          player.items.append(item_to_take) #add to the players items list

          #remove from room
          current_room.objects.remove(item_to_take)

          print("current room items after taking item " + str(current_room.objects))
          print("player has : " + str(player.items))

      else:
          print("No you can't pick that up")

  #Name
  elif "name" in input_msg:
      print( current_room.name)

  #Help
  elif "help" in input_msg:
      print(" You can type 'look' to look around and 'go' to follow a path.")
      
  elif input_msg == None:
      print(" input: " + input_msg)
        
      input_msg = input("What do you want to do? You can type 'help' for commands to use >>> ")
      
  else:
      print(" I don't understand that")

def start():
  global current_room

  print("Welcome to Zombie Manor!!")
  name = input("What is your name, player? ")
  player.name = name
  print("Welcome, " + name)

  #begin at the kitchen
  current_room = kitchen

  print(f"You are in a: {current_room.name}. and everything looks normal. The air smells like death")

  while(game_is_on):
    check_answer(prompt_user()) #this makes the game continously prompt and check response


start()