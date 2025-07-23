#********************************************************************
 #                                                                 
 #  Team Edge List Mini-project: THE SHOPPING LIST HELPER
 # 
 #  This project prompts users using input() to prompt users
 #  to add (or remove) items from a shopping list. It starts empty
 #  and each time the program is run it asks you to either add or 
 #  remove an item from the list. It also updates the user of its
 #  contents. The shopping list also checks to see if an item 
 #  is already present in the list and prevents you from adding it
 #  again, giving feedback along the way. 
 # 
 # ***************************************************************/

active = True

print("Welcome to Shopping List!")

welcome_message = "Hi! I'm your shopping assistant. Let me take your order. \n You can type 'add milk' to add milk to your shopping list. \n or you can type 'remove milk' to remove it. \n"

print(welcome_message)


#-->Todo: declare a shopping_list list

shopping_list = []

def prompt_user():

    reply = input("What do you want to add or remove?  >>  ")

    return reply

def check_answer(ans):
    words = ans.lower().split()


    command = words[0]
    item = " ".join(words[1:])

    if "add" != command and "remove" != command:
        print("Please enter a valid command like 'add milk' or 'remove eggs'.")
        return

    if command == "add":
        add_item(item)
    elif command == "remove":
        remove_item(item)
    else:
        print("Unknown command. Please use 'add' or 'remove' followed by the item name.")
        return



def add_item(item):
#this function can take in a string and store it in an array
    shopping_list.append(item)
    print(f"'{item}' has been added to your shopping list.")
    print("Current list:", shopping_list)



def remove_item(item):
#this function can take in a string and remove it from an array
    if item in shopping_list:
        shopping_list.remove(item)
        print(f"'{item}' has been removed from your shopping list.")
        print("Current list:", shopping_list)
    else:
        print(f"'{item}' is not in your shopping list.")


while active:

    check_answer(prompt_user()) #this makes the program continously prompt and check response while the boolean 'active' returns True
