#Create function called count_spaces(), make sure it passes in a string called text, pass in  a string and return the amount of spaces that contained in said string

def count_spaces(text):
    i = 0
    numspaces = 0
    while i < len(text):
        if text[i] == " ":
            numspaces += 1
        i += 1  # This must be inside the loop
    return numspaces

text = input("write your text here: ")
print("Number of spaces:", count_spaces(text))
