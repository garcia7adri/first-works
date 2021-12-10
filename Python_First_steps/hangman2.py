import random
from words import words
from parts_ahorcado import parts
import os

print ("""

¡Vamos a jugar ahorcado! \n """)


picked=random.choice(words)
picked=picked.upper()
right=["_"]*len(picked)
wrong=[]
print("La palabra elegida tiene ", len(picked), " letras.\n")
for i in range(len(picked)):
    print("_", " ",end="")

def add():
    for i in right:
        print(i, ' ', end = "")
    print()   

def wrong_letter():
    print("Letras equivocadas:", end = "")
    for i in wrong:
        print(i,' ',end = "")
    print()

def play():
    
    while True:   
        letter=input("\n Por favor, ingresa una letra: ").upper()
        if letter in wrong:
                print("Ya habías digitado ", letter, ".")
                continue
        elif letter in picked: 
            index = 0
            for i in picked:
                if i == letter:
                    right[index] = letter
                index = index + 1

            add()
            parts(len(wrong))
            wrong_letter()
            
        else:

            if letter not in picked: 
                print(letter, "no está en la palabra.\n")
                wrong.append(letter)
            wrong_letter()
            add()
            parts(len(wrong))
            wrong_letter()

            
        if len(wrong) > 6:
            os.system("cls")
            parts(len(wrong))
            print("\n Game Over!")
            print("\n La palabra era", picked,".")
            break

        if '_' not in right:
            os.system("cls")
            print("\nLa adivinaste! \n")
            print("\nLa palabra era", picked,".")
            break

def run():
    play()
   

if __name__=="__main__":
    run()