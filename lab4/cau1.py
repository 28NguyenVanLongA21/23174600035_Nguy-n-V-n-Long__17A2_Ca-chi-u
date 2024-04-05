tong = 0
so_le = ""
so_chan = ""
so_luong = 0
while tong <= 1000:
    so = int(input("Nhập một số nguyên dương: "))
    tong += so
    so_luong += 1
    if so % 2 == 0:
        if so_chan:
            so_chan += " "
        so_chan += str(so)
    else:
        if so_le:
            so_le += " "
        so_le += str(so)
print("Các số lẻ đã nhập là:", so_le)
print("Các số chẵn đã nhập là:", so_chan)
print("Số lượng các số nguyên đã nhập:", so_luong)