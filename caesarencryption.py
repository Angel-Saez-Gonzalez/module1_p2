alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


#Encryption with string
shift = 3

phrase = input("Write a phrase: ")

phrase = phrase.upper()

code = ""

for i in phrase:
    if i.isspace():
        code += " "
        continue
    code += alphabet[(alphabet.index(i)+shift)%len(alphabet)]
        

print(code)

#Encryption with ascii
#pasar la letra codigo ascii y comprobarla en el numero
alp = (66:91)
