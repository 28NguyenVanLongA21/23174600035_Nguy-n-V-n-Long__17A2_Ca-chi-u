def count_characters(string):
    # Khởi tạo các biến đếm
    lowercase_count = 0
    uppercase_count = 0
    digit_count = 0
    special_count = 0

    # Lặp qua từng ký tự trong chuỗi
    for char in string:
        # Kiểm tra xem ký tự là chữ thường, chữ hoa, chữ số hay ký tự đặc biệt
        if char.islower():
            lowercase_count += 1
        elif char.isupper():
            uppercase_count += 1
        elif char.isdigit():
            digit_count += 1
        else:
            special_count += 1

    return lowercase_count, uppercase_count, digit_count, special_count

# Nhập chuỗi từ người dùng
input_string = input("Nhập chuỗi: ")

# Gọi hàm để đếm số lượng chữ thường, chữ hoa, chữ số và ký tự đặc biệt
lowercase, uppercase, digits, special = count_characters(input_string)

# Hiển thị kết quả
print(f"Số lượng chữ thường: {lowercase}")
print(f"Số lượng chữ hoa: {uppercase}")
print(f"Số lượng chữ số: {digits}")
print(f"Số lượng ký tự đặc biệt: {special}")