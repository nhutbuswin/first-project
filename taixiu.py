#nay chơi tài xĩu nha
from random import sample
option = [1,2,3,4,5,6]
nha_cai = sample(option, 3)
print(f"nhà cái mở ra 3 xúc sắc là: {nha_cai}")
total = sum(nha_cai)
you = input("bạn chọn tài hay xĩu: ")
print("--------------------------------")
print(f"lựa chọn cảu bạn là : {you}")
print(f"tổng số diểm nhà cái mở ra là: {total}")
print("--------------------------------")
if you == "xĩu":
    if total <= 10 and total >=4:
        print("win")
    else:
        print("lose")
elif you == "tài":
    if total >=11 and total <= 17:
        print("win")
    else:
        print("lose")
else:
    print("bạn đã chọn sai. vui lòng chọn lại!")
    
