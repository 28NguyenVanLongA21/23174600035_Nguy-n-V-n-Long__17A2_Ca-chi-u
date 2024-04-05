
num = int(input("Nhập vào một số nguyên: "))
count = 0
while num != 0:
    num //= 10
    count += 1
print("Số chữ số của số nguyên:", count)
