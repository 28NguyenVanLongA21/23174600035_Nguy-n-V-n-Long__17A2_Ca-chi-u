def mix_strings(string1, string2):
    result = ""
    # Lặp qua cặp ký tự tương ứng từ hai chuỗi
    for char1, char2 in zip(string1, string2):
        # Thêm ký tự từ chuỗi đầu tiên
        result += char1
        # Thêm dấu gạch nối '-'
        result += '-'
        # Thêm ký tự từ chuỗi thứ hai
        result += char2
        # Thêm dấu gạch nối '-'
        result += '-'

    # Loại bỏ dấu gạch nối cuối cùng
    result = result[:-1]

    return result

# Chuỗi đầu vào
string1 = "Hello"
string2 = "World"

# Gọi hàm và hiển thị kết quả
output = mix_strings(string1, string2)
print(output)