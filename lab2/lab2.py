#cau 1
def giai_pt_bac_nhat(a, b):
    if a == 0:
        if b == 0:
            print("Phương trình vô số nghiệm")
        else:
            print("Phương trình vô nghiệm")
    else:
        x = -b / a
        print("Nghiệm của phương trình là:", x)

        if a > 0:
            print("Đồ thị hàm số nghịch biến trên (-∞,", x, ") và đồng biến trên (", x, ", +∞)")
        else:
            print("Đồ thị hàm số đồng biến trên (-∞,", x, ") và nghịch biến trên (", x, ", +∞)")
a = float(input("Nhập hệ số a: "))
b = float(input("Nhập hệ số b: "))
giai_pt_bac_nhat(a, b)
#cau 2
def chuso_hang_nghin(so):
    if so >= 1000:
        chuso = int(str(so)[0])
        print("Chữ số hàng nghìn của số", so, "là:", chuso)
    else:
        print("Không có chữ số hàng nghìn trong số", so)
        print("Kết quả là: 0")
so_nguyen = int(input("Nhập một số nguyên: "))
chuso_hang_nghin(so_nguyen)
#cau 3
def doc_so_hai_chu_so(chuso):
    hang_don_vi = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    hang_chuc = ["", "ten", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
    hang_teens = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]

    doc = ""

    if chuso >= 100:
        doc += hang_don_vi[chuso // 100] + " hundred "
        chuso %= 100

    if chuso >= 20:
        doc += hang_chuc[chuso // 10]
        if chuso % 10 != 0:
            doc += "-" + hang_don_vi[chuso % 10]
    elif chuso >= 10:
        doc += hang_teens[chuso % 10]
    elif chuso > 0:
        doc += hang_don_vi[chuso]

    return doc
so_nguyen = int(input("Nhập một số nguyên có ba chữ số: "))
print("Cách đọc của số này là:", doc_so_hai_chu_so(so_nguyen))

#cau 4
def xep_loai_diem(diem):
    if diem < 5:
        print("Điểm kém")
    elif diem < 7:
        print("Điểm trung bình")
    elif diem < 8.5:
        print("Điểm khá")
    else:
        print("Điểm tốt")
diem = float(input("Nhập điểm của bạn: "))
xep_loai_diem(diem)
#cau 5
def tinh_tong_tien(soluong_nguoi):
    gia_ve_mot_nguoi = 120000
    tong_tien = soluong_nguoi * gia_ve_mot_nguoi
    
    if 2 <= soluong_nguoi <= 4:
        tong_tien *= 0.95
    elif 4 < soluong_nguoi <= 10:
        tong_tien *= 0.9
    elif soluong_nguoi > 10:
        tong_tien *= 0.8
    
    return tong_tien
soluong_nguoi = int(input("Nhập số lượng người: "))
tong_tien = tinh_tong_tien(soluong_nguoi)
print("Tổng số tiền phải trả khi mua vé cho", soluong_nguoi, "người là:", int(tong_tien), "đồng")
#cau 6
def tim_so_lon_thu_hai(a, b, c):
    max_so_lon_nhat = max(a, b, c)
    min_so_nho_nhat = min(a, b, c)
    
    so_lon_thu_hai = a + b + c - max_so_lon_nhat - min_so_nho_nhat
    
    return so_lon_thu_hai
a = int(input("Nhập số nguyên dương thứ nhất: "))
b = int(input("Nhập số nguyên dương thứ hai: "))
c = int(input("Nhập số nguyên dương thứ ba: "))
so_lon_thu_hai = tim_so_lon_thu_hai(a, b, c)
print("Số lớn thứ hai trong ba số là:", so_lon_thu_hai)
#cau7
def tinh_chi_so_BMI(chieu_cao, can_nang):
    chi_so_BMI = can_nang / (chieu_cao ** 2)
    return chi_so_BMI

def phan_loai_BMI(chi_so_BMI):
    if chi_so_BMI < 18.5:
        return "Gầy"
    elif 18.5 <= chi_so_BMI < 25.0:
        return "Bình thường"
    elif 25.0 <= chi_so_BMI < 30.0:
        return "Hơi béo"
    else:
        return "Béo"
chieu_cao = float(input("Nhập chiều cao của bạn (mét): "))
can_nang = float(input("Nhập cân nặng của bạn (kg): "))
chi_so_BMI = tinh_chi_so_BMI(chieu_cao, can_nang)
phan_loai = phan_loai_BMI(chi_so_BMI)
print("Chỉ số BMI của bạn là:", chi_so_BMI)
print("Phân loại BMI của bạn là:", phan_loai)
#cau10
def chon_suatchieu(theloai, thoigian):
    if theloai == "Tình cảm" and thoigian == "tối":
        return "20:00"
    elif theloai == "Hoạt hình" and (thoigian == "sáng" or thoigian == "trưa"):
        return "10:00"
    elif theloai == "Kinh dị" and thoigian == "tối":
        return "22:00"
    else:
        return "Không có suất chiếu"
the_loai_phim = ["Hành động", "Kinh dị", "Tình cảm", "Hài hước", "Hoạt hình"]
thoi_gian_chieu = ["sáng", "trưa", "chiều", "tối"]

print("Các thể loại phim:")
for i, the_loai in enumerate(the_loai_phim, start=1):
    print(f"{i}. {the_loai}")

lua_chon_the_loai = int(input("Nhập số tương ứng với thể loại phim bạn muốn xem: "))
if lua_chon_the_loai < 1 or lua_chon_the_loai > len(the_loai_phim):
    print("Lựa chọn không hợp lệ!")
else:
    the_loai = the_loai_phim[lua_chon_the_loai - 1]
    print("Thời gian chiếu phim: sáng, trưa, chiều, tối")
    thoi_gian = input("Nhập thời gian muốn xem phim: ")
    thoi_gian_chieu = chon_suatchieu(the_loai, thoi_gian)
    print(f"Thời gian chiếu phim {the_loai} vào buổi {thoi_gian} là: {thoi_gian_chieu}")