#kéo búa bao
from random import randint
you = input("mời nhập option của bạn: ")
computer = randint(1,3)
if computer == 1:
    computer = "kéo"
elif computer == 2:
    computer = "búa"
else:
    computer = "bao"
print("---------------------------------")
print("option cảu bạn là: ", you)
print("option của computer là : ", computer)
print("--------------------------------")
if you == computer:
    print("hòa")
elif you == "kéo":
    if computer == "búa":
        print("thua")
    elif computer == "bao":
        print("thắng")
elif you == "búa":
    if computer == "bao":
        print("thua")
    elif computer == "kéo":
        print("thắng")
elif you == "bao":
    if computer == "kéo":
        print("thua")
    elif computer == "búa":
        print("thắng")
else:
    print("bạn đã chon option ko hợp lệ.")
           
    