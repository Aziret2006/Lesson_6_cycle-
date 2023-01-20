save = int(input("Сколько хотите накопить ?:"))
summ = 0
while save > summ:
    deposit = int(input("Deposit:"))
    summ += deposit
print("Congrats you have", summ, "$")
