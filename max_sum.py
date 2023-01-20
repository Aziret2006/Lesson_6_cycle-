max_num = input("Enter numbers")
# maximum = max(max_num)
# print(maximum)

maxx = 0

for digit in max_num:
    if maxx < int(digit):
        maxx = int(digit)
print(maxx)
