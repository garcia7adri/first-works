# def run():
#     squares=[]
#     for i in range (1,10001):
#         if i % 36== 0:
#             squares.append(i)
#     print(squares)
# if __name__== "__main__":
#     run()

# def run():
#     squares=[i for i in range (1,10001) if i % 36==0]
#     print (squares)

# if __name__== "__main__":
#     run()
# def run():

#      dictionario={ i: i**2 for i in range (1,101)  }
#      print(dictionario)

# if __name__== "__main__":
#     run()
# def run():
#     dict={}
#     for i in range (1,101):
#         if i % 3 ==0:
#             continue
#         dict[i]=i**3
#     print(dict)
# if __name__== "__main__":
#     run()

# from math import sqrt

# def run():
#     dict={i:round(sqrt(i),2) for i in range (1,1001)}
#     print (dict)

# if __name__== "__main__":
#     run()

# palindrome=lambda string: string == string [::-1]
# print (palindrome("ana"))

# def run():
#     my_list=[1,3,4,5,6]
#     dictionary={i : i**2 for i in (my_list)}
#     print (dictionary)

# if __name__== "__main__":
#     run()

DATA = [
    {
        'name': 'Facundo',
        'age': 72,
        'organization': 'Platzi',
        'position': 'Technical Coach',
        'language': 'python',
    },
    {
        'name': 'Luisana',
        'age': 33,
        'organization': 'Globant',
        'position': 'UX Designer',
        'language': 'javascript',
    },
    {
        'name': 'Héctor',
        'age': 19,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'ruby',
    },
    {
        'name': 'Gabriel',
        'age': 20,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'javascript',
    },
    {
        'name': 'Isabella',
        'age': 30,
        'organization': 'Platzi',
        'position': 'QA Manager',
        'language': 'java',
    },
    {
        'name': 'Karo',
        'age': 23,
        'organization': 'Everis',
        'position': 'Backend Developer',
        'language': 'python',
    },
    {
        'name': 'Ariel',
        'age': 32,
        'organization': 'Rappi',
        'position': 'Support',
        'language': '',
    },
    {
        'name': 'Juan',
        'age': 17,
        'organization': '',
        'position': 'Student',
        'language': 'go',
    },
    {
        'name': 'Pablo',
        'age': 32,
        'organization': 'Master',
        'position': 'Human Resources Manager',
        'language': 'python',
    },
    {
        'name': 'Lorena',
        'age': 16,
        'organization': 'Python Organization',
        'position': 'Language Maker',
        'language': 'python',
    },
]

def run():
    # all_python_devs=[worker["name"] for worker in DATA if worker ["language"]=="python"]
    # all_platzi_workers=[worker["name"] for worker in DATA if worker ["organization"]=="Platzi"]
    # adults=list(filter(lambda worker: worker ["age"]>18, DATA))
    # adults=list(map(lambda worker:worker["name"],adults))
    # old_people=list(map(lambda worker: worker | {"old":worker["age"]>70},DATA))

    # all_python_devs=list(filter(lambda worker : worker ["name"] | {worker: ["language"]="python", DATA))
  # 
    all_python_devs=[worker["name"] for worker in DATA if worker ["language"]=="python"]
    for worker in all_python_devs: 
        print(worker)


    
    all_python_devs=list(filter(lambda worker : worker ["language"]=="python", DATA))
    all_python_devs=list(map(lambda worker : worker ["name"],all_python_devs))
    for worker in all_python_devs:
        print(worker)

    # all_platzi_workers=list(filter(lambda worker: worker ["organization"]=="Platzi", DATA))
    # all_platzi_workers=list(map(lambda worker: worker ["name"], all_platzi_workers))
    # for worker in all_platzi_workers:
    #     print(worker)

    # old_people=[worker ["name"] for worker in DATA if worker ["age"]>70]
    # for worker in old_people:
    #     print(worker)

    
if __name__== "__main__":
    run()


#     with open("./files/new_words.txt", "w", encoding="utf-8") as f:
#         for word in words:
#             f.write(word)

# def read():
#     words=[]
#     with open("./DATA_AHORCADO.txt", "r", encoding="utf-8") as f:
#         for line in f:
#             words.append(line)
#     print (words)
# def run():
#     read()



    # def letter():
    #     new_letter=input("Por favor, escribe una letra: ")
    #     for letter in new_letter:
    #         print(letter)
# def get_word():
#     finalword=
#     for word in word_list:
#         choosenword=random.choice(word)
#         finalword.append(choosenword)