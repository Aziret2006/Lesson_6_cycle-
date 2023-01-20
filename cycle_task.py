imt_index = """"
-1000 -------- 16: Выраженный дефицит, \n
16 ------------ 18.5: Недостаточная масса тела, \n
18.5 ---------- 25: Норма, \n
25 ---------- 30: Избыточная масса тела, \n
30 ------------ 35: Ожирение 1 степень, \n
35 ------------ 40: Ожирение 2 степень, \n
40 ------------ 1000: Ожирение 3 степень, \n
"""

while True:
    h = float(input("Enter height:"))
    m = float(input("Enter weight: "))
    if h <= 0 and m <= 0:
        print("Вес или рост не должен быть меньше 0")
        continue
    else:
        imt = m / h**2
        print("Your IMT", imt)
        print(imt_index)
        print("---" * 20)
# TASK 2
login = "aziret@gmail.com"
password = "1234"
attemt = 0
while True:
    check_login = str(input("Enter your login:"))
    check_password = str(input("Enter your password:"))
    if attemt < 3:
        attemt += 1
        if check_login == login and check_password == check_password:
            print("Вы успешно прошли авторизацию!")
            break
        else:
            print("Вы вели неправильный пароль или логин")
    else:
        break
print("Вы заблокированы на 30 мин")



