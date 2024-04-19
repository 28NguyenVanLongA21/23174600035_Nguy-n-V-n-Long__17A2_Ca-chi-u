def main():
    # Nhập dãy số từ người dùng và chuyển đổi thành số thực
    numbers = [float(num) for num in input("Nhập dãy số, cách nhau bằng dấu cách: ").split()]

    # Tìm số lớn nhất và số nhỏ nhất trong dãy số
    max_number, min_number = max(numbers), min(numbers)

    # In kết quả
    print("Số lớn nhất trong dãy số là:", max_number)
    print("Số nhỏ nhất trong dãy số là:", min_number)

# Gọi hàm chính
main()