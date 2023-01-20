
number = input("enter number")
summ = 0

# for i in number:
#     summ += int(i)
# print(summ)

for index in range(len(number)):
    summ += int(number[index])
print(summ)

# digits = list()
# for char in number:
#     digits.append(int(char))
# summ = sum(digits)
#       print(summ)
print(f's,wl {number}')