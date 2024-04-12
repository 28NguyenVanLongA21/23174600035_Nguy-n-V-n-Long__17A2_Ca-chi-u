def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def remove_non_digits_and_check_prime(string):
    # Loại bỏ tất cả các ký tự không phải là số
    cleaned_string = ''.join(filter(str.isdigit, string))

    # Kiểm tra chuỗi kết quả có phải là số nguyên tố không
    if cleaned_string.isdigit():
        number = int(cleaned_string)
        if is_prime(number):
            return f"{number} là số nguyên tố."
        else:
            return f"{number} không phải là số nguyên tố."
    else:
        return "Chuỗi không chứa số."

# Chuỗi ký tự đầu vào
input_string = input("Nhập chuỗi ký tự: ")

# Kiểm tra và hiển thị kết quả
result = remove_non_digits_and_check_prime(input_string)
print(result)