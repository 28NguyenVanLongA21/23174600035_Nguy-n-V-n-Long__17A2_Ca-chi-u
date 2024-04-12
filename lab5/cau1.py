decimal_input = int(input("Nhập số nguyên dương (hệ thập phân): "))
if decimal_input < 0:
    print("Vui lòng nhập số nguyên dương.")
else:
    binary_output = format(decimal_input, 'b')
    print("Số nhị phân tương ứng là:", binary_output)