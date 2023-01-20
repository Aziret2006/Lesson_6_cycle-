summ = 0
number = 0
while summ <= 1000:
	print(number)
	summ += number
	number += 1

while True:
	number = int(input("enter number:"))
	if number > 100:
		print("Number then 100")

# break
count = 0
while count < 10:
	if count == 8:
		break
	print(count, "100")
	count += 1

#continue
count = 0
while count < 10:
	if count == 8:
		count += 2
		continue
	print(count, "100")
	count += 1



for i in range(10):
	if i % 2 == 0:
		continue
	if i % 2 == 0:
		print(i)
		break
	print(i)



