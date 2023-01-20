ante = int(input("Enter contribution (starting from 100$) :"))  # ante -> ставка
money = ante


#
# while True:
#     coin = randint(0, 1)
#     choiced = int(input("Выберите 1 или 0:"))
#     if money < ante + ante or money > 0:
#
#         if choiced == coin:
#             money += 7
#             print(f"You guessed it you get 7$ {money} $")
#         else:
#             if choiced != coin:
#                     money -= 10
#                     print(f"You lose 10$ {money}$")
#     else:
#         break
#

from random import randint
while 0 < money < 2 * money:

    coin = randint(0, 1)
    choiced = int(input("Выберите 1 или 0:"))

    if choiced not in (0, 1):
        print("enter only 0 or 1")
        continue
    if choiced == coin:
        print("Winner")
        money += 7
    else:
        print("Loser")
        money -= 10
    print("your current balance:", money, "$")

