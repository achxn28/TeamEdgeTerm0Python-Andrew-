#Create function called count_spaces(), make sure it passes in a string called text, pass in  a string and return the amount of spaces that contained in said string

text = str(input("write your text here: "))
def count_spaces(text):
    i = 0
    numspaces = 0
    while i < len(text):
        if text[i] == " ":
            numspaces += 1


count_spaces(text)