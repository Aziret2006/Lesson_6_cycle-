from random import randint
random_number = randint(1, 100)

for i in range(10):
    ent = int(input("Guess number 1 to 100:"))
    if ent != random_number:
        if ent > random_number:
            print("Less", ent)
        elif ent < random_number:
            print("More", ent)
        else:
            print("You Lose, correct answer", random_number)
    else:
        print("Well done")
        break
