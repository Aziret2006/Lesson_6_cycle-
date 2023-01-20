# print my name 10 times
for i in range(10):
    print("Aziret")

# 1 to 100 numbers
for i in range(1, 100):
    print(i)

# 1 to 100 even numbers
for i in range(1, 100):   # for i in range(100, 1, -2):
    if i % 2 == 0:             # print(i)
        print(i)

students = ['azat', 'awram', 'tramp']
for index in range(len(students)):
    students = students[index]
    if students == "tramp":
        print("Found student", index)
        break


names = ["Asia", 'java', 'tred', 'siri']
for name in names:
    if name == "java":
        print("yes")

"""name = "Sally"
for i in range(1, 10): # and range(10, 5, -1):
    for s in range(10):
        print(s, name)"""

# from random import randint
# win = True
# for i in range(10):
#     random_int = randint(1, 6)
#     human = int(input("Enter number 1 to 6 :").isdigit())
#     print("random number", random_int)
#     if random_int != human:
#         print("You lucky")
#     else:
#         print("You dead")
#         win = False
#         print("  You lose  ", win)
#         break

